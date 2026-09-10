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
import json
import asyncio

# Add agent to path
sys.path.insert(0, str(Path(__file__).parent / "agent"))

from agent import AlignmentExperimentAgent


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
    
    # Initialize and run agent
    try:
        agent = AlignmentExperimentAgent(str(workspace_dir), str(run_dir))
        print("\nAgent initialized. Starting experiment...")
        print("-" * 60)
        
        asyncio.run(agent.run())
        
        print("-" * 60)
        summary = agent.get_summary()
        
        print("\nExperiment completed.")
        print(f"Submissions made: {summary['submissions_made']}/3")
        for sub in summary['submissions']:
            print(f"  {sub['submission_number']}: {sub['timestamp']} - Score: {sub['score']}")
        
        print(f"\nFull log: {summary['log_file']}")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
