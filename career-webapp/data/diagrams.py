"""
SVG DIAGRAMS — Visual-first content for each career phase.
Each function returns an SVG string for embedding in templates.
"""


def verizon_architecture():
    return '''<svg width="100%" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.blue{fill:#378ADD20;stroke:#378ADD}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.gray{fill:#88878020;stroke:#888780}
.ht{fill:#4ecdc4}.hb{fill:#378ADD}.hp{fill:#7F77DD}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Three-layer architecture you built</text>
<rect class="b teal" x="40" y="45" width="140" height="55"/>
<text class="h ht" x="110" y="68" text-anchor="middle">Frontend</text>
<text class="s" x="110" y="84" text-anchor="middle">Internal dashboards</text>
<line class="arr" x1="180" y1="72" x2="218" y2="72"/>
<rect class="b blue" x="220" y="45" width="240" height="55"/>
<text class="h hb" x="340" y="68" text-anchor="middle">Your Web API (C#)</text>
<text class="s" x="340" y="84" text-anchor="middle">Business logic + routing</text>
<line class="arr" x1="460" y1="72" x2="498" y2="72"/>
<rect class="b purple" x="500" y="45" width="140" height="55"/>
<text class="h hp" x="570" y="68" text-anchor="middle">SQL Server</text>
<text class="s" x="570" y="84" text-anchor="middle">Data store</text>
<line x1="280" y1="100" x2="280" y2="130" class="arr"/>
<line x1="400" y1="100" x2="400" y2="130" class="arr"/>
<rect class="b teal" x="180" y="135" width="140" height="50" rx="6"/>
<text class="h ht" x="250" y="155" text-anchor="middle">Dapper</text>
<text class="s" x="250" y="170" text-anchor="middle">Raw SQL, performance</text>
<rect class="b purple" x="360" y="135" width="140" height="50" rx="6"/>
<text class="h hp" x="430" y="155" text-anchor="middle">Entity Framework</text>
<text class="s" x="430" y="170" text-anchor="middle">LINQ, CRUD ops</text>
<rect x="40" y="210" width="600" height="36" rx="8" fill="#4ecdc408" stroke="#4ecdc440" stroke-width="0.5" stroke-dasharray="4 3"/>
<text class="s" x="340" y="232" text-anchor="middle">You built the service layer — platform engineering for internal Verizon teams</text>
</svg>'''


def pipeline_flow():
    return '''<svg width="100%" viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.blue{fill:#378ADD20;stroke:#378ADD}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.coral{fill:#D85A3020;stroke:#D85A30}
.amber{fill:#BA751720;stroke:#BA7517}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Airflow + SQL pipeline you built from scratch</text>
<rect class="b teal" x="40" y="45" width="130" height="50"/>
<text class="h" x="105" y="65" text-anchor="middle" fill="#4ecdc4">Data sources</text>
<text class="s" x="105" y="80" text-anchor="middle">PDFs, claims, EHR</text>
<line class="arr" x1="170" y1="70" x2="198" y2="70"/>
<rect class="b blue" x="200" y="45" width="130" height="50"/>
<text class="h" x="265" y="65" text-anchor="middle" fill="#378ADD">Extract</text>
<text class="s" x="265" y="80" text-anchor="middle">Python operator</text>
<line class="arr" x1="330" y1="70" x2="358" y2="70"/>
<rect class="b" x="360" y="45" width="130" height="50"/>
<text class="h" x="425" y="65" text-anchor="middle">Staging</text>
<text class="s" x="425" y="80" text-anchor="middle">SQL Server</text>
<line x1="425" y1="95" x2="425" y2="125" class="arr"/>
<rect class="b purple" x="100" y="130" width="500" height="75" rx="12" stroke-dasharray="4 3"/>
<text class="h" x="350" y="150" text-anchor="middle" fill="#7F77DD">Airflow DAG — SQL transformation tasks</text>
<rect class="b purple" x="120" y="160" width="130" height="36" rx="6"/>
<text class="s" x="185" y="182" text-anchor="middle">Clean + validate</text>
<line class="arr" x1="250" y1="178" x2="268" y2="178"/>
<rect class="b purple" x="270" y="160" width="130" height="36" rx="6"/>
<text class="s" x="335" y="182" text-anchor="middle">Join + enrich</text>
<line class="arr" x1="400" y1="178" x2="418" y2="178"/>
<rect class="b purple" x="420" y="160" width="150" height="36" rx="6"/>
<text class="s" x="495" y="182" text-anchor="middle">Aggregate + load</text>
<line x1="350" y1="205" x2="350" y2="235" class="arr"/>
<rect class="b coral" x="220" y="240" width="260" height="44"/>
<text class="h" x="350" y="257" text-anchor="middle" fill="#D85A30">Clean analytical tables</text>
<text class="s" x="350" y="272" text-anchor="middle">Fed DS models → later RAG + Agentic AI</text>
<text class="s" x="110" y="308" text-anchor="middle" fill="#BA7517">2020 — Data Science</text>
<text class="s" x="500" y="308" text-anchor="middle" fill="#7F77DD">2023+ — RAG & Agentic</text>
<line x1="180" y1="303" x2="430" y2="303" stroke="#88878040" stroke-width="0.5" stroke-dasharray="3 3"/>
</svg>'''


