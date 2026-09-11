from http.server import BaseHTTPRequestHandler, HTTPServer
import tempfile
from evaluator import Evaluator
import json

evaluators = {}

class EvaluatorHandler(BaseHTTPRequestHandler):
    """HTTP handler for host-side evaluation requests."""

    def do_POST(self):
        if self.path != "/submit":
            self.send_error(404)
            return
        run_id = self.headers.get("X-Run-ID")
        if not run_id:
            self.send_error(400, "Missing X-Run-ID")
            return
        if run_id not in evaluators:
            print(f"Creating evaluator for run_id={run_id}, run_dir=runs/{run_id}", flush=True)
            evaluators[run_id] = Evaluator(
                ".",
                f"runs/{run_id}"
            )

        evaluator = evaluators[run_id]
        try:
            content_length = int(self.headers["Content-Length"])
        except (TypeError, ValueError):
            self.send_error(400, "Missing or invalid Content-Length")
            return

        if content_length > 10 * 1024 * 1024:
            self.send_error(413, "Submission too large")
            return

        body = self.rfile.read(content_length)

        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            f.write(body)
            submission_path = f.name

        try:
            score = evaluator.evaluate(submission_path)
        except RuntimeError as e:
            if "Submission limit (3) exceeded" in str(e):
                self.send_error(429, str(e))
            else:
                self.send_error(500, str(e))
        except Exception as e:
            self.send_error(500, str(e))
            return

        response = json.dumps({"score": score}).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), EvaluatorHandler)
    print("Evaluator server listening on 0.0.0.0:8000")
    server.serve_forever()