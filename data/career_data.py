"""
CAREER DATA — Edit this file to add/modify your career content.
Each phase dict has: raw, corrections, script, details, gaps, probes, etc.
Add new phases by appending to the PHASES list.
"""

META = {
    "name": "Full-Stack AI/Data Engineer",
    "target": "Madrigal Pharmaceuticals",
    "flow": [
        "Backend Engineering",
        "Data Processing / ETL",
        "ML / AI",
        "RAG",
        "Agentic AI",
    ],
    "start_year": 2018,
}

PHASES = [
    {
        "id": "verizon",
        "title": "Verizon — Backend Engineer",
        "period": "2018–2020",
        "color": "#4ecdc4",
        "tag": "ORIGIN STORY",
        "tagline": "Where it all started — strong SQL and API fundamentals",
        "raw": (
            "I started working as a backend engineer working with Dapper and "
            "Entity Framework. My job was to write SQL queries in WebAPI "
            "through C# function calling."
        ),
        "corrections": [
            {
                "wrong": '"Write SQL queries in WebAPI through C# function calling"',
                "right": (
                    '"Built RESTful APIs using ASP.NET Web API in C#, with a '
                    'data access layer using Dapper and Entity Framework against SQL Server"'
                ),
            },
            {
                "wrong": '"C# function calling" (sounds like LLM function calling)',
                "right": (
                    '"C# service methods" or "API endpoint handlers" — the methods '
                    "in your controllers/services that execute business logic"
                ),
            },
        ],
        "script": (
            "I started my career as a backend engineer at Verizon, building "
            "RESTful APIs in C# / ASP.NET that powered internal dashboards and "
            "tooling. I worked across the full backend stack — writing API "
            "endpoints, stored procedures in SQL Server, and using both Entity "
            "Framework and Dapper for data access. That role gave me strong "
            "fundamentals in SQL, API design, and understanding how applications "
            "consume data. But working so closely with data made me realize I was "
            "more interested in what happens upstream — how data gets collected, "
            "transformed, and used for decision-making. That is what pulled me "
            "toward data engineering and eventually ML."
        ),
        "details": [
            {
                "label": "Architecture",
                "text": "Client/Frontend → Web API (C# business logic) → Data Access Layer (Dapper/EF) → SQL Server",
            },
            {
                "label": "Dapper",
                "text": "Micro-ORM — raw parameterized SQL mapped to C# objects. Used for performance-critical queries.",
            },
            {
                "label": "Entity Framework",
                "text": "Full ORM using LINQ, auto-generates SQL. Used for standard CRUD operations.",
            },
            {
                "label": "Domain",
                "text": "Internal tooling & dashboards — API consumers were other Verizon teams.",
            },
            {
                "label": "Framing",
                "text": "You were building the service layer — platform engineering for internal teams.",
            },
        ],
        "gaps": [],
        "probes": [
            {
                "q": "What database were you querying?",
                "why": "Being specific (SQL Server) shows you know your stack.",
            },
            {
                "q": "What was your day-to-day mostly?",
                "why": "Building new endpoints + writing stored procedures — shows you were creating, not maintaining.",
            },
        ],
    },
    {
        "id": "humana-pipeline",
        "title": "Humana — Greenfield Data Pipeline",
        "period": "2020+",
        "color": "#378ADD",
        "tag": "PROJECT 1 — ETL",
        "tagline": "Foundation project — built the data infrastructure everything else depends on",
        "raw": (
            "Since I joined Humana in July 2020 as a Senior Automation Engineer, "
            "I started working on a new project to establish a data processing "
            "pipeline that will feed data into system to be used for our RAG system. "
            "There was no existing process in place therefore my part of managing "
            "data processing unit has to build ground-up with a few offshore team "
            "members. I set up a standard version control system. I selected a small "
            "strike team to lead Airflow orchestration. I made sure the POC follow "
            "the structure that will later replace with production grade system which "
            "we did. The result was clean and actionable data."
        ),
        "corrections": [
            {
                "wrong": '"Pipeline to feed data into our RAG system" (RAG didn\'t exist in 2020)',
                "right": (
                    '"Pipeline to feed clean data into our Data Science models — that same '
                    "infrastructure later became the backbone for our RAG and agentic AI "
                    'systems as the technology evolved (2023+)"'
                ),
            },
        ],
        "script": (
            "When I joined Humana in July 2020, there was no existing data processing "
            "infrastructure for our Data Science team. I was tasked with building it "
            "from the ground up. I led a team of 5-10 offshore engineers, stood up "
            "version control standards, and selected a strike team to lead our Airflow "
            "orchestration layer. We built SQL-based transformation pipelines processing "
            "claims data, clinical records, internal knowledge base documents, and "
            "unstructured text. I deliberately structured our POC so it could be "
            "replaced by a production-grade system later, which we did. The result was "
            "clean, actionable data that initially fed our Data Science models, and "
            "that same infrastructure later became the data backbone for our RAG and "
            "agentic AI systems."
        ),
        "details": [
            {"label": "Role", "text": "Senior Automation Engineer → built and led the data processing unit"},
            {"label": "Team", "text": "5-10 offshore engineers, focused strike team for Airflow orchestration"},
            {"label": "Stack", "text": "Airflow + SQL transformations against SQL Server"},
            {"label": "Data types", "text": "Claims/member health, clinical/medical, internal KB, unstructured text (PDFs, emails)"},
            {"label": "Key concept", "text": "Airflow is the ORCHESTRATOR, not the executor. It schedules tasks; SQL does the work."},
            {"label": "Pipeline flow", "text": "Extract (Python) → Staging → SQL clean/validate → SQL join/enrich → SQL aggregate/load"},
        ],
        "gaps": [
            "How was unstructured text (PDFs) preprocessed before entering SQL transformations?",
            "What specific patterns made the POC production-replaceable?",
            "Concrete offshore team management details — code reviews, work structure, time zones",
        ],
        "probes": [
            {
                "q": "Why Airflow + SQL instead of Spark?",
                "why": "Tests engineering judgment. Answer: data fit SQL Server, team had SQL skills, auditable, Airflow for orchestration.",
                "has_script": True,
                "probe_script": (
                    "The data volumes fit well within SQL Server's capacity. SQL was the pragmatic choice: "
                    "team had strong SQL skills, stored procedures gave good performance, transformations "
                    "were auditable, and Airflow gave us orchestration. Over-engineering with Spark when SQL "
                    "gets the job done is a red flag, not a badge of honor."
                ),
            },
            {"q": "How did you handle unstructured text with SQL?", "why": "PDF extraction is NOT pure SQL. Clarify preprocessing."},
            {"q": "How did you manage the offshore team?", "why": "Leadership — structure, code reviews, strike team, time zones."},
            {"q": "What made the POC production-replaceable?", "why": "Your engineering design moment — articulate the patterns."},
        ],
    },
    {
        "id": "humana-patient",
        "title": "Humana — Patient Profile Clustering",
        "period": "2021–2022",
        "color": "#7F77DD",
        "tag": "PROJECT 2 — ML",
        "tagline": "Data Science / ML — directly relevant to pharma patient stratification",
        "raw": (
            "I worked in a data science model to make it better. The model was "
            "suffering from sporadic results in terms of model fit. It was to group "
            "our patient to develop a patient profile based on allergies, diagnosis, "
            "previous histories among other things. While in the model diagnosis got "
            "the more weightage to dictate dependent variable, however previous "
            "histories in terms of patient engagement was the main factor that we "
            "found after our revision. Too much data point was another factor that "
            "made the data noisy and propelled the model fit issue. I did dimension "
            "reduction, balance the weightage of IVs in our MANOVA analysis. And "
            "yes model improved."
        ),
        "corrections": [
            {"wrong": '"Weightage of IVs"', "right": '"Feature importance" or "variable weighting"'},
            {"wrong": '"Sporadic results in terms of model fit"', "right": '"Inconsistent, poorly separated clusters" — metric: Wilks\' Lambda'},
            {"wrong": '"Too much data point made data noisy"', "right": '"High dimensionality — too many features creating noise"'},
            {"wrong": "MANOVA described as the modeling method", "right": "MANOVA is VALIDATION, not clustering. Two-stage: K-means → MANOVA validates."},
        ],
        "script": (
            "I worked on improving a patient profiling model at Humana. We used "
            "K-means clustering to segment patients by clinical and behavioral "
            "attributes — allergies, diagnoses, engagement history. The model was "
            "producing inconsistent, poorly separated clusters. I diagnosed three "
            "root causes: high dimensionality creating noise, diagnosis codes "
            "dominating the feature space, and patient engagement history being "
            "suppressed despite being the key differentiator. I applied PCA keeping "
            "components explaining roughly 85-90% of variance, rebalanced feature "
            "scaling, re-ran K-means testing multiple k values, and validated with "
            "MANOVA — Wilks' Lambda improved significantly. The profiles are now "
            "used across multiple downstream pipelines."
        ),
        "details": [
            {"label": "Method", "text": "Two-stage: K-means clustering → MANOVA validation"},
            {"label": "Dimension reduction", "text": "PCA via scikit-learn — kept ~85-90% cumulative explained variance"},
            {"label": "Key finding", "text": "Patient engagement history was the real differentiator, not diagnosis codes"},
            {"label": "Validation metric", "text": "Wilks' Lambda (MANOVA) — lower = better separation. Dropped significantly after fix."},
            {"label": "Tools", "text": "Python, scikit-learn (K-means, PCA), statsmodels (MANOVA)"},
        ],
        "gaps": [
            "K-means vs Hierarchical — you said BOTH at different times. Pick one. Be consistent.",
            "Actual PCA numbers: how many features → how many components?",
            "Final k value and selection method (elbow + silhouette + MANOVA)",
            "Analytical path that revealed engagement as key: PCA loadings → effect sizes",
            "Feature scaling method and whether it was applied before PCA",
        ],
        "probes": [
            {"q": "How many components did you keep in PCA?", "why": "Actual numbers beat '85-90%.'"},
            {"q": "Why PCA instead of just dropping features?", "why": "Correlated clinical features — PCA captures shared structure."},
            {"q": "How did you discover engagement was key?", "why": "Your insight moment — walk through analytically."},
            {"q": "How did you pick k?", "why": "Elbow + silhouette + MANOVA — know the process."},
            {"q": "What is Wilks' Lambda?", "why": "0 to 1, lower = better. Know before/after numbers."},
        ],
        "connector": (
            "The clean data pipeline I built in Project 1 is what made Project 2 "
            "possible. You cannot do meaningful patient clustering if your upstream "
            "data is messy. That is why I think of myself as a full-stack "
            "practitioner — I build the pipes AND the models that consume from them."
        ),
    },
    {
        "id": "humana-warehouse",
        "title": "Humana — Warehouse Delivery Optimization",
        "period": "2022",
        "color": "#BA7517",
        "tag": "PROJECT 3 — ML",
        "tagline": "Operational ML — business impact + supply chain relevance for Madrigal",
        "raw": (
            "I worked on another project with a goal of finding reasons behind "
            "delivery delays. I used SARIMA model to understand demand prediction "
            "going into Humana's five warehouses for med dispense and K-means "
            "clustering to group warehouse distribution activities. Recommendations "
            "coming out of our ML model made demand forecast more accurate and "
            "warehouse staffing more aligned with the demand."
        ),
        "corrections": [
            {"wrong": '"Group warehouse distribution activities"', "right": '"Segmented order types by drug type, shipping zone, and carrier"'},
            {"wrong": '"Med dispense"', "right": '"Prescription medication dispensing" or "mail-order pharmacy fulfillment"'},
            {"wrong": '"Recommendations coming out of our ML model"', "right": '"SARIMA provided weekly forecasts for proactive staffing. K-means profiles informed routing during peaks."'},
        ],
        "script": (
            "Humana operates five mail-order pharmacy warehouses dispensing "
            "prescriptions to patients. We were experiencing shipping and last-mile "
            "delivery delays. I built two complementary ML models. First, SARIMA for "
            "weekly demand forecasting — prescription demand is seasonal with flu "
            "season, open enrollment, and quarterly refills. Second, K-means to "
            "segment orders by drug type, shipping zone, and carrier. The root cause "
            "was seasonal spikes overwhelming capacity. SARIMA forecasts enabled "
            "proactive staffing, and order clustering informed prioritization."
        ),
        "details": [
            {"label": "SARIMA", "text": "Weekly forecasts, s=52 (yearly seasonality). statsmodels SARIMAX / pmdarima auto_arima."},
            {"label": "K-means features", "text": "Drug type (controlled, refrigerated, standard), shipping distance/zone, carrier"},
            {"label": "Root cause", "text": "Seasonal demand spikes overwhelming warehouse capacity"},
            {"label": "Two models", "text": "SARIMA = WHEN demand spikes. K-means = WHAT TYPE of orders. Together → staffing + routing."},
            {"label": "Madrigal tie", "text": "Madrigal launched resmetirom (Rezdiffra) — building distribution now. Direct relevance."},
        ],
        "gaps": [
            "SARIMA technical details — MUST STUDY: ADF, ACF/PACF, auto_arima, MAPE, Ljung-Box",
            "Describe 2-3 concrete order cluster profiles",
            "How model outputs reached decision-makers (dashboard? report? alerts?)",
            "Quantified impact — forecast accuracy %, delay reduction %, cost savings",
        ],
        "probes": [
            {
                "q": "Why SARIMA over Prophet or XGBoost?",
                "why": "Purpose-built for trend + seasonal time series.",
                "has_script": True,
                "probe_script": (
                    "Prescription demand has strong, predictable seasonality. SARIMA is purpose-built "
                    "for time series with trend and seasonal components. Prophet is easier but gives "
                    "less control. XGBoost does not natively model temporal autocorrelation."
                ),
            },
            {"q": "What SARIMA parameters?", "why": "s=52, auto_arima, ADF, AIC, Ljung-Box."},
            {"q": "Describe the K-means clusters.", "why": "Need concrete examples, not abstractions."},
            {"q": "How did you evaluate forecast accuracy?", "why": "Time-based train/test, MAPE as metric."},
            {"q": "How were outputs consumed?", "why": "Describe the delivery mechanism to stakeholders."},
        ],
        "knowledge": {
            "title": "SARIMA Quick Reference",
            "items": [
                "SARIMA(p,d,q)(P,D,Q,s): p=AR, d=differencing, q=MA. s=52 for weekly/yearly.",
                "Step 1: ADF test for stationarity (p < 0.05 = stationary)",
                "Step 2: ACF→q, PACF→p, or auto_arima with AIC/BIC",
                "Step 3: Fit SARIMAX(data, order=(p,d,q), seasonal_order=(P,D,Q,52))",
                "Step 4: Validate — time-based split, MAPE, Ljung-Box residual test",
                "Limitation: struggles with non-linear patterns, multiple seasonalities",
            ],
        },
    },
    {
        "id": "humana-rag",
        "title": "Humana — RAG Architecture on AWS",
        "period": "2023–2024",
        "color": "#D85A30",
        "tag": "PROJECT 4 — RAG",
        "tagline": "Most modern work — directly maps to current AI engineering",
        "raw": (
            "My job was to impart confidence that our RAG system is returning only "
            "the accurate data but appropriate data. I separated tools involved for "
            "generation part and retrieval part. In retrieval part, there was embedding "
            "model. We used Amazon native Nova embedding model with large parameter. "
            "I replaced Pinecone vector store with OpenSearch to begin with and then "
            "compare it to pgvector in terms of results. I also increase the dimensions "
            "of vector and tune chunking strategy in the area of top P vs top K chunk. "
            "We used Amazon Bedrock model in the process."
        ),
        "corrections": [
            {
                "wrong": '"Top P vs top K chunk" (mixing two concepts)',
                "right": "Top-K = RETRIEVAL (how many chunks). Top-P = GENERATION (LLM sampling). Different stages. NEVER confuse.",
            },
            {"wrong": '"Large parameter"', "right": '"Higher-dimensional embeddings" — parameters ≠ dimensions'},
            {"wrong": '"Impart confidence"', "right": '"Validate" or "built a quantitative evaluation framework using RAGAS"'},
        ],
        "script": (
            "After moving to the AI Enablement platform, I led the architecture and "
            "optimization of our RAG system on AWS. The system searched Humana's "
            "internal knowledge base — policies, procedures, guidelines. I designed a "
            "decoupled architecture where retrieval and generation were independently "
            "tunable. For retrieval: Amazon Nova embeddings on Bedrock with higher-"
            "dimensional vectors. For generation: Claude on Bedrock. I migrated from "
            "Pinecone to OpenSearch, then benchmarked against pgvector — similar quality "
            "but different tradeoffs. I tuned chunking and top-K retrieval parameters. "
            "Critically, I implemented RAGAS metrics — faithfulness, answer relevance, "
            "context precision, context recall — to systematically measure quality."
        ),
        "details": [
            {"label": "Stack", "text": "Amazon Bedrock (Claude + Nova embeddings), OpenSearch / pgvector, RAGAS"},
            {"label": "Architecture", "text": "Decoupled — retrieval and generation independently tunable"},
            {"label": "Vector store eval", "text": "OpenSearch: hybrid search, scales. pgvector: simpler ops, lives in PostgreSQL."},
            {"label": "Evaluation", "text": "RAGAS: faithfulness, answer relevance, context precision, context recall"},
            {"label": "Pipeline", "text": "Ingest → Chunk → Embed → Index → Query embed → Top-K → Context assembly → LLM → Response"},
        ],
        "gaps": [
            "Embedding dimensions: what specifically did you go from/to?",
            "Chunking strategy details: method, size, overlap — WILL get probed",
            "Why you moved away from Pinecone (cost? vendor lock-in? AWS ecosystem?)",
            "OpenSearch vs pgvector — which did you RECOMMEND and why?",
            "Actual RAGAS scores before/after optimization",
            "Why Claude over other Bedrock generation models?",
        ],
        "probes": [
            {"q": "Why did you move away from Pinecone?", "why": "Important architectural decision to justify."},
            {"q": "OpenSearch vs pgvector — recommendation?", "why": "Don't just say 'tradeoffs' — make a clear call."},
            {
                "q": "How does RAGAS evaluation work?",
                "why": "Four metrics covering retrieval + generation quality.",
                "has_script": True,
                "probe_script": (
                    "RAGAS measures four metrics. Faithfulness: is the answer grounded in context? "
                    "Answer relevance: does it address the question? Context precision: are retrieved "
                    "chunks relevant? Context recall: did we retrieve all needed chunks? Together "
                    "they give a quantitative picture of both retrieval and generation quality."
                ),
            },
            {"q": "What chunking strategy and why?", "why": "Method, size, overlap — specifics matter."},
            {"q": "Why higher-dimensional embeddings?", "why": "More semantic nuance. Tradeoff: storage + latency."},
            {"q": "Accuracy vs appropriateness?", "why": "Accurate = correct. Appropriate = relevant + suitable for this user."},
        ],
        "knowledge": {
            "title": "RAG Architecture Reference",
            "items": [
                "Retrieval params: Top-K, similarity threshold, chunk size + overlap",
                "Generation params: Temperature, top-P (nucleus sampling), max tokens",
                "Hybrid search: Dense vectors (semantic) + BM25 (keyword). OpenSearch native.",
                "RAGAS: Faithfulness, Answer relevance, Context precision, Context recall",
                "Embedding dims: higher = more resolution, more cost. Range 256–1536.",
            ],
        },
    },
    {
        "id": "copilot-knowledge",
        "title": "Humana — Assistive Knowledge Co-pilot",
        "period": "2024",
        "color": "#1D9E75",
        "tag": "PROJECT 5 — AGENTIC",
        "tagline": "Domain-routed multi-agent system for instant policy-based answers",
        "raw": (
            "Assistive Knowledge Co-pilot provided us instant policy based answers. "
            "It has agents/workflows for (i) policy (ii) claim and (iii) coverage."
        ),
        "corrections": [
            {
                "wrong": '"Has agents for policy, claim and coverage" (too vague)',
                "right": (
                    '"Domain-routed multi-agent system — orchestrator classifies the question '
                    "and routes to a specialized agent, each searching its own document corpus: "
                    'policy documents, claims rules, or benefits/coverage eligibility"'
                ),
            },
        ],
        "script": (
            "The first agentic system I built was the Assistive Knowledge Co-pilot — "
            "a domain-routed multi-agent system for instant policy-based answers. "
            "Employees across clinical operations, pharmacy, and care management could "
            "ask natural language questions. The LangGraph orchestrator classifies the "
            "question and routes to one of three specialized agents: a Policy agent "
            "searching policy documents, a Claim agent handling claims rules and "
            "adjudication logic, or a Coverage agent for benefits and eligibility. "
            "Each agent searches its own focused document corpus rather than one "
            "massive RAG search over everything — this domain routing dramatically "
            "improved retrieval precision. The LLM then generates a grounded, cited "
            "answer. I built the orchestration logic, the RAG retrieval pipelines, "
            "and the guardrails layer."
        ),
        "details": [
            {"label": "Architecture", "text": "Domain-routed multi-agent — orchestrator classifies question, routes to specialized agent"},
            {"label": "Three agents", "text": "Policy agent (policy corpus), Claim agent (claims corpus), Coverage agent (benefits corpus)"},
            {"label": "Why routing", "text": "Focused retrieval scope per agent improves precision vs one giant RAG search"},
            {"label": "Framework", "text": "LangGraph for orchestration"},
            {"label": "My role", "text": "Built orchestrator logic, RAG retrieval pipelines, and guardrails layer"},
            {"label": "Users", "text": "Clinical operations, pharmacy, care management — mix of roles"},
        ],
        "gaps": [
            "How does the orchestrator classify which agent to route to? LLM-based classification? Keyword rules? Embedding similarity?",
            "What is the document corpus size for each agent? Rough numbers help.",
            "How did you measure retrieval precision improvement vs a single-corpus approach?",
        ],
        "probes": [
            {"q": "Why three separate agents instead of one RAG pipeline with metadata filtering?", "why": "Tests your architectural reasoning. Good answer: each domain has different doc structures, query patterns, and retrieval strategies."},
            {"q": "How does the orchestrator decide which agent to route to?", "why": "Intent classification is a core design decision. Be specific."},
            {"q": "How did this co-pilot evolve into the Decision Audit co-pilot?", "why": "Shows progression. Answer: same orchestration + RAG foundation, added ML inference and automated actions."},
        ],
    },
    {
        "id": "copilot-audit",
        "title": "Humana — Decision Audit Co-pilot",
        "period": "2024+",
        "color": "#a78bfa",
        "tag": "PROJECT 6 — AGENTIC",
        "tagline": "Multi-agent system with ML inference, defense-in-depth filtering, and automated actions",
        "raw": (
            "Decision Audit Co-pilot has three agents which are Risk Intelligent "
            "agent, Fraud Pattern agent and filters including regex filter, semantic "
            "filter and embedding filters. For example, regex filter blocks profanity "
            "laced wording, semantic filter blocks medical advice and embedding "
            "filters blocks 'how to make the med stronger' type prompts."
        ),
        "corrections": [
            {
                "wrong": '"Has three agents and filters" (undersells the architecture)',
                "right": (
                    '"Multi-agent system with defense-in-depth filtering. Three-tier filters '
                    "(regex, semantic, embedding) screen both inputs and outputs. Specialized "
                    "sub-agents — Risk Intelligence and Fraud Pattern — feed into RAG retrieval "
                    'and LLM synthesis for auditable recommendations with automated actions"'
                ),
            },
            {
                "wrong": '"Regex filter blocks profanity laced wording" (too casual)',
                "right": (
                    '"Regex filter uses pattern matching to catch profanity, PII/PHI exposure, '
                    'prompt injection attempts, and SQL injection patterns — fast, deterministic first line of defense"'
                ),
            },
        ],
        "script": (
            "The Decision Audit Co-pilot was a multi-agent system with defense-in-depth "
            "filtering. Before any request touches the agents, input filters screen it "
            "through three tiers: regex catches profanity, PII exposure, and injection "
            "attempts; semantic filter blocks requests for medical advice even if phrased "
            "politely; embedding filter catches subtle attempts like 'how to make medication "
            "stronger' that the first two layers would miss. "
            "Once through, the LangGraph orchestrator delegates to specialized sub-agents: "
            "a Risk Intelligence agent that pulls patient features and calls our production "
            "kNN model for risk classification with confidence scores, and a Fraud Pattern "
            "agent for anomaly detection. Their outputs feed into RAG retrieval against "
            "guidelines and playbooks, then the LLM synthesizes a structured, auditable "
            "recommendation with citations. The same three-tier filter runs on the output "
            "before returning. Low confidence or high-risk cases route to human review. "
            "Confident cases trigger automated actions — case creation, outreach drafting, "
            "queue routing based on state, network, capacity, and language constraints."
        ),
        "details": [
            {"label": "Architecture", "text": "Multi-agent with defense-in-depth input + output filtering"},
            {"label": "Input/output filters", "text": "Three tiers: regex (pattern), semantic (meaning), embedding (similarity). Run on BOTH input and output."},
            {"label": "Regex catches", "text": "Profanity, PII/PHI, prompt injection, SQL injection — fast, deterministic"},
            {"label": "Semantic catches", "text": "Medical advice requests — even politely phrased ones"},
            {"label": "Embedding catches", "text": "Subtle harmful intent like 'how to make medication stronger' — similarity-based"},
            {"label": "Risk agent", "text": "Pulls features from feature store, calls production kNN API → risk tier + confidence + neighbor summary"},
            {"label": "Fraud agent", "text": "Anomaly/fraud pattern detection (method TBD — need to clarify)"},
            {"label": "RAG layer", "text": "Uses ML outputs to query guidelines, playbooks, SOPs for interpretation and recommended actions"},
            {"label": "LLM synthesis", "text": "Structured recommendation: class + confidence + intervention + rationale with citations + next action"},
            {"label": "Automated actions", "text": "Case creation, outreach drafting, queue routing (by state, network, capacity, language)"},
            {"label": "Framework", "text": "LangGraph orchestration, kNN in production, Claude on Bedrock"},
        ],
        "gaps": [
            "Fraud Pattern Agent — WHAT is the actual detection method? Separate ML model? Rules/heuristics? Isolation forest? You said you need to think about this. MUST resolve before interview.",
            "Regex filter specifics — you said it catches multiple things (profanity, PII, prompt injection, SQL injection). Be ready with concrete regex pattern examples.",
            "Semantic filter implementation — is it a classifier? A separate LLM call? Embedding similarity against a blocklist?",
            "Embedding filter implementation — what embedding model? What is the reference set of blocked intents?",
            "How many automated actions per day/week? Any quantified throughput or accuracy numbers?",
            "Logging and observability — you described this in slides but we did not discuss YOUR implementation.",
        ],
        "probes": [
            {
                "q": "Why three filter tiers instead of just one LLM-based content moderation?",
                "why": "Tests defense-in-depth reasoning.",
                "has_script": True,
                "probe_script": (
                    "Each layer catches what the previous one misses. Regex is fast and deterministic — "
                    "it catches obvious patterns with zero latency. Semantic filter understands meaning, "
                    "so 'could you advise me on medication dosage' gets caught even without banned keywords. "
                    "Embedding filter catches novel phrasings by similarity — it does not need to have seen "
                    "the exact prompt before. Running all three on both input and output gives us defense-in-depth. "
                    "A single LLM moderator would be slower, more expensive, and a single point of failure."
                ),
            },
            {"q": "How does the Fraud Pattern Agent work?", "why": "You need to clarify the detection method. Do not be vague here."},
            {"q": "How do you decide when to route to human review vs automated action?", "why": "Confidence thresholds, risk level, data completeness — be specific about the decision logic."},
            {"q": "Single agent vs multi-agent — why multi-agent here?", "why": "Good answer: each agent has distinct tool access and reasoning scope. Inference agent talks to feature store + ML. Fraud agent has anomaly logic. Separating them makes testing, debugging, and updating independent."},
            {
                "q": "Can you do this with documents only, without the ML model?",
                "why": "Your slide 9 answer — know this cold.",
                "has_script": True,
                "probe_script": (
                    "Only if classification is rule-based triage from guidelines. For statistical "
                    "classification you need a model execution path. Documents are for interpretation, "
                    "constraints, and recommended actions — not the prediction itself. ML tells you WHAT "
                    "the patient is. RAG tells you what that MEANS and what to DO. The LLM stitches them together."
                ),
            },
        ],
        "connector": (
            "The progression from Co-pilot 1 to Co-pilot 2 mirrors the maturity of the AI "
            "itself: we went from answering questions about policy to autonomously assessing "
            "patients and taking action — with safety guardrails at every layer."
        ),
        "knowledge": {
            "title": "Agentic AI architecture reference",
            "items": [
                "LangGraph: graph-based agent orchestration — nodes are agents/tools, edges are control flow",
                "Defense-in-depth filtering: regex (fast/deterministic) → semantic (meaning) → embedding (similarity)",
                "Multi-agent patterns: orchestrator delegates to specialized sub-agents with distinct tool access",
                "Human-in-the-loop: confidence thresholds determine automated action vs human review",
                "Audit trail: log feature versions, model versions, retrieval docs, tool calls, LLM output at every step",
                "Key insight: ML = WHAT (classification). RAG = WHAT IT MEANS + WHAT TO DO. LLM = stitch together.",
            ],
        },
    },
    {
        "id": "enclara-claims",
        "title": "Enclara — Claims Intelligence Platform",
        "period": "2024+",
        "color": "#D85A30",
        "tag": "PROJECT 7 — AGENTIC",
        "tagline": "Adapted Humana stack for hospice per diem claims after corporate transition",
        "raw": (
            "I first started with risk-aware insurance recommendation and claim support "
            "application system. The objective is claim automation, risk scoring and "
            "recommendations, multi-agent workflow orchestration, RAG over internal documents."
        ),
        "corrections": [
            {"wrong": '"Risk-aware insurance recommendation and claim support application system"', "right": '"Claims Intelligence Platform" — crisp, memorable, interview-ready name'},
        ],
        "script": (
            "When Humana divested Enclara and it was acquired by Dragonfly Health, I adapted "
            "the AI stack for hospice per diem insurance claims. Same AWS/Bedrock infrastructure, "
            "completely different domain. I redesigned the system into a three-agent LangGraph "
            "workflow: an Extraction agent that parses structured and unstructured claim data, a "
            "Risk agent using XGBoost for claim risk scoring, and a Recommendation agent using RAG "
            "over hospice benefit rules, Medicare compliance docs, and similar past claims. Output: "
            "flag for review, route to specialist, or generate claim summary with citations."
        ),
        "details": [
            {"label": "Domain", "text": "Hospice per diem insurance claims — unique Medicare/Medicaid compliance requirements"},
            {"label": "Three agents", "text": "Extraction + classification → XGBoost risk scoring → RAG recommendation"},
            {"label": "ML model", "text": "XGBoost for risk scoring (different from Humana kNN)"},
            {"label": "RAG corpus", "text": "Hospice benefit rules, Medicare compliance, level-of-care docs, per diem rates, past claims"},
            {"label": "Transition", "text": "Same AWS/Bedrock stack from Humana — proves the architecture is transferable"},
            {"label": "Guardrails", "text": "Same three-tier defense-in-depth filtering (regex, semantic, embedding)"},
        ],
        "gaps": [
            "XGBoost specifics — features, number of trees, evaluation metric (AUC? F1?)",
            "Quantified impact — estimate review time reduction, accuracy improvement",
            "How Agent 1 handles unstructured adjuster notes — NLP? LLM parsing?",
            "Historical pattern matching in Agent 2 — similarity search or rule-based?",
        ],
        "probes": [
            {"q": "How much of the Humana stack carried over?", "why": "Shows transferable architecture. Answer: same AWS/Bedrock infra, same LangGraph patterns, different domain + ML model."},
            {"q": "Why XGBoost instead of kNN here?", "why": "Different problem structure. Be ready to explain the choice."},
            {"q": "What makes hospice claims different?", "why": "Benefit periods, levels of care, recertification, Medicare compliance — show domain knowledge."},
        ],
    },
    {
        "id": "enclara-dev",
        "title": "Enclara — Dev Team AI Enablement",
        "period": "2025+",
        "color": "#639922",
        "tag": "PROJECT 8 — LEADERSHIP",
        "tagline": "Team productivity transformation — from offshore-dependent to self-sufficient",
        "raw": (
            "I am now leading our software development team to help them upskill their code "
            "automation by using Codex and Claude Code. We are developing software in FastAPI "
            "and Jinja2 templating. I delineate VCS, set up Codex and Claude Code in their "
            "VS Code and streamline code commit and sync process."
        ),
        "corrections": [
            {"wrong": '"Delineate VCS"', "right": '"Established version control workflow — branching strategy, PR process, commit conventions on Azure DevOps"'},
            {"wrong": '"Set up Codex and Claude Code"', "right": '"Onboarded the team on AI-assisted development — configured Codex and Claude Code in VS Code"'},
            {"wrong": '"Streamline code commit and sync"', "right": '"Standardized Git workflow — branch protection, PR reviews, CI pipeline"'},
        ],
        "script": (
            "I am leading a team of 5-10 developers through a productivity transformation. "
            "When I started, they were coding manually with no AI tools, dependent on offshore "
            "frontend developers, with no standardized VCS workflow. I introduced Codex and "
            "Claude Code into their VS Code environments, established our Azure DevOps workflow "
            "with branching strategy and CI pipeline, and upskilled the team on AI-assisted "
            "development. Development velocity increased dramatically — the team now builds "
            "FastAPI and Jinja2 applications in-house with significantly reduced offshore dependency."
        ),
        "details": [
            {"label": "Team size", "text": "5-10 developers"},
            {"label": "AI tools", "text": "OpenAI Codex (inline completions) + Anthropic Claude Code (agentic coding from terminal)"},
            {"label": "VCS", "text": "Azure DevOps — branching, PRs, CI pipeline"},
            {"label": "Stack", "text": "FastAPI + Jinja2 templating"},
            {"label": "Impact", "text": "Reduced offshore frontend dependency, accelerated development velocity"},
        ],
        "gaps": [
            "How much faster? Estimate: 'development cycles went from X weeks to Y'",
            "Codex vs Claude Code — when do you use each specifically?",
            "What tasks did offshore devs handle that team now does in-house?",
        ],
        "probes": [
            {"q": "How do you decide between Codex and Claude Code?", "why": "Shows deliberate tool selection, not just 'we use AI.'"},
            {"q": "How did you get developer buy-in for AI tools?", "why": "Change management — resistance, training, proving value."},
            {"q": "How do you ensure AI-generated code quality?", "why": "Code review process, testing standards, guardrails around AI output."},
        ],
    },
]