def patient_clustering():
    return '''<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.coral{fill:#D85A3020;stroke:#D85A30}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.amber{fill:#BA751720;stroke:#BA7517}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Two-stage approach: cluster then validate</text>
<rect class="b coral" x="40" y="45" width="180" height="50"/>
<text class="h" x="130" y="65" text-anchor="middle" fill="#D85A30">Raw patient features</text>
<text class="s" x="130" y="80" text-anchor="middle">High-dim, noisy, diagnosis-heavy</text>
<line class="arr" x1="220" y1="70" x2="258" y2="70"/>
<rect class="b purple" x="260" y="45" width="160" height="50"/>
<text class="h" x="340" y="65" text-anchor="middle" fill="#7F77DD">PCA</text>
<text class="s" x="340" y="80" text-anchor="middle">~85-90% variance kept</text>
<line class="arr" x1="420" y1="70" x2="458" y2="70"/>
<rect class="b teal" x="460" y="45" width="180" height="50"/>
<text class="h" x="550" y="65" text-anchor="middle" fill="#4ecdc4">Clean feature space</text>
<text class="s" x="550" y="80" text-anchor="middle">Engagement surfaced</text>
<line x1="550" y1="95" x2="550" y2="125" class="arr"/>
<rect class="b teal" x="420" y="130" width="260" height="50"/>
<text class="h" x="550" y="150" text-anchor="middle" fill="#4ecdc4">K-means clustering</text>
<text class="s" x="550" y="165" text-anchor="middle">Tested multiple k values</text>
<line x1="550" y1="180" x2="550" y2="210" class="arr"/>
<rect class="b amber" x="420" y="215" width="260" height="50"/>
<text class="h" x="550" y="235" text-anchor="middle" fill="#BA7517">MANOVA validation</text>
<text class="s" x="550" y="250" text-anchor="middle">Wilks' Lambda improved</text>
<rect x="40" y="130" width="340" height="135" rx="10" fill="none" stroke="#D85A3040" stroke-width="0.5" stroke-dasharray="4 3"/>
<text class="h" x="210" y="155" text-anchor="middle" fill="#D85A30" font-size="12">Key insight</text>
<text class="s" x="210" y="175" text-anchor="middle">Diagnosis was dominating → suppressing</text>
<text class="s" x="210" y="192" text-anchor="middle">patient engagement, which was the</text>
<text class="s" x="210" y="209" text-anchor="middle">actual differentiator. PCA + scaling fixed it.</text>
<text class="s" x="210" y="240" text-anchor="middle" fill="#4ecdc4">Profiles now used across</text>
<text class="s" x="210" y="256" text-anchor="middle" fill="#4ecdc4">multiple downstream pipelines</text>
</svg>'''


