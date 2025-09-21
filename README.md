# AI Coding Setup

Repository skeleton for orchestrating AI-assisted software development across multiple providers (Anthropic Claude, OpenAI, Google Gemini, DeepSeek, Ollama, ...). It codifies spec-first habits, safe Git checkpoints, MCP tool access, and shared prompts so teams can bootstrap new projects quickly.

## Quick start

1. Run `python scripts/repo/setup_wizard.py` to select assistants, populate `.env`, and review environment prerequisites.
2. Prepare your workstation following the [operating system setup](#operating-system-setup) guidance below (the wizard highlights the tasks to prioritise).
3. Run `make setup` (or the equivalent commands listed for your OS) to install dependencies and register recommended pre-commit hooks.
4. Explore the docs:
   - `docs/PROJECT_SPEC.md` for business goals
   - `docs/TECHNICAL_SPEC.md` for architecture plans
   - `docs/CLAUDE.md` for Claude-oriented practices (MCP, git hygiene, auto-accept policy)
5. Trigger workflows with `python scripts/ai/run_workflow.py --task spec-first --assistant anthropic/claude-3.7-sonnet`.

## Interactive setup wizard

The wizard at `scripts/repo/setup_wizard.py` guides you through the most important configuration steps:

- Detects your operating system and reiterates the prerequisites from this README.
- Lets you confirm or override task-to-assistant routing in `configs/assistants.yaml`.
- Collects provider credentials and writes them to `.env`, preserving any custom entries.
- Verifies that required tooling (Python, Git, `pip`, etc.) is installed and that each referenced provider has credentials.

Re-run the wizard later with `python scripts/repo/setup_wizard.py --check` to validate your environment without prompts.

## Operating system setup

All platforms need:

- Git 2.40+
- Python 3.10 or newer with `pip`
- Access to the provider API keys you plan to use
- `make` **or** the ability to run the equivalent shell commands shown in each section

Follow the section that matches your environment before running `make setup`.

### macOS (Apple Silicon or Intel)

1. Install the Xcode Command Line Tools for Git: `xcode-select --install`.
2. Install Homebrew if you do not already have it: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
3. Use Homebrew to install Python tooling:
   ```bash
   brew install python@3.11 git pre-commit
   ```
4. (Optional) Install `gnu-getopt` if you prefer `gmake` syntax: `brew install gnu-getopt`.
5. From the repository root, create and activate the virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```
6. Run `make setup` or execute `pip install -r requirements.txt`, `pip install pre-commit`, and `pre-commit install` manually.

### Linux (Debian/Ubuntu)

1. Update package lists: `sudo apt update`.
2. Install the required build and Python tooling:
   ```bash
   sudo apt install -y build-essential python3 python3-venv python3-pip git make
   ```
3. (Optional) Install `pre-commit` globally with `pipx` if you prefer isolation: `pipx install pre-commit`.
4. From the repository root, run:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   make setup
   ```
   If `make` is unavailable, run the commands under the `make setup` recipe manually (see the `Makefile`).

### Windows 11 (recommended: WSL2)

1. Enable the Windows Subsystem for Linux and install an Ubuntu distribution by following [Microsoft's guide](https://learn.microsoft.com/windows/wsl/install).
2. Inside the WSL terminal, follow the [Linux instructions](#linux-debianubuntu) above.
3. If you need to edit files from Windows, use VS Code's "WSL" extension or another editor that understands the WSL file system to avoid permission issues.

### Windows (native PowerShell)

1. Install [Git for Windows](https://git-scm.com/download/win) and ensure `git` is available in PowerShell.
2. Install [Python 3.11+](https://www.python.org/downloads/windows/) and check `Add python.exe to PATH` during setup.
3. Install [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) **or** plan to run the underlying commands manually.
4. In an *Administrator* PowerShell prompt, install virtual environment tooling:
   ```powershell
   py -3 -m pip install --upgrade pip virtualenv
   ```
5. From the repository directory:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   pip install pre-commit
   pre-commit install
   ```
6. If `pre-commit` blocks the shell policy, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.

After the environment is prepared, run `python scripts/repo/validate_config.py` to confirm the template configuration loads correctly.

## Using this template in a new project

1. **Create your repository.** Either fork this repo or use GitHub's "Use this template" feature to start with a clean history.
2. **Fill in the specs first.** Complete `docs/PROJECT_SPEC.md` and `docs/TECHNICAL_SPEC.md` before writing code so agents can reference them.
3. **Configure assistants.** Update `configs/assistants.yaml` and the files under `assistants/` (the setup wizard can walk you through the defaults).
4. **Secure credentials.** Run `python scripts/repo/setup_wizard.py` to populate `.env` with the necessary secrets, or copy `.env.example` manually if you prefer.
5. **Bootstrap tooling.** Run `make setup` (or the manual commands from the OS sections) followed by `python scripts/repo/validate_config.py` to ensure everything is wired together.
6. **Iterate with safe checkpoints.** Follow the spec-first workflow (`workflows/spec-first.yml`), commit frequently, and rely on `docs/CLAUDE.md` for rules about MCP tools, auto-accept limits, and Git hygiene.
7. **Customize further.** Replace the sample `examples/demo_project` contents, add source code under `src/`, and flesh out `tests/` as you build features.

## Repository layout

See `docs/CLAUDE.md` and `docs/PROJECT_SPEC.md` for full descriptions. Highlights:

- `assistants/` – parameter files per provider/model.
- `prompts/` – reusable prompt modules (system/global/task).
- `workflows/` – orchestration recipes for spec-first, review, and migration flows.
- `mcp/servers/` – Model Context Protocol definitions for safe tool use.
- `scripts/` – automation helpers (AI workflows + repo bootstrap/validation).

## Recommended reading

- [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code quickstart (YouTube)](https://www.youtube.com/watch?v=amEUIuBKwvg)
- [Agentic workflows deep-dive (YouTube)](https://www.youtube.com/watch?v=T0zFZsr_d0Q)

Adopt spec-first planning and commit often for recoverable checkpoints.