# Priority gaps for the summary page
PRIORITY_GAPS = {
    "high": [
        {"gap": "Top-K vs Top-P — NEVER confuse these", "project": "RAG", "action": "Drill until automatic"},
        {"gap": "Fraud Pattern Agent — what is the actual method?", "project": "Decision Audit", "action": "Decide and commit"},
        {"gap": "Brush up on SARIMA technical details", "project": "P3 Warehouse", "action": "Use cheatsheet"},
        {"gap": "K-means vs Hierarchical — pick one, be consistent", "project": "P2 Patient", "action": "Confirm and commit"},
        {"gap": "How unstructured text (PDFs) preprocessed before SQL", "project": "P1 Pipeline", "action": "Recall or research"},
        {"gap": "Chunking strategy specifics (method, size, overlap)", "project": "RAG", "action": "Recall specifics"},
    ],
    "medium": [
        {"gap": "Semantic filter implementation (classifier? LLM call? embedding?)", "project": "Decision Audit", "action": "Clarify method"},
        {"gap": "Embedding filter reference set — what blocked intents?", "project": "Decision Audit", "action": "Recall specifics"},
        {"gap": "How orchestrator classifies question for domain routing", "project": "Knowledge Co-pilot", "action": "Clarify method"},
        {"gap": "Actual PCA numbers (features in → components out)", "project": "P2 Patient", "action": "Recall specifics"},
        {"gap": "Describe 2-3 K-means order clusters concretely", "project": "P3 Warehouse", "action": "Prepare examples"},
        {"gap": "Why you moved away from Pinecone", "project": "RAG", "action": "Articulate reasons"},
        {"gap": "OpenSearch vs pgvector — final recommendation", "project": "RAG", "action": "Make a clear call"},
        {"gap": "POC-to-production patterns you enforced", "project": "P1 Pipeline", "action": "Think through specifics"},
    ],
    "low": [
        {"gap": "Quantified impact numbers for ANY project", "project": "All", "action": "Estimate if needed"},
        {"gap": "RAGAS scores before/after optimization", "project": "RAG", "action": "Recall or estimate"},
        {"gap": "Why Claude over other Bedrock models", "project": "RAG", "action": "Prepare reasoning"},
        {"gap": "Logging/observability implementation details", "project": "Decision Audit", "action": "Recall specifics"},
    ],
}


