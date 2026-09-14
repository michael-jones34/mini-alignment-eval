# Quick Start Guide

## Setup (First Time Only)

### Windows PowerShell

```powershell
cd "Alignment Eval"

.\setup.ps1
```

This will:

1. Create a Python virtual environment (`.venv`)
2. Install the required dependencies
3. Display activation instructions

### Linux/Mac

```bash
cd "Alignment Eval"

bash setup.sh
```

## Running the Experiment

### Activate the Virtual Environment

**Windows PowerShell:**

```powershell
cd "Alignment Eval"

.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` appear in your prompt.

**Linux/Mac:**

```bash
cd "Alignment Eval"

source .venv/bin/activate
```

### Set Your OpenAI API Key

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="sk-..."
```

**Linux/Mac:**

```bash
export OPENAI_API_KEY="sk-..."
```

### Run the Experiment

```bash
python main.py
```

The experiment will:

1. Start the host-side evaluator server
2. Build and run the agent inside a Docker container
3. Give the agent access to the corrupted dataset and its tools
4. Allow up to three submissions
5. Return a numerical score after each successful submission
6. Save logs and outputs to the local `runs/` directory

Each run creates its own directory:

```text
runs/run_<run_id>/
```

Run artefacts are local and are gitignored; they are not committed to the repository.

## Testing

Run the grader tests with:

```bash
python -m pytest tests/test_grader.py -v
```

These tests cover the local grading and submission-tracking components. They do not replace running the full agent experiment.

## Project Structure

```text
Alignment Eval/
├── data/
│   ├── corrupted.csv          # Input: corrupted tensile-test data
│   └── ground_truth.csv       # Researcher-only reference data
├── agent/
│   ├── agent.py               # Agent implementation
│   └── __init__.py
├── grader/
│   ├── grader.py              # Scoring logic
│   ├── submission_tracker.py  # Submission-limit enforcement
│   └── __init__.py
├── tests/
│   └── test_grader.py         # Grader tests
├── runs/                      # Local experiment logs and outputs (gitignored)
├── main.py                    # Experiment entry point
├── evaluator_server.py        # Host-side evaluator server
├── container_entrypoint.py    # Container entry point
├── Dockerfile                 # Agent container definition
├── validate.py                # Setup/validation checks
├── requirements.txt           # Python dependencies
├── setup.ps1                  # Windows setup script
├── setup.sh                   # Linux/Mac setup script
├── .gitignore                 # Git ignore patterns
├── README.md                  # Full project documentation
└── quickstart.md              # This guide
```

## Troubleshooting

### `OPENAI_API_KEY` not set

Set the environment variable before running the experiment.

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="sk-..."

python main.py
```

**Linux/Mac:**

```bash
export OPENAI_API_KEY="sk-..."

python main.py
```

### Docker is not running

The experiment runs the agent inside Docker. Make sure Docker Desktop (Windows/Mac) or Docker Engine (Linux) is running before executing:

```bash
python main.py
```

### Virtual environment not activating

**Windows PowerShell:**

```powershell
& ".\.venv\Scripts\Activate.ps1"
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### Tests not found

Make sure you are in the project directory and that the virtual environment is activated:

```bash
cd "Alignment Eval"

python -m pytest tests/test_grader.py -v
```

## Key Files

- **Experiment entry point:** [main.py](main.py)
- **Agent implementation:** [agent/agent.py](agent/agent.py)
- **Container entry point:** [container_entrypoint.py](container_entrypoint.py)
- **Evaluator server:** [evaluator_server.py](evaluator_server.py)
- **Grader logic:** [grader/grader.py](grader/grader.py)
- **Tests:** [tests/test_grader.py](tests/test_grader.py)
- **Full documentation:** [README.md](README.md)