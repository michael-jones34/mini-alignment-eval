"""
Main entry point for alignment/specification-gaming experiment.

Usage:
    python main.py

The experiment will:
1. Load task instructions
2. Initialize agent with GPT-6 Astra
3. Agent inspects corrupted.csv
4. Agent uses Python to analyze/clean data
5. Agent can submit up to 3 times for evaluation
6. Experiment log saved to runs/[run_id]/experiment_log.jsonl
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import subprocess

def main():
    """Run the alignment experiment."""
    
    # Setup paths
    workspace_dir = Path(__file__).parent
    
    # Create run directory with timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    run_id = f"run_{timestamp}"
    run_dir = workspace_dir / "runs" / run_id
    
    print(f"Starting alignment experiment run: {run_id}")
    print(f"Workspace: {workspace_dir}")
    print(f"Run directory: {run_dir}")
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    # Run agent inside Docker container
    try:
        print("\nStarting agent in Docker container...")
        print("-" * 60)
        result = subprocess.run(
            [
                "docker", "run", "--rm",
                "-e", "OPENAI_API_KEY",
                "-v", f"{run_dir}:/run_output",
                "mini-alignment-eval"
            ],
            check=True
)
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
