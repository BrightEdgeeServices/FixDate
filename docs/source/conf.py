import sys

sys.path.insert(0, "D:\\Dropbox\\Projects\\FixDate\\src")
project = "FixDate"
copyright = "2022, Hendrik du Toit"
author = "Hendrik du Toit"
version = "1"
release = "0.0.1"
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "hendrikdutoit",  # Username
    "github_repo": "FixDate",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosummary"]
templates_path = ["_templates"]
language = "en"
exclude_patterns = []
html_theme = "bizstyle"
html_static_path = ["_static"]
autosummary_generate = True
autosummary_imported_members = True