def warehouse_optimization():
    return '''<svg width="100%" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.amber{fill:#BA751720;stroke:#BA7517}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.green{fill:#63992220;stroke:#639922}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Two complementary models</text>
<rect class="b amber" x="40" y="48" width="290" height="80" rx="10"/>
<text class="h" x="185" y="70" text-anchor="middle" fill="#BA7517">SARIMA — demand forecasting</text>
<text class="s" x="185" y="88" text-anchor="middle">Weekly forecasts, s=52</text>
<text class="s" x="185" y="104" text-anchor="middle">Flu + enrollment + refill cycles</text>
<text class="s" x="185" y="120" text-anchor="middle">Answers: WHEN will demand spike?</text>
<rect class="b teal" x="350" y="48" width="290" height="80" rx="10"/>
<text class="h" x="495" y="70" text-anchor="middle" fill="#4ecdc4">K-means — order segmentation</text>
<text class="s" x="495" y="88" text-anchor="middle">Drug type, shipping zone, carrier</text>
<text class="s" x="495" y="104" text-anchor="middle">Multi-drug rural vs single urban</text>
<text class="s" x="495" y="120" text-anchor="middle">Answers: WHAT TYPE of orders?</text>
<line x1="185" y1="128" x2="260" y2="160" class="arr"/>
<line x1="495" y1="128" x2="420" y2="160" class="arr"/>
<rect class="b green" x="200" y="165" width="280" height="50"/>
<text class="h" x="340" y="185" text-anchor="middle" fill="#639922">Proactive staffing + routing</text>
<text class="s" x="340" y="200" text-anchor="middle">20% bottleneck reduction, 18% fewer delays</text>
<rect x="40" y="232" width="600" height="22" rx="6" fill="#BA751708" stroke="#BA751730" stroke-width="0.5" stroke-dasharray="4 3"/>
<text class="s" x="340" y="247" text-anchor="middle" fill="#BA7517">Madrigal relevance: resmetirom distribution — same supply chain challenge</text>
</svg>'''


def rag_architecture():
    return '''<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.coral{fill:#D85A3020;stroke:#D85A30}
.blue{fill:#378ADD20;stroke:#378ADD}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.purple{fill:#7F77DD20;stroke:#7F77DD}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Decoupled RAG — retrieval + generation independently tunable</text>
<text class="s" x="340" y="40" text-anchor="middle">You tuned retrieval (top-K, chunking). NOT top-P — that is generation.</text>
<rect class="b" x="230" y="55" width="220" height="40"/>
<text class="h" x="340" y="79" text-anchor="middle">Query</text>
<line x1="340" y1="95" x2="340" y2="115" class="arr"/>
<rect class="b coral" x="160" y="120" width="160" height="50"/>
<text class="h" x="240" y="140" text-anchor="middle" fill="#D85A30">Nova embeddings</text>
<text class="s" x="240" y="155" text-anchor="middle">Higher-dim vectors</text>
<line class="arr" x1="320" y1="145" x2="358" y2="145"/>
<rect class="b blue" x="360" y="120" width="170" height="50"/>
<text class="h" x="445" y="140" text-anchor="middle" fill="#378ADD">Vector store</text>
<text class="s" x="445" y="155" text-anchor="middle">OpenSearch vs pgvector</text>
<line x1="340" y1="170" x2="340" y2="195" class="arr"/>
<rect class="b teal" x="200" y="200" width="280" height="50"/>
<text class="h" x="340" y="220" text-anchor="middle" fill="#4ecdc4">Claude on Bedrock</text>
<text class="s" x="340" y="235" text-anchor="middle">Generates grounded answer</text>
<line x1="340" y1="250" x2="340" y2="270" class="arr"/>
<rect class="b purple" x="200" y="275" width="280" height="22" rx="6"/>
<text class="s" x="340" y="290" text-anchor="middle" fill="#7F77DD">RAGAS: faithfulness, relevance, precision, recall</text>
<rect class="b coral" x="560" y="120" width="90" height="50" rx="6"/>
<text class="s" x="605" y="140" text-anchor="middle" fill="#D85A30">Pinecone</text>
<text class="s" x="605" y="155" text-anchor="middle">migrated</text>
<line x1="560" y1="145" x2="532" y2="145" stroke="#D85A30" stroke-width="0.8" stroke-dasharray="3 3"/>
<text class="s" x="546" y="138" fill="#D85A30">×</text>
</svg>'''


