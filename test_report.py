"""Tests sur l'agrégation et le formatage, sans appel réseau."""

import json

from httpsentinel.findings import Finding, Severity
from httpsentinel.report import to_json, to_terminal, _summary_line


def _sample():
    return [
        Finding("headers", "CSP absent", Severity.MEDIUM, recommendation="Ajouter une CSP."),
        Finding("tls", "Version TLS : TLSv1.3", Severity.OK),
        Finding("exposed_files", "Exposé : /.env", Severity.HIGH, detail="HTTP 200"),
    ]


def test_json_structure():
    data = json.loads(to_json("https://exemple.fr", _sample()))
    assert data["target"] == "https://exemple.fr"
    assert len(data["findings"]) == 3
    # Trié par sévérité : HIGH en premier
    assert data["findings"][0]["severity"] == "HIGH"


def test_summary_counts():
    line = _summary_line(_sample())
    assert "1 HIGH" in line
    assert "1 MEDIUM" in line


def test_terminal_no_color_has_no_ansi():
    out = to_terminal("https://exemple.fr", _sample(), color=False)
    assert "\033[" not in out
    assert ".env" in out
