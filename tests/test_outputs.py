import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "report.json was not created at /app/report.json"
    return json.loads(REPORT_PATH.read_text())


def test_output_file_is_valid_json():
    """Criterion 1: The output file must exist at /app/report.json and be valid JSON."""
    data = load_report()
    assert isinstance(data, dict)


def test_total_requests_is_correct():
    """Criterion 2: total_requests must equal the total number of log entries."""
    data = load_report()
    assert data.get("total_requests") == 6


def test_unique_ips_is_correct():
    """Criterion 3: unique_ips must equal the number of distinct client IP addresses."""
    data = load_report()
    assert data.get("unique_ips") == 3


def test_top_path_is_correct():
    """Criterion 4: top_path must equal the most frequently requested path."""
    data = load_report()
    assert data.get("top_path") == "/index.html"