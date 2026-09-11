"""
Authoritative host-side evaluator for the alignment experiment.

This component owns the real grader and submission tracker. It is intended
to run outside the agent's Docker container.
"""

from pathlib import Path

from grader.grader import Grader
from grader.submission_tracker import SubmissionTracker


class Evaluator:
    """Authoritative evaluator for agent submissions."""

    def __init__(self, workspace_dir: str, run_dir: str):
        self.workspace_dir = Path(workspace_dir)
        self.run_dir = Path(run_dir)

        ground_truth_path = self.workspace_dir / "data" / "ground_truth.csv"

        self.grader = Grader(str(ground_truth_path))
        self.tracker = SubmissionTracker(str(self.run_dir))

    def evaluate(self, submission_path: str) -> int:
        """
        Grade a submission and record the result.

        Args:
            submission_path: Path to the submission CSV on the host.

        Returns:
            Numerical score from the grader.
        """
        if not self.tracker.can_submit():
            raise RuntimeError("Submission limit (3) exceeded")

        score = self.grader.grade(submission_path)

        self.tracker.record_submission(submission_path, score)

        return score