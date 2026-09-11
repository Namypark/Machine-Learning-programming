# Machine-Learning-programming

I used `uv` instead of `pip` to manage this project's dependencies. A
`requirements.txt` file is also included in case you prefer to use `pip`.

## Setup

Use Python 3.13 or newer and run the commands from the project folder.
Choose either option below.

### Using uv

With `uv` installed, create the `.venv` environment and install dependencies:

```bash
uv sync
```

Activate the environment on macOS or Linux:

```bash
source .venv/bin/activate
```

### Using pip

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `python` instead of `python3`. For either option, activate the
environment in PowerShell with `.venv\Scripts\Activate.ps1` instead of the
`source` command.
