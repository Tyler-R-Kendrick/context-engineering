import ast
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks" / "prompt-engineering"
EXPECTED_NOTEBOOKS = [
    "01-introduction-to-prompt-engineering.ipynb",
    "02-types-of-prompts.ipynb",
    "03-anatomy-of-an-effective-prompt.ipynb",
    "04-prompt-engineering-techniques-overview.ipynb",
    "04-1-basic-techniques.ipynb",
    "04-2-reasoning-techniques.ipynb",
    "04-3-rag.ipynb",
    "04-4-parameter-tuning.ipynb",
    "04-5-constrained-decoding.ipynb",
    "06-best-practices-for-effective-prompts.ipynb",
    "09-resources-for-further-learning.ipynb",
]


def load_notebook(notebook_name: str) -> dict:
    return json.loads((NOTEBOOKS_DIR / notebook_name).read_text())


def test_prompt_engineering_slide_notebooks_exist():
    actual = sorted(path.name for path in NOTEBOOKS_DIR.glob("*.ipynb"))
    assert actual == sorted(EXPECTED_NOTEBOOKS)


def test_prompt_engineering_slide_notebooks_have_required_sections():
    for notebook_name in EXPECTED_NOTEBOOKS:
        notebook = load_notebook(notebook_name)

        markdown_text = "\n".join(
            "".join(cell["source"])
            for cell in notebook["cells"]
            if cell["cell_type"] == "markdown"
        )

        assert "Source slide:" in markdown_text, (
            f"{notebook_name} missing slide reference"
        )

        if "No technique examples are added here" in markdown_text:
            assert len(notebook["cells"]) == 2, (
                f"{notebook_name} should stay brief for non-technique slides"
            )
        else:
            assert len(notebook["cells"]) >= 5, (
                f"{notebook_name} should include setup and technique demos"
            )
            assert "## Prerequisites" in markdown_text, (
                f"{notebook_name} missing prerequisites"
            )
            for phrase in [
                "**Failure mode:**",
                "**Failure test:**",
                "**Technique:**",
                "**Improved example:**",
            ]:
                assert phrase in markdown_text, (
                    f"{notebook_name} missing {phrase!r}"
                )


def test_prompt_engineering_technique_notebooks_use_real_copilot_sdk():
    technique_notebooks = [
        notebook_name
        for notebook_name in EXPECTED_NOTEBOOKS
        if notebook_name
        not in {
            "01-introduction-to-prompt-engineering.ipynb",
            "09-resources-for-further-learning.ipynb",
        }
    ]

    for notebook_name in technique_notebooks:
        notebook_text = (NOTEBOOKS_DIR / notebook_name).read_text()

        assert "from copilot import CopilotClient" in notebook_text
        assert "from copilot.session import PermissionHandler" in notebook_text
        assert "PermissionHandler.approve_all" in notebook_text
        assert "create_session(" in notebook_text
        assert "await ask_copilot(" in notebook_text
        assert "ambient auth" in notebook_text
        assert "fake" not in notebook_text.lower()


def test_prompt_engineering_slide_notebook_code_cells_compile():
    for notebook_name in EXPECTED_NOTEBOOKS:
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
