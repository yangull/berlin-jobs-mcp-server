import types
import tools.search as search_module
from tools.search import search_jobs


def _make_job(**kwargs):
    defaults = {"id": 1, "title": "Backend Engineer", "company": "Acme GmbH",
                "seniority": "Senior", "tech_stack": "Python, FastAPI",
                "url": "https://example.com/job/1", "description": "Build great APIs"}
    defaults.update(kwargs)
    return types.SimpleNamespace(**defaults)


def _mock_session(results):
    return types.SimpleNamespace(
        query=lambda model: types.SimpleNamespace(
            filter=lambda *_: types.SimpleNamespace(all=lambda: results)
        ),
        close=lambda: None
    )


def test_returns_matching_jobs(monkeypatch):
    jobs = [_make_job(), _make_job(id=2, title="Python Developer", company="Beta GmbH")]
    monkeypatch.setattr(search_module, "get_db_session", lambda: _mock_session(jobs))
    result = search_jobs("Python")
    assert "Backend Engineer" in result
    assert "Acme GmbH" in result
    assert "Found 2 job(s)" in result


def test_returns_no_results_message(monkeypatch):
    monkeypatch.setattr(search_module, "get_db_session", lambda: _mock_session([]))
    result = search_jobs("nonexistent-xyz")
    assert "No jobs found" in result


def test_shows_seniority_and_tech_stack(monkeypatch):
    jobs = [_make_job(seniority="Junior", tech_stack="Go, Kubernetes")]
    monkeypatch.setattr(search_module, "get_db_session", lambda: _mock_session(jobs))
    result = search_jobs("Go")
    assert "Junior" in result
    assert "Go, Kubernetes" in result


def test_shows_unknown_when_seniority_is_none(monkeypatch):
    jobs = [_make_job(seniority=None, tech_stack=None)]
    monkeypatch.setattr(search_module, "get_db_session", lambda: _mock_session(jobs))
    result = search_jobs("anything")
    assert "Unknown" in result
    assert "Not specified" in result
