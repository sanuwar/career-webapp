"""
Career Notebook — FastAPI + Jinja2 Web Application (Visual-First)

Run:  uvicorn app:app --reload --port 8000
Open: http://localhost:8000
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from markupsafe import Markup

from data.career_data import META, PHASES, PRIORITY_GAPS, WAR_STORIES
from data.diagrams import DIAGRAMS, career_timeline, story_mind_map_diagram, war_stories_diagram
from data.vocab_data import VOCAB_CATEGORIES, VOCAB_TERMS

app = FastAPI(title="Career Notebook")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_diagram(phase_id: str) -> str:
    fn = DIAGRAMS.get(phase_id)
    return Markup(fn()) if fn else ""


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "meta": META,
            "phases": PHASES,
            "current_phase": PHASES[0],
            "current_phase_id": PHASES[0]["id"],
            "current_index": 0,
            "diagram": get_diagram(PHASES[0]["id"]),
            "timeline_svg": Markup(career_timeline()),
        },
    )


@app.get("/phase/{phase_id}", response_class=HTMLResponse)
async def phase_detail(request: Request, phase_id: str):
    phase = next((p for p in PHASES if p["id"] == phase_id), None)
    if phase is None:
        phase = PHASES[0]
    index = PHASES.index(phase)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "meta": META,
            "phases": PHASES,
            "current_phase": phase,
            "current_phase_id": phase["id"],
            "current_index": index,
            "diagram": get_diagram(phase["id"]),
            "timeline_svg": Markup(career_timeline()),
        },
    )


@app.get("/gaps", response_class=HTMLResponse)
async def gaps_summary(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="gaps.html",
        context={
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
        request=request,
        name="timeline.html",
        context={
            "request": request,
            "meta": META,
            "phases": PHASES,
            "current_phase_id": "__timeline__",
            "timeline_svg": Markup(career_timeline()),
        },
    )


@app.get("/stories", response_class=HTMLResponse)
async def stories_view(request: Request):
    stories = []
    for story in WAR_STORIES:
        story_view = dict(story)
        story_view["mind_map_svg"] = Markup(story_mind_map_diagram(story))
        stories.append(story_view)

    return templates.TemplateResponse(
        request=request,
        name="stories.html",
        context={
            "request": request,
            "meta": META,
            "phases": PHASES,
            "stories": stories,
            "current_phase_id": "__stories__",
            "stories_diagram": Markup(war_stories_diagram()),
        },
    )


@app.get("/vocab", response_class=HTMLResponse)
async def vocab_view(request: Request):
    import json
    terms_by_cat = {}
    for cat in VOCAB_CATEGORIES:
        terms_by_cat[cat["id"]] = [t for t in VOCAB_TERMS if t["category"] == cat["id"]]

    cats_with_count = [
        {**cat, "count": len(terms_by_cat[cat["id"]])}
        for cat in VOCAB_CATEGORIES
    ]

    cat_label_map = {cat["id"]: cat["label"] for cat in VOCAB_CATEGORIES}
    enriched_terms = [
        {**t, "category_label": cat_label_map.get(t["category"], t["category"])}
        for t in VOCAB_TERMS
    ]

    return templates.TemplateResponse(
        request=request,
        name="vocab.html",
        context={
            "request": request,
            "meta": META,
            "phases": PHASES,
            "categories": cats_with_count,
            "terms_by_cat": terms_by_cat,
            "total": len(VOCAB_TERMS),
            "vocab_json": Markup(json.dumps(enriched_terms)),
            "current_phase_id": "__vocab__",
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