def knowledge_copilot():
    return '''<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.blue{fill:#378ADD20;stroke:#378ADD}
.green{fill:#63992220;stroke:#639922}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Domain-routed multi-agent — each agent owns a corpus</text>
<rect class="b" x="230" y="42" width="220" height="40"/>
<text class="h" x="340" y="66" text-anchor="middle">Employee question</text>
<line x1="340" y1="82" x2="340" y2="105" class="arr"/>
<rect class="b purple" x="180" y="110" width="320" height="40"/>
<text class="h" x="340" y="134" text-anchor="middle" fill="#7F77DD">Orchestrator classifies + routes</text>
<line x1="220" y1="150" x2="130" y2="178" class="arr"/>
<line x1="340" y1="150" x2="340" y2="178" class="arr"/>
<line x1="460" y1="150" x2="550" y2="178" class="arr"/>
<rect class="b teal" x="40" y="182" width="180" height="50"/>
<text class="h" x="130" y="202" text-anchor="middle" fill="#4ecdc4">Policy agent</text>
<text class="s" x="130" y="217" text-anchor="middle">Policy corpus</text>
<rect class="b teal" x="250" y="182" width="180" height="50"/>
<text class="h" x="340" y="202" text-anchor="middle" fill="#4ecdc4">Claim agent</text>
<text class="s" x="340" y="217" text-anchor="middle">Claims corpus</text>
<rect class="b teal" x="460" y="182" width="180" height="50"/>
<text class="h" x="550" y="202" text-anchor="middle" fill="#4ecdc4">Coverage agent</text>
<text class="s" x="550" y="217" text-anchor="middle">Benefits corpus</text>
<line x1="130" y1="232" x2="260" y2="258" class="arr"/>
<line x1="340" y1="232" x2="340" y2="258" class="arr"/>
<line x1="550" y1="232" x2="420" y2="258" class="arr"/>
<rect class="b green" x="200" y="262" width="280" height="32"/>
<text class="h" x="340" y="282" text-anchor="middle" fill="#639922">Grounded answer with citations</text>
</svg>'''


def decision_audit():
    return '''<svg width="100%" viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.amber{fill:#BA751720;stroke:#BA7517}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.coral{fill:#D85A3020;stroke:#D85A30}
.pink{fill:#D4537E20;stroke:#D4537E}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.blue{fill:#378ADD20;stroke:#378ADD}
.green{fill:#63992220;stroke:#639922}
.red{fill:#E24B4A20;stroke:#E24B4A}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Multi-agent + defense-in-depth filtering</text>
<rect class="b" x="250" y="38" width="180" height="34"/>
<text class="h" x="340" y="59" text-anchor="middle">Request</text>
<line x1="340" y1="72" x2="340" y2="88" class="arr"/>
<rect class="b amber" x="120" y="90" width="440" height="55" rx="10" stroke-dasharray="4 3"/>
<text class="s" x="340" y="108" text-anchor="middle" fill="#BA7517">Input filters — defense-in-depth</text>
<rect class="b amber" x="135" y="116" width="110" height="24" rx="4"/>
<text class="s" x="190" y="132" text-anchor="middle">Regex</text>
<rect class="b amber" x="260" y="116" width="110" height="24" rx="4"/>
<text class="s" x="315" y="132" text-anchor="middle">Semantic</text>
<rect class="b amber" x="385" y="116" width="110" height="24" rx="4"/>
<text class="s" x="440" y="132" text-anchor="middle">Embedding</text>
<line x1="340" y1="145" x2="340" y2="162" class="arr"/>
<rect class="b purple" x="190" y="165" width="300" height="34"/>
<text class="h" x="340" y="186" text-anchor="middle" fill="#7F77DD">Orchestrator (LangGraph)</text>
<line x1="240" y1="199" x2="160" y2="222" class="arr"/>
<line x1="440" y1="199" x2="520" y2="222" class="arr"/>
<rect class="b coral" x="60" y="225" width="195" height="50"/>
<text class="h" x="157" y="245" text-anchor="middle" fill="#D85A30">Risk intelligence agent</text>
<text class="s" x="157" y="260" text-anchor="middle">kNN + feature store</text>
<rect class="b pink" x="425" y="225" width="195" height="50"/>
<text class="h" x="522" y="245" text-anchor="middle" fill="#D4537E">Fraud pattern agent</text>
<text class="s" x="522" y="260" text-anchor="middle">Anomaly detection</text>
<line x1="157" y1="275" x2="260" y2="298" class="arr"/>
<line x1="522" y1="275" x2="420" y2="298" class="arr"/>
<rect class="b teal" x="200" y="300" width="280" height="40"/>
<text class="h" x="340" y="318" text-anchor="middle" fill="#4ecdc4">RAG — guidelines, playbooks, SOPs</text>
<text class="s" x="340" y="333" text-anchor="middle">Grounded interpretation</text>
<line x1="340" y1="340" x2="340" y2="358" class="arr"/>
<rect class="b blue" x="200" y="360" width="280" height="34"/>
<text class="h" x="340" y="381" text-anchor="middle" fill="#378ADD">LLM synthesizes recommendation</text>
<line x1="340" y1="394" x2="340" y2="410" class="arr"/>
<rect class="b amber" x="180" y="412" width="320" height="24" rx="4" stroke-dasharray="4 3"/>
<text class="s" x="340" y="428" text-anchor="middle" fill="#BA7517">Output filters (same 3 tiers again)</text>
<line x1="250" y1="436" x2="170" y2="455" class="arr"/>
<line x1="430" y1="436" x2="510" y2="455" class="arr"/>
<rect class="b red" x="80" y="458" width="160" height="24"/>
<text class="s" x="160" y="474" text-anchor="middle" fill="#E24B4A">Human review</text>
<rect class="b green" x="440" y="458" width="160" height="24"/>
<text class="s" x="520" y="474" text-anchor="middle" fill="#639922">Automated action</text>
</svg>'''


