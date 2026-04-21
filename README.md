# Career Notebook — FastAPI + Jinja2

A personal career reference and interview preparation web app.
Built with Python FastAPI and Jinja2 templates.

## Project Structure

```
career-webapp/
├── app.py                  ← FastAPI application (routes)
├── requirements.txt        ← Python dependencies
├── data/
│   ├── __init__.py
│   └── career_data.py      ← YOUR CONTENT (edit this most often)
├── templates/
│   ├── base.html            ← Layout, header, nav (shared)
│   ├── index.html           ← Phase detail page
│   └── gaps.html            ← Priority gaps summary
├── static/
│   └── css/
│       └── style.css        ← All styling
└── README.md
```

## Quick Start

```bash
# 1. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn app:app --reload --port 8000

# 4. Open browser
open http://localhost:8000
```

## How to Edit Content

All career content lives in `data/career_data.py`. Each phase is a Python dict:

```python
{
    "id": "unique-id",              # URL slug: /phase/unique-id
    "title": "Company — Role",
    "period": "2020–2022",
    "color": "#4ecdc4",             # Timeline dot color (hex)
    "tag": "PROJECT 1 — ETL",
    "tagline": "One-line summary",
    "raw": "Your original words...",
    "corrections": [
        {"wrong": "Bad phrasing", "right": "Better phrasing"}
    ],
    "script": "Polished interview pitch...",
    "details": [
        {"label": "Stack", "text": "Python, Airflow, SQL Server"}
    ],
    "gaps": ["Gap description"],
    "probes": [
        {"q": "Why this?", "why": "Tests judgment"}
    ],
    "connector": "Line tying this to the next project...",
    "knowledge": {
        "title": "Quick Reference",
        "items": ["Fact 1", "Fact 2"]
    }
}
```

Add new phases by appending to the `PHASES` list.

## Routes

| URL | Description |
|-----|-------------|
| `/` | Home — shows first phase |
| `/phase/{id}` | Specific phase detail |
| `/gaps` | Priority gaps summary |

## Navigation

- Click timeline nodes at the top
- Use ← → arrow keys
- Click Prev/Next buttons at bottom of each phase

## Deployment Options

### Render.com (free tier)
```bash
# Add to requirements.txt: gunicorn
# Create render.yaml or use dashboard
# Start command: uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Railway / Fly.io / AWS
Standard Python deployment — the app reads from files, no database needed.

## Extending

- **Add authentication**: Use FastAPI middleware for basic auth
- **Add a database**: Replace `career_data.py` with SQLAlchemy models
- **Add editing UI**: Create POST routes to update career_data
- **Add export**: Create a `/export` route that generates PDF/DOCX
- **Add dark/light toggle**: CSS variables are already set up for theming