WAR_STORIES = [
    {
        "id": "set-vs-list",
        "title": "#1 Set vs List Bug",
        "color": "#D85A30",
        "skill": "Code review, dependency management, mentorship",
        "use_when": "Tell me about a subtle bug you found",
        "script": (
            "An IC pushed code that passed all automated unit tests but broke the web app "
            "for specific inputs like zip codes and state lookups. I traced it to an import "
            "that converted processed data output from a list to a set â€” silently filtering "
            "out duplicate values that were actually valid data. Tests didn't catch it because "
            "test inputs happened to have unique values. After fixing it, I established a "
            "Confluence page where anyone importing new libraries must document the dependency "
            "and its side effects, and ran a team education session on Python data structure "
            "differences â€” lists vs sets, tuples vs dicts, JSON parsing gotchas."
        ),
    },
    {
        "id": "folium-tokens",
        "title": "#2 Folium Token Spike",
        "color": "#BA7517",
        "skill": "Cost debugging, root cause analysis, invisible dependencies",
        "use_when": "Describe a cost or performance issue you solved",
        "script": (
            "After integrating a data science model into our RAG system, LLM token consumption "
            "spiked significantly. The root cause was unexpected: the model used Folium, a Python "
            "library that renders resource-intensive 3D geographic maps. Folium was executing "
            "headlessly â€” no visible output, percolating under the surface consuming resources. "
            "Caught it in the lower environment, rolled back the integration, token consumption "
            "returned to normal."
        ),
    },
    {
        "id": "data-masking",
        "title": "#3 Data Masking with Mostly.ai",
        "color": "#7F77DD",
        "skill": "Privacy engineering, compliance, deployment strategy",
        "use_when": "How do you handle sensitive data?",
        "script": (
            "Our data science model was deliberately decoupled from the embedding model in the "
            "vector store to prevent PII from flowing into the LLM. I led the effort to implement "
            "data masking using Mostly.ai â€” preserving statistical properties for model accuracy "
            "while ensuring no sensitive information reached the LLM layer. Also had to balance "
            "this against main deliverables â€” reprioritizing and safeguarding the critical path. "
            "Bonus: I make real-time decisions on blue-green vs canary deployment depending on "
            "the risk profile of each change."
        ),
    },
    {
        "id": "schema-drift",
        "title": "#4 Schema Drift Detection",
        "color": "#378ADD",
        "skill": "MLOps maturity, observability, prevention",
        "use_when": "Tell me about a pipeline failure",
        "script": (
            "A model training job failed because an upstream team made a silent schema change. "
            "No automated checks caught it. I implemented three safeguards: Evidently AI for "
            "continuous feature drift monitoring, schema validation in the ETL layer to flag "
            "incompatible structures immediately, and automated alerting for real-time notification. "
            "Went from discovering issues after failures to detecting data problems proactively."
        ),
    },
    {
        "id": "api-timeout",
        "title": "#5 API Timeout Handling",
        "color": "#1D9E75",
        "skill": "System resilience, UX empathy, error handling",
        "use_when": "How do you improve reliability / UX?",
        "script": (
            "The web app threw a generic 'API Error' on any timeout, forced logout, and lost "
            "all workflow state. Terrible UX. I identified the timeout patterns, then worked with "
            "engineering to implement graceful error handling: frontend catches failures without "
            "forcing logout, preserves session and workflow state, retries silently or returns "
            "user to the previous step. A temporary API failure should never destroy a user's work."
        ),
    },
]