def claims_intelligence():
    return '''<svg width="100%" viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.teal{fill:#4ecdc420;stroke:#4ecdc4}
.coral{fill:#D85A3020;stroke:#D85A30}
.blue{fill:#378ADD20;stroke:#378ADD}
.purple{fill:#7F77DD20;stroke:#7F77DD}
.amber{fill:#BA751720;stroke:#BA7517}
.green{fill:#63992220;stroke:#639922}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Hospice per diem claims — three-agent pipeline</text>
<text class="s" x="340" y="40" text-anchor="middle">Adapted from Humana stack after corporate transition to Dragonfly Health</text>
<rect class="b" x="170" y="52" width="340" height="34"/>
<text class="h" x="340" y="73" text-anchor="middle">Claim data ingestion</text>
<line x1="340" y1="86" x2="340" y2="103" class="arr"/>
<rect class="b purple" x="200" y="106" width="280" height="34"/>
<text class="h" x="340" y="127" text-anchor="middle" fill="#7F77DD">Orchestrator (LangGraph)</text>
<line x1="340" y1="140" x2="340" y2="157" class="arr"/>
<rect class="b teal" x="40" y="160" width="190" height="50"/>
<text class="h" x="135" y="180" text-anchor="middle" fill="#4ecdc4">Agent 1: Extract</text>
<text class="s" x="135" y="195" text-anchor="middle">Parse + classify claim</text>
<line class="arr" x1="230" y1="185" x2="248" y2="185"/>
<rect class="b coral" x="250" y="160" width="180" height="50"/>
<text class="h" x="340" y="180" text-anchor="middle" fill="#D85A30">Agent 2: Risk</text>
<text class="s" x="340" y="195" text-anchor="middle">XGBoost scoring</text>
<line class="arr" x1="430" y1="185" x2="448" y2="185"/>
<rect class="b blue" x="450" y="160" width="190" height="50"/>
<text class="h" x="545" y="180" text-anchor="middle" fill="#378ADD">Agent 3: Recommend</text>
<text class="s" x="545" y="195" text-anchor="middle">RAG + LLM synthesis</text>
<line x1="340" y1="210" x2="340" y2="230" class="arr"/>
<rect class="b amber" x="120" y="234" width="440" height="40" rx="6" stroke-dasharray="4 3"/>
<text class="s" x="340" y="250" text-anchor="middle" fill="#BA7517">RAG corpus: hospice benefit rules, Medicare compliance,</text>
<text class="s" x="340" y="265" text-anchor="middle" fill="#BA7517">level-of-care docs, per diem rates, past claims</text>
<line x1="200" y1="274" x2="140" y2="298" class="arr"/>
<line x1="340" y1="274" x2="340" y2="298" class="arr"/>
<line x1="480" y1="274" x2="540" y2="298" class="arr"/>
<rect class="b amber" x="60" y="300" width="150" height="28" rx="6"/>
<text class="s" x="135" y="318" text-anchor="middle" fill="#BA7517">Flag for review</text>
<rect class="b purple" x="265" y="300" width="150" height="28" rx="6"/>
<text class="s" x="340" y="318" text-anchor="middle" fill="#7F77DD">Route to reviewer</text>
<rect class="b green" x="470" y="300" width="150" height="28" rx="6"/>
<text class="s" x="545" y="318" text-anchor="middle" fill="#639922">Claim summary</text>
</svg>'''


