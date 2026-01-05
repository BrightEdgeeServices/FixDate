# Release 2.1.0

- Implementation of fork workflows
- Major configuration update
  - Comprehensive update of `.gitignore`
  - Update Poetry dependencies and configuration
  - Update pre-commit hooks and configuration
  - Update project metadata and classifiers in `pyproject.toml`
- Improvements to documentation
  - Updated `README.md` with detailed Overview, Features, and Usage examples
  - Removed deprecated `README.rst`
- Workflow and CI/CD updates
  - Added reusable GitHub Action workflows for PR and Publishing
  - Removed outdated GitHub Action templates and issue templates
- Utility script updates
  - Added `Install.ps1` and `SetupGitHubAccess.ps1`
  - Updated `InstallDevEnv.ps1`, `SetupDotEnv.ps1`, and `SetupPrivateRepoAccess.ps1`
- Miscellaneous
  - Renamed `LICENSE` to `LICENSE.txt`
  - Removed redundant `scripts/setup_db.sql` and `.idea` configuration files
- Statistics
  - Changed files: .github/CODEOWNERS, .github/ISSUE_TEMPLATE/bugfix.md, .github/ISSUE_TEMPLATE/config.yaml, .github/ISSUE_TEMPLATE/enhancement.md, .github/ISSUE_TEMPLATE/hotfix.md, .github/ISSUE_TEMPLATE/release.md, .github/workflows/py-temp-pr-pub-no_docker-def.yaml, .github/workflows/py-temp-publish-pub-build_release_notify_after_merge-def.yaml, .github/workflows/python-template-pypi-public-no-docker.yaml, .gitignore, .idea/.gitignore, .idea/FixDate.iml, .idea/dbnavigator.xml, .idea/dictionaries, .idea/inspectionProfiles/Project_Default.xml, .idea/markdown.xml, .idea/misc.xml, .idea/vcs.xml, .pre-commit-config.yaml, Install.ps1, InstallDevEnv.ps1, LICENSE.txt, README.md, README.rst, SetupDotEnv.ps1, SetupGitHubAccess.ps1, SetupPrivateRepoAccess.ps1, coverage.xml, poetry.lock, pyproject.toml, scripts/setup_db.sql
  - Number of files changed: 31
  - Insertations: 358
  - Deletions: 937
  - Branch name: hendrik/urs-313-feature-fixdate-remove-discontinued-workflow

______________________________________________________________________

# Release 2.0.1

- Update ISSUE_TEMPLATE's
- Implement GitHub Reusable workflows.
- Upgrade to support Python 13.1
- Update formatting configuration files
  - flake8
  - .gitattributes
  - .gitignore
  - .pre-commit-config.yaml
  - readthedocs.yaml
  - rstcheck.cfg
- Delete redundant files
  - fixdate.bat
  - install.ps1
- Add utility scripts
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1

______________________________________________________________________

# Release 2.0.0

- Update ISSUE_TEMPLATE's
- Update GitHub Workflows
- Move code from `Code` directory to `src` directory
- Implemented Poetry
- Removed irrelevant info from README.rst

______________________________________________________________________
