"""
Career Notebook — FastAPI + Jinja2 Web Application (Visual-First)

Run:  uvicorn app:app --reload --port 8000
Open: http://localhost:8000
"""

from types import SimpleNamespace
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from markupsafe import Markup

from data.career_data import META, PHASES, PRIORITY_GAPS, WAR_STORIES
from data.diagrams import DIAGRAMS, career_timeline, war_stories_diagram

app = FastAPI(title="Career Notebook")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_diagram(phase_id: str) -> str:
    fn = DIAGRAMS.get(phase_id)
    return Markup(fn()) if fn else ""


def dict_to_ns(d: dict) -> SimpleNamespace:
    """Convert a dict to SimpleNamespace so Jinja2 can cache it."""
    ns = SimpleNamespace(**d)
    return ns


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    phase = PHASES[0]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "meta": META,
            "phases": PHASES,
            "cp": phase,
            "current_phase_id": phase["id"],
            "current_index": 0,
            "diagram": get_diagram(phase["id"]),
        },
    )


@app.get("/phase/{phase_id}", response_class=HTMLResponse)
async def phase_detail(request: Request, phase_id: str):
    phase = next((p for p in PHASES if p["id"] == phase_id), None)
    if phase is None:
        phase = PHASES[0]
    index = PHASES.index(phase)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "meta": META,
            "phases": PHASES,
            "cp": phase,
            "current_phase_id": phase["id"],
            "current_index": index,
            "diagram": get_diagram(phase["id"]),
        },
    )


@app.get("/gaps", response_class=HTMLResponse)
async def gaps_summary(request: Request):
    return templates.TemplateResponse(
        "gaps.html",
        {
            "request": request,
            "meta": META,
            "phases": PHASES,
            "gaps": PRIORITY_GAPS,
            "current_phase_id": "__gaps__",
        },
    )


@app.get("/timeline", response_class=HTMLResponse)
async def timeline_view(request: Request):
    return templates.TemplateResponse(
        "timeline.html",
        {
            "request": request,
            "meta": META,
            "phases": PHASES,
            "current_phase_id": "__timeline__",
            "timeline_svg": Markup(career_timeline()),
        },
    )


@app.get("/stories", response_class=HTMLResponse)
async def stories_view(request: Request):
    return templates.TemplateResponse(
        "stories.html",
        {
            "request": request,
            "meta": META,
            "phases": PHASES,
            "stories": WAR_STORIES,
            "current_phase_id": "__stories__",
            "stories_diagram": Markup(war_stories_diagram()),
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