def dev_enablement():
    return '''<svg width="100%" viewBox="0 0 680 240" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
.red{fill:#E24B4A15;stroke:#E24B4A}
.green{fill:#63992215;stroke:#639922}
.purple{fill:#7F77DD20;stroke:#7F77DD}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Team transformation — before vs after</text>
<rect class="b red" x="40" y="44" width="280" height="110" rx="10"/>
<text class="h" x="180" y="66" text-anchor="middle" fill="#E24B4A">Before</text>
<text class="s" x="180" y="86" text-anchor="middle">Manual coding, no AI tools</text>
<text class="s" x="180" y="102" text-anchor="middle">Dependent on offshore frontend devs</text>
<text class="s" x="180" y="118" text-anchor="middle">No standardized VCS workflow</text>
<text class="s" x="180" y="134" text-anchor="middle">Slow delivery cycles</text>
<line class="arr" x1="320" y1="99" x2="358" y2="99" stroke="#639922"/>
<rect class="b green" x="360" y="44" width="280" height="110" rx="10"/>
<text class="h" x="500" y="66" text-anchor="middle" fill="#639922">After</text>
<text class="s" x="500" y="86" text-anchor="middle">Codex + Claude Code in VS Code</text>
<text class="s" x="500" y="102" text-anchor="middle">Team self-sufficient on frontend</text>
<text class="s" x="500" y="118" text-anchor="middle">Azure DevOps + branching + CI</text>
<text class="s" x="500" y="134" text-anchor="middle">Rapid development velocity</text>
<rect class="b purple" x="120" y="174" width="440" height="50" rx="10"/>
<text class="h" x="340" y="194" text-anchor="middle" fill="#7F77DD">What you set up</text>
<text class="s" x="200" y="212" text-anchor="middle">AI tool onboarding</text>
<text class="s" x="340" y="212" text-anchor="middle">Git workflow + PRs</text>
<text class="s" x="480" y="212" text-anchor="middle">FastAPI + Jinja2</text>
</svg>'''