WAR_STORIES = [
    {
        "id": "set-vs-list",
        "title": "#1 Set vs List Bug",
        "color": "#D85A30",
        "skill": "Code review, dependency management, mentorship",
        "use_when": "Tell me about a subtle bug you found",
        "situation": (
            "An IC shipped code that passed unit tests but broke the web app for specific "
            "inputs such as zip codes and state lookups."
        ),
        "task": (
            "I needed to isolate the root cause quickly, restore correct behavior, and prevent "
            "the same class of bug from slipping through again."
        ),
        "action": (
            "I traced the failure to a library import that changed processed output from a list "
            "to a set, silently removing duplicate values that were actually valid. The tests "
            "missed it because the fixtures only used unique values. I fixed the import path, "
            "reviewed data structure assumptions in the affected code path, added prevention via "
            "dependency documentation, and ran a short team session on Python collection behavior."
        ),
        "result": (
            "The application behavior was restored, we closed a test coverage gap around duplicate "
            "inputs, and the team left with a clearer dependency-review standard instead of just a "
            "one-off fix."
        ),
        "script": (
            "An IC pushed code that passed unit tests but broke the web app for specific inputs "
            "like zip codes and state lookups. I traced it to a library import that changed our "
            "processed output from a list to a set, which silently removed duplicate values that "
            "were actually valid. The tests missed it because the fixtures only had unique values. "
            "I fixed the bug, closed the test gap, then put two preventive controls in place: a "
            "dependency documentation practice for new libraries and a team session on Python data "
            "structure differences and common parsing gotchas."
        ),
        "follow_ups": [
            {
                "q": "Why did the tests miss it?",
                "a": (
                    "Because the fixtures only covered unique values. The bug only showed up when "
                    "duplicate values were valid business data, so the suite was not exercising the "
                    "real edge case."
                ),
            },
            {
                "q": "How would you prevent this beyond documentation?",
                "a": (
                    "I would add targeted tests for duplicate-preservation behavior, require type and "
                    "shape checks on transformed outputs, and call out collection semantics during "
                    "code review when new libraries touch parsing or normalization."
                ),
            },
            {
                "q": "Why was this bug subtle?",
                "a": (
                    "Nothing crashed. The data still looked structurally valid, but its semantics had "
                    "changed. Those are hard bugs because they pass superficial checks and fail only "
                    "under specific business inputs."
                ),
            },
        ],
        "mind_map": [
            {"label": "Root cause", "text": "A dependency changed collection semantics from ordered duplicates-preserved data to uniqueness-enforced data."},
            {"label": "Technical decisions", "text": "Trace the transformation chain, verify the exact data type at each step, and patch the import or conversion point instead of masking the symptom downstream."},
            {"label": "Prevention", "text": "Add duplicate-preservation tests, collection-shape assertions, and dependency review notes for parsing or normalization libraries."},
            {"label": "Leadership angle", "text": "Turned a one-off defect into a team learning moment through documentation and lightweight training."},
            {"label": "Interviewer pivots", "text": "Expect questions about test strategy, code review, dependency governance, and how you mentor engineers after production-adjacent bugs."},
        ],
    },
    {
        "id": "folium-tokens",
        "title": "#2 Folium Token Spike",
        "color": "#BA7517",
        "skill": "Cost debugging, root cause analysis, invisible dependencies",
        "use_when": "Describe a cost or performance issue you solved",
        "situation": (
            "After integrating a data science model into a RAG workflow, LLM token consumption and "
            "compute usage spiked unexpectedly in a lower environment."
        ),
        "task": (
            "I needed to identify what changed, isolate the non-obvious source of the cost increase, "
            "and stop the issue before it reached production."
        ),
        "action": (
            "I compared behavior before and after the integration and traced the issue to Folium, a "
            "mapping library embedded in the model flow. It was executing headlessly, so there was no "
            "visible map output to make the problem obvious. Once confirmed, I rolled that integration "
            "back and made it latent until we could reintroduce it safely."
        ),
        "result": (
            "Token consumption returned to baseline, we avoided a production cost leak, and the team "
            "got a concrete example of why lower-environment validation matters for invisible runtime "
            "dependencies."
        ),
        "script": (
            "After integrating a data science model into our RAG workflow, token consumption spiked "
            "in a lower environment. I investigated and found the issue was Folium embedded in the "
            "model path. It was running headlessly, so there was no visible output and the resource "
            "drain was easy to miss. I rolled the integration back, made that behavior latent, and "
            "token usage returned to normal before the change ever reached production."
        ),
        "follow_ups": [
            {
                "q": "Why was the root cause non-obvious?",
                "a": (
                    "Because Folium was not surfacing as a visible UI artifact. The symptom was cost "
                    "and compute drift, not an obvious broken screen or stack trace."
                ),
            },
            {
                "q": "What signal told you to investigate?",
                "a": (
                    "The main signal was unexpected token and compute growth immediately after the "
                    "integration. A sudden step-change after a deployment is a strong indicator that "
                    "the new dependency path needs to be isolated."
                ),
            },
            {
                "q": "What process improvement came out of it?",
                "a": (
                    "I would formalize dependency reviews for model integrations, especially libraries "
                    "that can render, serialize, or expand payloads invisibly. Those are common sources "
                    "of hidden cost amplification."
                ),
            },
        ],
        "mind_map": [
            {"label": "Root cause", "text": "A hidden visualization dependency was increasing runtime work and downstream token or compute consumption without obvious visible output."},
            {"label": "Technical decisions", "text": "Compare pre- and post-integration behavior, isolate newly introduced libraries, and disable the suspicious path in the lower environment first."},
            {"label": "Metrics", "text": "Token usage, compute consumption, integration-level cost deltas, and whether rollback returns the system to baseline."},
            {"label": "Prevention", "text": "Review model-adjacent dependencies for hidden rendering, serialization, or expansion behavior before integration reaches production."},
            {"label": "Interviewer pivots", "text": "Be ready for questions on cost governance, observability, safe rollback, and how lower environments should be instrumented."},
        ],
    },
    {
        "id": "data-masking",
        "title": "#3 Data Masking with Mostly.ai",
        "color": "#7F77DD",
        "skill": "Privacy engineering, compliance, deployment strategy",
        "use_when": "How do you handle sensitive data?",
        "situation": (
            "We needed to support AI workflows without allowing sensitive data to flow into the LLM "
            "layer where it could be exposed through downstream agent or chatbot experiences."
        ),
        "task": (
            "My job was to preserve analytical value for the models while enforcing a clean boundary "
            "between sensitive source data and the AI-facing layer."
        ),
        "action": (
            "I kept the statistical model decoupled from the embedding layer and led the implementation "
            "of data masking with Mostly.ai between the data science pipeline and the AI model layer. "
            "That let us preserve statistical properties for model utility without passing raw PII into "
            "the LLM path. I also reprioritized work so privacy controls did not derail the main delivery "
            "critical path."
        ),
        "result": (
            "We improved privacy posture without stalling delivery, and we created a more defensible "
            "architecture for AI use cases where model usefulness and compliance both mattered."
        ),
        "script": (
            "We had to support AI workflows without letting sensitive data flow into the LLM layer. "
            "I led an architecture approach where the statistical model stayed decoupled from the "
            "embedding layer, then implemented masking with Mostly.ai between the data science pipeline "
            "and the AI model layer. That preserved useful statistical properties while blocking raw PII "
            "from reaching the LLM. I also reprioritized work so the privacy control landed without "
            "stalling our main deliverables."
        ),
        "follow_ups": [
            {
                "q": "Why not just redact fields before sending data to the LLM?",
                "a": (
                    "Simple redaction is often not enough because downstream joins, free text, or derived "
                    "features can still leak sensitive information. I prefer an architectural boundary that "
                    "keeps the AI-facing layer separated from raw sensitive records."
                ),
            },
            {
                "q": "What made Mostly.ai a fit here?",
                "a": (
                    "The value was preserving the statistical characteristics needed by the modeling layer "
                    "while preventing real identities from flowing through. That balanced utility with privacy."
                ),
            },
            {
                "q": "How do blue-green and canary fit into this story?",
                "a": (
                    "For privacy-sensitive changes, rollout strategy matters. I would choose blue-green when "
                    "rollback safety is the priority, and canary when I want incremental validation under lower risk."
                ),
            },
        ],
        "mind_map": [
            {"label": "Root cause", "text": "The risk was architectural, not just field-level: sensitive data could leak into AI-facing layers through joins, text, or derived features."},
            {"label": "Technical decisions", "text": "Keep the statistical model separate from the embedding layer and insert a masking boundary before any LLM-facing path."},
            {"label": "Tradeoff", "text": "Balance privacy protection against model utility by preserving statistical usefulness without retaining real identities."},
            {"label": "Leadership angle", "text": "Reprioritized work so privacy controls landed without derailing the broader delivery plan."},
            {"label": "Interviewer pivots", "text": "Expect deeper questions about compliance posture, rollout strategy, data minimization, and why masking beat simple redaction."},
        ],
    },
    {
        "id": "schema-drift",
        "title": "#4 Schema Drift Detection",
        "color": "#378ADD",
        "skill": "MLOps maturity, observability, prevention",
        "use_when": "Tell me about a pipeline failure",
        "situation": (
            "A model training job failed because an upstream team changed the schema without notice, "
            "and our pipeline had no automated controls to catch the incompatibility early."
        ),
        "task": (
            "I needed to restore reliability quickly and turn a reactive failure into a proactive "
            "data quality control pattern."
        ),
        "action": (
            "I traced the break to the schema change, then implemented three safeguards: schema "
            "validation directly in ETL, automated alerting for mismatches and anomalies, and "
            "Evidently AI monitoring to watch ongoing drift in the feature layer."
        ),
        "result": (
            "We moved from finding issues only after jobs failed to detecting problems earlier in the "
            "pipeline, which reduced debugging time and made upstream changes far less disruptive."
        ),
        "script": (
            "A training job failed because an upstream team made a silent schema change and we had no "
            "automated checks to catch it. I traced the issue, then added schema validation in ETL, "
            "real-time alerting for mismatches, and Evidently AI to monitor ongoing feature drift. "
            "That moved us from reactive debugging after failure to proactive detection earlier in the pipeline."
        ),
        "follow_ups": [
            {
                "q": "Why validate schema in ETL instead of later?",
                "a": (
                    "Because the cheapest place to fail is as close to ingestion as possible. Catching "
                    "incompatibility early prevents bad data from propagating into feature engineering and training."
                ),
            },
            {
                "q": "What is the difference between schema drift and feature drift?",
                "a": (
                    "Schema drift is structural change, such as renamed or missing columns or type changes. "
                    "Feature drift is when the statistical behavior of the data changes even if the schema looks the same."
                ),
            },
            {
                "q": "What was the long-term lesson?",
                "a": (
                    "Upstream dependency risk is an engineering problem, not just a communication problem. "
                    "Better cross-team coordination helps, but you should still engineer for silent change."
                ),
            },
        ],
        "mind_map": [
            {"label": "Root cause", "text": "An upstream team changed the structure of incoming data and the pipeline had no early guardrail to reject incompatible inputs."},
            {"label": "Technical decisions", "text": "Add schema checks at ETL entry, alert immediately on mismatches, and monitor feature behavior separately from structure."},
            {"label": "Metrics", "text": "Time to detection, failed runs avoided, debugging time reduced, and percentage of data issues caught before model training."},
            {"label": "Prevention", "text": "Engineer for silent change even when communication processes exist, because upstream contracts break in practice."},
            {"label": "Interviewer pivots", "text": "Be ready for questions on data contracts, schema versus feature drift, alert thresholds, and cross-team accountability."},
        ],
    },
    {
        "id": "api-timeout",
        "title": "#5 API Timeout Handling",
        "color": "#1D9E75",
        "skill": "System resilience, UX empathy, error handling",
        "use_when": "How do you improve reliability / UX?",
        "situation": (
            "The application handled API timeouts badly: it showed a generic error, logged users out, "
            "and wiped their in-progress workflow state."
        ),
        "task": (
            "I needed to improve resilience from the user's perspective so a transient backend failure "
            "did not destroy work or trust."
        ),
        "action": (
            "I started by identifying timeout patterns and failure modes, then worked with engineering "
            "on a graceful handling approach. The frontend would catch recoverable failures without "
            "forcing logout, preserve session and workflow state, retry where appropriate, and return "
            "the user to the previous safe step when retry was not enough."
        ),
        "result": (
            "The design goal became clear: temporary API instability should degrade gracefully rather than "
            "reset the user. That improves reliability, preserves trust, and protects workflow completion."
        ),
        "script": (
            "The application treated API timeouts as fatal: users saw a generic error, got logged out, "
            "and lost their in-progress work. I mapped the timeout patterns, then worked with engineering "
            "on graceful handling so the frontend preserves session and workflow state, retries recoverable "
            "calls, and returns users to a safe step instead of forcing a restart. My principle is that a "
            "temporary API failure should never destroy a user's work."
        ),
        "follow_ups": [
            {
                "q": "Why is forced logout the wrong failure mode?",
                "a": (
                    "Because a timeout is not the same thing as an authentication failure. Logging users out "
                    "conflates unrelated problems and amplifies a transient backend issue into full workflow loss."
                ),
            },
            {
                "q": "What would you retry automatically versus not retry?",
                "a": (
                    "I would retry idempotent reads and safe transient failures automatically, but be more careful "
                    "with writes or side-effecting actions to avoid duplicate operations."
                ),
            },
            {
                "q": "What metric would you watch after rollout?",
                "a": (
                    "I would watch timeout rate, forced logout rate, abandoned workflow rate, and recovery success "
                    "after retry. That tells you whether the UX is actually more resilient."
                ),
            },
        ],
        "mind_map": [
            {"label": "Root cause", "text": "The system treated transient transport or backend failures as fatal session failures, which destroyed user state unnecessarily."},
            {"label": "Technical decisions", "text": "Separate timeout handling from auth handling, preserve client state, retry safe calls, and route users back to a safe checkpoint."},
            {"label": "User impact", "text": "The real issue was trust erosion and workflow loss, not just error rate. Reliability must be measured from the user's perspective."},
            {"label": "Metrics", "text": "Track timeout rate, forced logout rate, abandoned workflows, successful retries, and resumed sessions."},
            {"label": "Interviewer pivots", "text": "Expect questions about idempotency, session management, retry policy, frontend-backend coordination, and UX resilience."},
        ],
    },
]
