"""
Interview Vocabulary — 7 categories, flashcard-ready.
Each entry: term, definition, example (interview sentence), category id.
"""

VOCAB_CATEGORIES = [
    {
        "id": "rca",
        "label": "Problem Identification & RCA",
        "color": "#4a90d9",
        "icon": "🧩",
        "description": "Diagnosing issues, tracing failures, quantifying impact",
    },
    {
        "id": "risk",
        "label": "Risk, Reliability & Mitigation",
        "color": "#e86100",
        "icon": "⚙️",
        "description": "Balancing innovation with control and resilience",
    },
    {
        "id": "design",
        "label": "Solution Design & Experimentation",
        "color": "#7c5cdb",
        "icon": "🧠",
        "description": "Prototyping safely, validating fast, iterating wisely",
    },
    {
        "id": "arch",
        "label": "Architecture & Scalability",
        "color": "#1e8b61",
        "icon": "🏗️",
        "description": "Platform-level reasoning, modular and fault-tolerant systems",
    },
    {
        "id": "resources",
        "label": "Resource Allocation & Prioritization",
        "color": "#c0392b",
        "icon": "🧩",
        "description": "Team management, capacity, competing deadlines",
    },
    {
        "id": "alignment",
        "label": "Team Alignment & Communication",
        "color": "#2980b9",
        "icon": "🤝",
        "description": "Leadership, collaboration, stakeholder communication",
    },
    {
        "id": "governance",
        "label": "Governance, Security & Compliance",
        "color": "#8e44ad",
        "icon": "🔐",
        "description": "Regulatory decisions, auditability, enterprise-grade controls",
    },
]