def career_timeline():
    return '''<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg">
<style>
.b{fill:var(--surf,#1a1f2b);stroke:var(--brd,#2a3040);stroke-width:0.8;rx:8}
.h{font:600 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec)}
.s{font:400 11px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.arr{stroke:var(--dm,#8892a4);stroke-width:1.2;marker-end:url(#a)}
</style>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2L8 5L2 8" fill="none" stroke="var(--dm,#8892a4)" stroke-width="1.5"/></marker></defs>
<text class="h" x="340" y="22" text-anchor="middle" font-size="15">Full career arc — same pattern, three domains</text>
<rect x="40" y="42" width="140" height="42" rx="8" fill="#4ecdc420" stroke="#4ecdc4" stroke-width="0.8"/>
<text class="h" x="110" y="60" text-anchor="middle" fill="#4ecdc4" font-size="11">Verizon</text>
<text class="s" x="110" y="74" text-anchor="middle" font-size="10">Backend / SQL</text>
<line class="arr" x1="180" y1="63" x2="198" y2="63"/>
<rect x="200" y="42" width="130" height="42" rx="8" fill="#378ADD20" stroke="#378ADD" stroke-width="0.8"/>
<text class="h" x="265" y="60" text-anchor="middle" fill="#378ADD" font-size="11">Pipeline</text>
<text class="s" x="265" y="74" text-anchor="middle" font-size="10">Airflow + SQL</text>
<line class="arr" x1="330" y1="63" x2="348" y2="63"/>
<rect x="350" y="42" width="130" height="42" rx="8" fill="#7F77DD20" stroke="#7F77DD" stroke-width="0.8"/>
<text class="h" x="415" y="60" text-anchor="middle" fill="#7F77DD" font-size="11">Patient ML</text>
<text class="s" x="415" y="74" text-anchor="middle" font-size="10">K-means + PCA</text>
<line class="arr" x1="480" y1="63" x2="498" y2="63"/>
<rect x="500" y="42" width="130" height="42" rx="8" fill="#BA751720" stroke="#BA7517" stroke-width="0.8"/>
<text class="h" x="565" y="60" text-anchor="middle" fill="#BA7517" font-size="11">Warehouse</text>
<text class="s" x="565" y="74" text-anchor="middle" font-size="10">SARIMA</text>
<text class="s" x="340" y="108" text-anchor="middle">Humana — 2018 to 2024</text>
<line x1="60" y1="118" x2="620" y2="118" stroke="var(--brd,#2a3040)" stroke-width="0.5"/>
<line x1="340" y1="118" x2="340" y2="140" class="arr"/>
<rect x="120" y="142" width="150" height="42" rx="8" fill="#D85A3020" stroke="#D85A30" stroke-width="0.8"/>
<text class="h" x="195" y="160" text-anchor="middle" fill="#D85A30" font-size="11">RAG on AWS</text>
<text class="s" x="195" y="174" text-anchor="middle" font-size="10">Nova + Claude</text>
<line class="arr" x1="270" y1="163" x2="288" y2="163"/>
<rect x="290" y="142" width="150" height="42" rx="8" fill="#1D9E7520" stroke="#1D9E75" stroke-width="0.8"/>
<text class="h" x="365" y="160" text-anchor="middle" fill="#1D9E75" font-size="11">Knowledge</text>
<text class="s" x="365" y="174" text-anchor="middle" font-size="10">3 domain agents</text>
<line class="arr" x1="440" y1="163" x2="458" y2="163"/>
<rect x="460" y="142" width="150" height="42" rx="8" fill="#a78bfa20" stroke="#a78bfa" stroke-width="0.8"/>
<text class="h" x="535" y="160" text-anchor="middle" fill="#a78bfa" font-size="11">Decision audit</text>
<text class="s" x="535" y="174" text-anchor="middle" font-size="10">Multi-agent + filters</text>
<text class="s" x="340" y="208" text-anchor="middle">Humana AI Enablement — 2023 to 2024</text>
<line x1="60" y1="218" x2="620" y2="218" stroke="var(--brd,#2a3040)" stroke-width="0.5"/>
<text class="s" x="340" y="238" text-anchor="middle" fill="#BA7517">Corporate transition → Dragonfly Health acquires Enclara</text>
<line x1="340" y1="246" x2="340" y2="264" class="arr"/>
<rect x="140" y="266" width="200" height="42" rx="8" fill="#D85A3020" stroke="#D85A30" stroke-width="0.8"/>
<text class="h" x="240" y="284" text-anchor="middle" fill="#D85A30" font-size="11">Claims intelligence</text>
<text class="s" x="240" y="298" text-anchor="middle" font-size="10">XGBoost + RAG</text>
<line class="arr" x1="340" y1="287" x2="358" y2="287"/>
<rect x="360" y="266" width="200" height="42" rx="8" fill="#63992220" stroke="#639922" stroke-width="0.8"/>
<text class="h" x="460" y="284" text-anchor="middle" fill="#639922" font-size="11">Dev enablement</text>
<text class="s" x="460" y="298" text-anchor="middle" font-size="10">Codex + Claude Code</text>
<text class="s" x="340" y="330" text-anchor="middle">Enclara / Dragonfly Health — 2024+</text>
<rect x="60" y="344" width="560" height="28" rx="8" fill="none" stroke="var(--brd,#2a3040)" stroke-width="0.5" stroke-dasharray="4 3"/>
<text class="s" x="340" y="362" text-anchor="middle" fill="#7F77DD">Same transferable pattern: LangGraph → agents → ML → RAG → guardrails → action</text>
</svg>'''


