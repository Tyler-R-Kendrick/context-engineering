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
        assert 1 <= len(notebook["cells"]) <= 2, (
            f"{notebook_name} should contain 1-2 cells to stay concise"
        )

        markdown_text = "\n".join(
            "".join(cell["source"])
            for cell in notebook["cells"]
            if cell["cell_type"] == "markdown"
        )

        assert "Source slide:" in markdown_text, (
            f"{notebook_name} missing slide reference"
        )

        assert (
            "## Techniques" in markdown_text
            or "No standalone prompt technique examples" in markdown_text
        ), f"{notebook_name} missing technique-focused content"

        if "## Techniques" in markdown_text:
            for phrase in [
                "**Failure mode:**",
                "**Failure example:**",
                "**Technique:**",
                "**Improved example:**",
            ]:
                assert phrase in markdown_text, (
                    f"{notebook_name} missing {phrase!r}"
                )


def test_prompt_engineering_slide_notebook_code_cells_compile():
    for notebook_name in EXPECTED_NOTEBOOKS:
        notebook = load_notebook(notebook_name)

        for cell in notebook["cells"]:
            if cell["cell_type"] != "code":
                continue

            source = "".join(cell["source"])
            compile(source, notebook_name, "exec")
