# Quick Start Guide

## Setup (First Time Only)

### Windows PowerShell
```powershell
cd "Alignment Eval"
.\setup.ps1
```

This will:
1. Create a Python virtual environment (.venv)
2. Install all dependencies (openai, pandas, pytest)
3. Display activation instructions

### Linux/Mac
```bash
cd Alignment\ Eval
bash setup.sh
```

## Running the Experiment

### Activate Virtual Environment

**Windows PowerShell:**
```powershell
cd "Alignment Eval"
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` appear in your prompt.

**Linux/Mac:**
```bash
cd Alignment\ Eval
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

### Verify Setup

```bash
python validate.py
```

Should show: ✓ All validation checks passed!

### Run the Experiment

```bash
python main.py
```

The agent will:
1. Inspect the corrupted dataset
2. Clean the data using Python
3. Submit the cleaned dataset (up to 3 times)
4. Receive a numerical score after each submission

Results will be saved to: `runs/run_[timestamp]/experiment_log.jsonl`

## Testing

### Run All Tests
```bash
python -m pytest tests/test_grader.py -v
```

### Run Specific Test
```bash
python -m pytest tests/test_grader.py::TestGrader::test_perfect_submission -v
```

## Project Structure

```
Alignment Eval/
├── .venv/                 # Virtual environment (created by setup.ps1/sh)
├── data/
│   ├── corrupted.csv      # Input: corrupted tensile-test data
│   └── ground_truth.csv   # Researcher-only: expected cleaned data
├── agent/
│   ├── agent.py           # OpenAI Agent implementation
│   └── __init__.py
├── grader/
│   ├── grader.py          # Scoring logic
│   ├── submission_tracker.py  # 3-submission limit enforcement
│   └── __init__.py
├── tests/
│   └── test_grader.py     # Comprehensive test suite
├── runs/                  # Experiment logs and outputs
├── main.py                # Entry point
├── validate.py            # Validation script
├── requirements.txt       # Dependencies
├── setup.ps1              # Windows setup script
├── setup.sh               # Linux/Mac setup script
├── .gitignore             # Git ignore patterns
└── README.md              # Full documentation
```

## Troubleshooting

### "OPENAI_API_KEY not set"
Make sure you've set the environment variable before running:
```powershell
$env:OPENAI_API_KEY="sk-..."
python main.py
```

### Virtual environment not activating
Try running the activation command with full path:
```powershell
cd Alignment\ Eval
& ".\.venv\Scripts\Activate.ps1"
```

### Permission denied on setup.sh (Linux/Mac)
```bash
chmod +x setup.sh
bash setup.sh
```

### Tests not found
Make sure you're in the project directory and the virtual environment is activated:
```bash
cd Alignment\ Eval
source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
python -m pytest tests/test_grader.py -v
```

## Key Files

- **Experiment entry point:** [main.py](main.py)
- **Agent implementation:** [agent/agent.py](agent/agent.py)
- **Grader logic:** [grader/grader.py](grader/grader.py)
- **Tests:** [tests/test_grader.py](tests/test_grader.py)
- **Full documentation:** [README.md](README.md)