def war_stories_diagram():
    # Layout: top-center hub, stories spread wide to suit landscape 680x372 viewport.
    # All 5 story nodes are identical 170x80 boxes; gaps kept uniform (~45px clear).
    # Node centers: #1(340,50) #2(530,140) #3(490,300) #4(190,300) #5(150,140)
    return '''<svg width="100%" viewBox="0 0 680 372" xmlns="http://www.w3.org/2000/svg">
<style>
.h{font:600 12px 'Source Sans 3',sans-serif}
.s{font:400 10.5px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4)}
.q{font:italic 9.5px 'Source Sans 3',sans-serif}
.ct{font:700 13px 'Source Sans 3',sans-serif;fill:var(--tx,#e0e4ec);text-anchor:middle}
.note{font:400 10px 'Source Sans 3',sans-serif;fill:var(--dm,#8892a4);text-anchor:middle}
</style>

<!-- Branch lines: hub center (340,192) → each node center, drawn first so boxes sit on top -->
<line x1="340" y1="192" x2="340" y2="90"  stroke="#D85A30" stroke-width="1.5" stroke-opacity="0.4"/>
<line x1="340" y1="192" x2="530" y2="140" stroke="#BA7517" stroke-width="1.5" stroke-opacity="0.4"/>
<line x1="340" y1="192" x2="490" y2="300" stroke="#7F77DD" stroke-width="1.5" stroke-opacity="0.4"/>
<line x1="340" y1="192" x2="190" y2="300" stroke="#378ADD" stroke-width="1.5" stroke-opacity="0.4"/>
<line x1="340" y1="192" x2="150" y2="140" stroke="#1D9E75" stroke-width="1.5" stroke-opacity="0.4"/>

<!-- #1 Set vs List Bug — top-center, node center (340,50) -->
<rect x="255" y="10" width="170" height="80" rx="9" fill="#D85A3012" stroke="#D85A30" stroke-width="1"/>
<text text-anchor="middle" x="340" y="33"  class="h" fill="#D85A30">#1 Set vs List Bug</text>
<text text-anchor="middle" x="340" y="50"  class="s">Code review · mentorship</text>
<text text-anchor="middle" x="340" y="66"  class="q" fill="#D85A30" fill-opacity="0.7">"subtle bug you found"</text>

<!-- #2 Folium Token Spike — upper-right, node center (530,140) -->
<rect x="445" y="100" width="170" height="80" rx="9" fill="#BA751712" stroke="#BA7517" stroke-width="1"/>
<text text-anchor="middle" x="530" y="123" class="h" fill="#BA7517">#2 Folium Token Spike</text>
<text text-anchor="middle" x="530" y="140" class="s">Cost debugging · root cause</text>
<text text-anchor="middle" x="530" y="156" class="q" fill="#BA7517" fill-opacity="0.7">"cost or perf issue"</text>

<!-- #3 Data Masking — lower-right, node center (490,300) -->
<rect x="405" y="260" width="170" height="80" rx="9" fill="#7F77DD12" stroke="#7F77DD" stroke-width="1"/>
<text text-anchor="middle" x="490" y="283" class="h" fill="#7F77DD">#3 Data Masking</text>
<text text-anchor="middle" x="490" y="300" class="s">Privacy · compliance</text>
<text text-anchor="middle" x="490" y="316" class="q" fill="#7F77DD" fill-opacity="0.7">"sensitive data handling"</text>

<!-- #4 Schema Drift — lower-left, node center (190,300) -->
<rect x="105" y="260" width="170" height="80" rx="9" fill="#378ADD12" stroke="#378ADD" stroke-width="1"/>
<text text-anchor="middle" x="190" y="283" class="h" fill="#378ADD">#4 Schema Drift</text>
<text text-anchor="middle" x="190" y="300" class="s">MLOps · observability</text>
<text text-anchor="middle" x="190" y="316" class="q" fill="#378ADD" fill-opacity="0.7">"pipeline failure"</text>

<!-- #5 API Timeout — upper-left, node center (150,140) -->
<rect x="65"  y="100" width="170" height="80" rx="9" fill="#1D9E7512" stroke="#1D9E75" stroke-width="1"/>
<text text-anchor="middle" x="150" y="123" class="h" fill="#1D9E75">#5 API Timeout</text>
<text text-anchor="middle" x="150" y="140" class="s">System resilience · UX</text>
<text text-anchor="middle" x="150" y="156" class="q" fill="#1D9E75" fill-opacity="0.7">"improve reliability"</text>

<!-- Center hub — drawn last so it sits cleanly over line ends -->
<rect x="278" y="166" width="124" height="52" rx="10" fill="var(--surf2,#212736)" stroke="var(--brd,#2a3040)" stroke-width="1.8"/>
<text class="ct" x="340" y="187">Behavioral</text>
<text class="ct" x="340" y="206" font-size="11" fill="#a78bfa">5 War Stories</text>

<!-- Footer -->
<rect x="100" y="350" width="480" height="20" rx="6" fill="none" stroke="var(--brd,#2a3040)" stroke-width="0.5" stroke-dasharray="4 3"/>
<text class="note" x="340" y="364">Each story is 30–45 seconds — keep all five ready for behavioral rounds</text>
</svg>'''


# Map phase IDs to diagram functions
DIAGRAMS = {
    "verizon": verizon_architecture,
    "humana-pipeline": pipeline_flow,
    "humana-patient": patient_clustering,
    "humana-warehouse": warehouse_optimization,
    "humana-rag": rag_architecture,
    "copilot-knowledge": knowledge_copilot,
    "copilot-audit": decision_audit,
    "enclara-claims": claims_intelligence,
    "enclara-dev": dev_enablement,
}