VOCAB_TERMS = [
    # ── 1. Problem Identification & Root Cause Analysis ──────────────────
    {
        "term": "Root cause analysis",
        "definition": "A structured method of tracing a problem back to its fundamental origin rather than just treating the symptom.",
        "example": "Before escalating the incident, I ran a root cause analysis to determine whether the failure stemmed from the model layer or the upstream data pipeline.",
        "category": "rca",
    },
    {
        "term": "Cross-team triage",
        "definition": "A collaborative process where multiple teams examine an issue together to determine ownership and priority.",
        "example": "We ran a cross-team triage across infra, ML, and product to identify who owned the latency regression before the on-call rotation changed.",
        "category": "rca",
    },
    {
        "term": "Isolate the latency root cause",
        "definition": "Narrow down which component in a system's call chain is responsible for a slowdown.",
        "example": "I instrumented each service boundary so we could isolate the latency root cause to the third-party enrichment API, not our own inference stack.",
        "category": "rca",
    },
    {
        "term": "Network configuration / data locality / service throttling",
        "definition": "Three common categories of infrastructure root causes: misconfigured routing, data stored far from compute, or rate-limited upstream services.",
        "example": "After ruling out code regressions, I narrowed the candidates to network configuration, data locality, and service throttling — and it turned out to be throttling on the feature store.",
        "category": "rca",
    },
    {
        "term": "Identify bottlenecks",
        "definition": "Find the constraint in a system that limits overall throughput or speed.",
        "example": "I used profiling tools to identify bottlenecks in the preprocessing step, which was blocking GPU utilization at under 40%.",
        "category": "rca",
    },
    {
        "term": "Observable data or benchmark",
        "definition": "Measurable signals (logs, metrics, traces) or baseline performance numbers used as evidence in a diagnosis.",
        "example": "Rather than guessing, I grounded my diagnosis in observable data — p95 latency traces and a benchmark against last quarter's release.",
        "category": "rca",
    },
    {
        "term": "Risk review to quantify potential impact",
        "definition": "A structured assessment that estimates the severity and scope of a problem before committing to a fix.",
        "example": "Before proposing a solution, I did a risk review to quantify potential impact — the failure affected roughly 12% of daily active users and had a $40K/hour cost implication.",
        "category": "rca",
    },
    {
        "term": "Feasibility of mitigation steps",
        "definition": "An evaluation of whether proposed solutions are practical given team capacity, timeline, and technical constraints.",
        "example": "We assessed the feasibility of mitigation steps before committing to a full re-architecture — the team agreed a configuration change would cover 80% of the risk with 10% of the effort.",
        "category": "rca",
    },

    # ── 2. Risk, Reliability & Mitigation ───────────────────────────────
    {
        "term": "Risk mitigation plan",
        "definition": "A documented set of actions designed to reduce the likelihood or impact of a known risk.",
        "example": "I put together a risk mitigation plan with rollback triggers and circuit breakers before we pushed the new ranking model to production.",
        "category": "risk",
    },
    {
        "term": "Rapid validation path",
        "definition": "A short, focused experiment or test designed to confirm or refute a hypothesis before full investment.",
        "example": "Rather than a six-week build, I proposed a rapid validation path — a two-day spike with synthetic data — to check whether the approach was even viable.",
        "category": "risk",
    },
    {
        "term": "Balance velocity with reliability",
        "definition": "The principle of shipping fast without compromising system stability or user trust.",
        "example": "The team was under pressure to ship quickly, but I pushed for feature flags so we could balance velocity with reliability and roll back safely.",
        "category": "risk",
    },
    {
        "term": "Reliability metrics",
        "definition": "Measurements that track system stability, such as uptime, error rate, mean time to recovery (MTTR), and SLA adherence.",
        "example": "We established reliability metrics — uptime, p99 latency, and error budget — so any future change could be evaluated against a clear baseline.",
        "category": "risk",
    },
    {
        "term": "Impact metrics",
        "definition": "Quantitative signals that show the business or user effect of a change, such as revenue, conversion, or engagement.",
        "example": "I tied each engineering decision to impact metrics so leadership could see the direct connection between our infrastructure investment and user retention.",
        "category": "risk",
    },
    {
        "term": "Temporary workaround",
        "definition": "A short-term fix applied to contain a problem while a permanent solution is developed.",
        "example": "We shipped a temporary workaround — capping request concurrency — to stop the bleeding while the underlying race condition was addressed.",
        "category": "risk",
    },
    {
        "term": "Safeguard critical path",
        "definition": "Protect the sequence of steps most essential to delivering a product or feature from disruption.",
        "example": "I restructured the sprint to safeguard the critical path — the model training pipeline — while experimental features were developed in parallel branches.",
        "category": "risk",
    },
    {
        "term": "Balance innovation velocity with platform reliability",
        "definition": "Ensure that the pace of new feature development does not degrade the underlying platform's stability.",
        "example": "My approach was to balance innovation velocity with platform reliability by requiring any new model integration to pass a chaos test before merging.",
        "category": "risk",
    },
    {
        "term": "Aware of reward vs. trade-offs",
        "definition": "Understanding that every technical decision carries both potential gains and hidden costs.",
        "example": "I was transparent with stakeholders that I was aware of the reward vs. trade-offs — faster iteration speed in exchange for a short-term increase in tech debt.",
        "category": "risk",
    },

    # ── 3. Solution Design & Experimentation ────────────────────────────
    {
        "term": "Shadow deployment",
        "definition": "Running a new system in parallel with the live system, receiving the same traffic but not serving responses to users, to compare behavior safely.",
        "example": "We used a shadow deployment to route 100% of production traffic to the new ranking model without any user-facing risk before a full cutover.",
        "category": "design",
    },
    {
        "term": "A/B testing in a controlled environment",
        "definition": "Randomly splitting users into groups to measure the effect of one variable, conducted under conditions that limit confounding factors.",
        "example": "I designed an A/B test in a controlled environment — matching cohorts by region and device type — to isolate the effect of the new recommendation algorithm.",
        "category": "design",
    },
    {
        "term": "Synthetic or cached data",
        "definition": "Artificially generated or pre-recorded data used in place of live production data to safely test systems.",
        "example": "Because production PII couldn't leave the secure boundary, we ran the initial validation on synthetic data that matched the schema and statistical distribution of real records.",
        "category": "design",
    },
    {
        "term": "Sandbox or segregated environment",
        "definition": "An isolated deployment context where experiments run without risk to production systems or data.",
        "example": "I spun up a sandbox environment with representative traffic replays so engineers could stress-test the new pipeline without any production blast radius.",
        "category": "design",
    },
    {
        "term": "Canary release strategy",
        "definition": "Gradually rolling out a change to a small percentage of users before a full deployment to detect issues early.",
        "example": "We used a canary release strategy — 1% of users first, then 10%, then 100% — with automated rollback triggers tied to our error budget.",
        "category": "design",
    },
    {
        "term": "Proof-of-concept validation",
        "definition": "A minimal, time-boxed implementation used to test whether an idea is technically feasible before committing resources.",
        "example": "Rather than building the full pipeline, I scoped a proof-of-concept validation over two sprints to confirm that the retrieval-augmented approach could hit our latency target.",
        "category": "design",
    },
    {
        "term": "Rapid feedback loop",
        "definition": "A process designed to return information about results quickly so teams can course-correct without significant delay.",
        "example": "I restructured our evaluation pipeline to shorten the feedback loop from two weeks to 48 hours, enabling faster iteration on model quality.",
        "category": "design",
    },
    {
        "term": "Continuous monitoring and evaluation",
        "definition": "Ongoing automated tracking of system performance and model quality metrics to detect degradation in real time.",
        "example": "We put continuous monitoring and evaluation in place — dashboards, alerting on drift, and weekly model performance reviews — so regressions were caught before users noticed.",
        "category": "design",
    },

    # ── 4. Architecture & Scalability ────────────────────────────────────
    {
        "term": "Scalable pipelines",
        "definition": "Data or ML workflows designed to handle growing volume and complexity without requiring proportional increases in engineering effort.",
        "example": "I re-architected the feature engineering step into scalable pipelines that could absorb a 10× data growth without manual intervention.",
        "category": "arch",
    },
    {
        "term": "Decouple architecture layers",
        "definition": "Separate distinct concerns (data ingestion, processing, serving) so each can evolve, scale, or fail independently.",
        "example": "The first thing I did was decouple the architecture layers — separating the training pipeline from the serving API — so we could update models without touching the inference layer.",
        "category": "arch",
    },
    {
        "term": "Abstraction layer for portability",
        "definition": "An interface that hides implementation details, allowing the underlying technology to be swapped without changing downstream consumers.",
        "example": "I introduced an abstraction layer for portability over our vector store, so the team could migrate from Pinecone to a self-hosted solution without changing a single line of application code.",
        "category": "arch",
    },
    {
        "term": "Assess current dependencies, assess portability, and build an abstraction layer",
        "definition": "A three-step approach to future-proofing a system: catalog what it relies on, evaluate lock-in risk, then isolate those dependencies behind interfaces.",
        "example": "Before recommending a vendor, I walked the team through assessing current dependencies, evaluating portability risk, and then designing an abstraction layer to protect us regardless of which vendor we chose.",
        "category": "arch",
    },
    {
        "term": "Ensure continuity and stability",
        "definition": "Design systems so that changes or failures in one component do not cascade into broader outages or data loss.",
        "example": "I added idempotent retry logic and dead-letter queues to ensure continuity and stability in the event of transient upstream failures.",
        "category": "arch",
    },
    {
        "term": "Modular and fault-tolerant design",
        "definition": "A system architecture where components are independent and the failure of any single part does not bring down the whole system.",
        "example": "The platform was built with a modular and fault-tolerant design — each enrichment service was independently deployable and could be bypassed without blocking the core inference path.",
        "category": "arch",
    },
    {
        "term": "Resilient and reproducible workflows",
        "definition": "Processes that recover automatically from failure and can be re-run to produce the same output consistently.",
        "example": "We moved to resilient and reproducible workflows by containerizing every step of the training pipeline and storing all artifacts in versioned object storage.",
        "category": "arch",
    },
    {
        "term": "GANs, VAE, Transformer models",
        "definition": "Three generative deep learning architectures: GANs (adversarial image/data synthesis), VAEs (probabilistic latent-space generation), Transformers (attention-based sequence models underlying LLMs).",
        "example": "We evaluated GANs, VAEs, and Transformer-based approaches for the data augmentation task, ultimately choosing a fine-tuned Transformer because it offered the best fidelity with our limited labeled dataset.",
        "category": "arch",
    },

    # ── 5. Resource Allocation & Prioritization ──────────────────────────
    {
        "term": "Assess current bandwidth",
        "definition": "Evaluate how much capacity a team actually has available, accounting for existing commitments and ongoing incidents.",
        "example": "Before accepting the new project, I assessed current bandwidth across the team and found we had roughly 40% capacity available after accounting for on-call and tech-debt obligations.",
        "category": "resources",
    },
    {
        "term": "Quantify true capacity gap",
        "definition": "Measure the difference between what a team can deliver and what is being asked of them, with evidence.",
        "example": "I built a resource model to quantify the true capacity gap — we needed two additional senior engineers for six months to deliver on time without sacrificing reliability.",
        "category": "resources",
    },
    {
        "term": "Reprioritize, allocate, and safeguard critical path",
        "definition": "A three-step management response: update priorities, direct resources accordingly, and protect the work that cannot be delayed.",
        "example": "Facing a scope increase mid-quarter, I reprioritized the backlog, reallocated two engineers from exploratory work, and safeguarded the critical path to ensure the compliance deadline was met.",
        "category": "resources",
    },
    {
        "term": "Smaller strike team for parallel progress",
        "definition": "A focused sub-team assigned to advance a specific initiative concurrently with the main team's work.",
        "example": "I pulled together a smaller strike team of three to tackle the API migration in parallel so the main team could stay focused on the Q3 product launch.",
        "category": "resources",
    },
    {
        "term": "Progress without stalling main deliverables",
        "definition": "The ability to advance new or exploratory work without delaying committed, high-priority outputs.",
        "example": "By time-boxing the research spike to two days per sprint, I ensured we made progress on the new architecture without stalling main deliverables.",
        "category": "resources",
    },
    {
        "term": "Managing reliability trade-offs",
        "definition": "Consciously choosing where to accept reduced stability in exchange for speed, cost savings, or new capability.",
        "example": "I facilitated a team discussion on managing reliability trade-offs — we agreed to tolerate a higher error rate on the experimental endpoint to ship faster, while keeping the core API at five nines.",
        "category": "resources",
    },
    {
        "term": "Competing deadlines and cross-project alignment",
        "definition": "The challenge of synchronizing delivery timelines across multiple initiatives that share people or dependencies.",
        "example": "I ran a monthly cross-project alignment session to surface competing deadlines early enough to negotiate trade-offs before they became emergencies.",
        "category": "resources",
    },

    # ── 6. Team Alignment & Communication ───────────────────────────────
    {
        "term": "Aligning teams around shared priorities",
        "definition": "Building consensus across different groups so everyone understands and commits to the same top-level goals.",
        "example": "I facilitated a quarterly goal-setting workshop specifically to align teams around shared priorities before individual roadmaps were locked in.",
        "category": "alignment",
    },
    {
        "term": "Data-driven communication with stakeholders",
        "definition": "Presenting updates, risks, or recommendations to non-technical decision-makers using metrics and evidence rather than anecdote.",
        "example": "I replaced our narrative-only status updates with data-driven communication — dashboards with KPIs — so stakeholders could see progress and risk without waiting for a meeting.",
        "category": "alignment",
    },
    {
        "term": "Transparent updates on impact metrics",
        "definition": "Sharing honest, timely information about how a project is performing against its stated goals.",
        "example": "Even when results were mixed, I sent transparent updates on impact metrics weekly, which built more trust with leadership than if I had waited for a clean story.",
        "category": "alignment",
    },
    {
        "term": "Proactive risk communication",
        "definition": "Surfacing potential problems to stakeholders before they materialize, giving time to adjust plans.",
        "example": "When I saw the data pipeline falling behind schedule, I practiced proactive risk communication — I flagged it two sprints early rather than waiting for the milestone miss.",
        "category": "alignment",
    },
    {
        "term": "Normalizing feedback and maintaining a supportive culture",
        "definition": "Creating an environment where giving and receiving constructive feedback is routine and psychologically safe.",
        "example": "I introduced structured retros and peer-review practices focused on normalizing feedback, which measurably reduced the discomfort around code review and cross-team critiques.",
        "category": "alignment",
    },
    {
        "term": "Collaborative cross-functional discussions",
        "definition": "Conversations that bring together people from different disciplines — engineering, product, data science, legal — to solve a problem jointly.",
        "example": "The decision on data retention policy required collaborative cross-functional discussions with legal, privacy, and engineering rather than a unilateral technical call.",
        "category": "alignment",
    },
    {
        "term": "Driving consensus through clarity and shared goals",
        "definition": "Using clear communication of objectives to move a group from disagreement to alignment.",
        "example": "When the team was split on the architecture decision, I drove consensus through clarity — I reframed the debate around our shared goal of sub-200ms latency and the options converged quickly.",
        "category": "alignment",
    },

    # ── 7. Governance, Security & Compliance ────────────────────────────
    {
        "term": "Data anonymization procedure",
        "definition": "A defined process for removing or obfuscating personally identifiable information before data is used in analytics, training, or sharing.",
        "example": "Before ingesting user behavioral data into the training pipeline, I implemented a data anonymization procedure that stripped all PII and replaced user IDs with rotating pseudonyms.",
        "category": "governance",
    },
    {
        "term": "Compliance and security vetting",
        "definition": "A formal review process to ensure a system, vendor, or process meets regulatory and internal security requirements.",
        "example": "Every third-party model vendor went through our compliance and security vetting process — SOC 2 audit, data residency review, and penetration test summary — before any contract was signed.",
        "category": "governance",
    },
    {
        "term": "Governance checkpoints",
        "definition": "Scheduled review gates in a project lifecycle where compliance, legal, or security stakeholders must approve before work continues.",
        "example": "We built governance checkpoints into the ML release process — a privacy review at design phase and a security sign-off before production deployment.",
        "category": "governance",
    },
    {
        "term": "Auditability and traceability",
        "definition": "The ability to reconstruct exactly what happened in a system — who did what, when, and why — for review or investigation.",
        "example": "I designed the feature pipeline with auditability and traceability in mind: every transformation was logged with a timestamp, operator identity, and input/output snapshot.",
        "category": "governance",
    },
    {
        "term": "Policy-driven approvals",
        "definition": "A system where decisions are gated by predefined rules or policies rather than ad-hoc human judgment, reducing inconsistency.",
        "example": "I replaced the informal 'ask your manager' approval process with policy-driven approvals in our IAM system, so access to production data was governed by role rather than relationship.",
        "category": "governance",
    },
]
