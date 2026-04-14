import ast
import json
import sys
import textwrap
import types
from pathlib import Path
from types import SimpleNamespace

import pytest


REPO_ROOT = Path("/home/runner/work/context-engineering/context-engineering")
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def load_notebook(notebook_name: str) -> dict:
    return json.loads((NOTEBOOKS_DIR / notebook_name).read_text())


def load_code_cell(notebook_name: str, cell_index: int) -> str:
    notebook = load_notebook(notebook_name)
    return "".join(notebook["cells"][cell_index]["source"])


def install_fake_copilot_modules():
    calls: list[dict] = []

    class FakeSession:
        def __init__(self, kwargs):
            self.kwargs = kwargs
            self.prompts = []

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        async def send_and_wait(self, prompt):
            self.prompts.append(prompt)
            return SimpleNamespace(
                data=SimpleNamespace(content=f"reply:{prompt}")
            )

    class FakeClient:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        async def create_session(self, **kwargs):
            session = FakeSession(kwargs)
            calls.append({"kwargs": kwargs, "session": session})
            return session

    permission_handler = SimpleNamespace(approve_all=object())

    copilot_module = types.ModuleType("copilot")
    copilot_module.CopilotClient = FakeClient

    session_module = types.ModuleType("copilot.session")
    session_module.PermissionHandler = permission_handler

    return calls, permission_handler, {
        "copilot": copilot_module,
        "copilot.session": session_module,
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "notebook_name",
    [
        "03-prompt-engineering-with-github-models.ipynb",
        "04-context-optimization.ipynb",
        "05-rag-context-pipeline.ipynb",
    ],
)
async def test_setup_cells_use_copilot_sdk_auth(notebook_name: str):
    calls, permission_handler, modules = install_fake_copilot_modules()
    namespace = {}

    with pytest.MonkeyPatch.context() as monkeypatch:
        for module_name, module in modules.items():
            monkeypatch.setitem(sys.modules, module_name, module)
        exec(load_code_cell(notebook_name, 1), namespace)
        result = await namespace["ask_copilot"](
            "Hello from a notebook",
            system_message="Stay concise.",
        )

    assert result == "reply:Hello from a notebook"
    assert namespace["model"] == "gpt-4.1"
    assert namespace["estimate_tokens"]("abcd") == 1
    assert namespace["estimate_tokens"]("abcdefgh") == 2

    assert len(calls) == 1
    session_kwargs = calls[0]["kwargs"]
    assert session_kwargs["model"] == "gpt-4.1"
    assert (
        session_kwargs["on_permission_request"]
        is permission_handler.approve_all
    )
    assert session_kwargs["system_message"] == {
        "mode": "append",
        "content": "Stay concise.",
    }


@pytest.mark.asyncio
async def test_prompt_notebook_reuses_single_session_for_context_chaining():
    calls, _, modules = install_fake_copilot_modules()
    namespace = {}

    with pytest.MonkeyPatch.context() as monkeypatch:
        for module_name, module in modules.items():
            monkeypatch.setitem(sys.modules, module_name, module)

        notebook_file = "03-prompt-engineering-with-github-models.ipynb"
        exec(load_code_cell(notebook_file, 1), namespace)
        contextual_chaining_code = load_code_cell(
            notebook_file,
            12,
        )
        wrapped = "async def _run_cell():\n" + textwrap.indent(
            contextual_chaining_code,
            "    ",
        )
        exec(wrapped, namespace)
        await namespace["_run_cell"]()

    assert len(calls) == 1
    assert calls[0]["session"].prompts == [
        (
            "Create a User model with id, email, and name fields using "
            "dataclasses."
        ),
        (
            "Add validation methods to ensure email is valid and name is not "
            "empty."
        ),
        (
            "Create a UserRepository class with CRUD operations using this "
            "User model."
        ),
    ]


@pytest.mark.parametrize(
    "notebook_name",
    [
        "03-prompt-engineering-with-github-models.ipynb",
        "04-context-optimization.ipynb",
        "05-rag-context-pipeline.ipynb",
    ],
)
def test_code_cells_compile_with_top_level_await(notebook_name: str):
    notebook = load_notebook(notebook_name)

    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        compile(
            source,
            notebook_name,
            "exec",
            flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT,
        )


@pytest.mark.parametrize(
    "notebook_name",
    [
        "03-prompt-engineering-with-github-models.ipynb",
        "04-context-optimization.ipynb",
        "05-rag-context-pipeline.ipynb",
    ],
)
def test_notebooks_remove_pat_based_azure_model_usage(notebook_name: str):
    notebook_text = (NOTEBOOKS_DIR / notebook_name).read_text()

    assert "azure.ai.inference" not in notebook_text
    assert "AzureKeyCredential" not in notebook_text
    assert "GITHUB_TOKEN" not in notebook_text
    assert "github-copilot-sdk" in notebook_text
