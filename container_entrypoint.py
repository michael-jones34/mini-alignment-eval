import asyncio
import os
from pathlib import Path

from agent.agent import AlignmentExperimentAgent


async def main():
    workspace_dir = Path(__file__).parent
    run_dir = Path("/run_output")
    run_id = os.environ["RUN_ID"]

    agent = AlignmentExperimentAgent(
        str(workspace_dir),
        str(run_dir),
        run_id
    )

    print("Agent initialized. Starting experiment...")
    print("-" * 60)

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())