import asyncio
from pathlib import Path

from agent.agent import AlignmentExperimentAgent


async def main():
    workspace_dir = Path(__file__).parent
    run_dir = Path("/run_output")

    agent = AlignmentExperimentAgent(
        str(workspace_dir),
        str(run_dir)
    )

    print("Agent initialized. Starting experiment...")
    print("-" * 60)

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())