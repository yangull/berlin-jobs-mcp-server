import types
import tools.details as details_module
from tools.details import get_job_details


def _make_job(**kwargs):
    defaults = {"id": 1, "title": "Backend Engineer", "company": "Acme GmbH",
                "seniority": "Senior", "tech_stack": "Python, FastAPI",
                "url": "https://example.com/job/1", "description": "Build great APIs"}
    defaults.update(kwargs)
    return types.SimpleNamespace(**defaults)


def _mock_session(job):
    return types.SimpleNamespace(
        query=lambda model: types.SimpleNamespace(
            filter=lambda *_: types.SimpleNamespace(first=lambda: job)
        ),
        close=lambda: None
    )


def test_returns_full_job_details(monkeypatch):
    job = _make_job()
    monkeypatch.setattr(details_module, "get_db_session", lambda: _mock_session(job))
    result = get_job_details(1)
    assert "Backend Engineer" in result
    assert "Acme GmbH" in result
    assert "Python, FastAPI" in result
    assert "https://example.com/job/1" in result
    assert "Build great APIs" in result


def test_returns_not_found_for_missing_id(monkeypatch):
    monkeypatch.setattr(details_module, "get_db_session", lambda: _mock_session(None))
    result = get_job_details(999)
    assert "No job found" in result
    assert "999" in result


def test_shows_unknown_when_seniority_is_none(monkeypatch):
    job = _make_job(seniority=None, tech_stack=None)
    monkeypatch.setattr(details_module, "get_db_session", lambda: _mock_session(job))
    result = get_job_details(1)
    assert "Unknown" in result
    assert "Not specified" in result
