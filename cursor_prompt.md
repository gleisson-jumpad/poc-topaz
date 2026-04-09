# Topaz Knowledge Base Builder -- Cursor Agent Prompt

> **Purpose**: This prompt allows any Cursor agent session to autonomously build the Topaz knowledge base from scratch. Copy the entire PROMPT section below into a new Cursor chat to execute.

---

## PROMPT

You are tasked with building a comprehensive knowledge base about Topaz (a Stefanini Group company specialized in financial technology) for use by LLM-powered sales support agents. The output must be a single consolidated Markdown file in Brazilian Portuguese (pt-BR).

### PHASE 1: SCRAPE WEBSITE CONTENT

Fetch the content of each URL below using the WebFetch tool. Run them in parallel batches to save time. Store the fetched content in memory -- you will use it in Phase 3.

**Product pages (9 URLs):**
1. `https://www.topazevolution.com/topaz-one` -- Topaz One platform overview
2. `https://www.topazevolution.com/topaz-one/financialcore` -- FinancialCore (Core Banking)
3. `https://www.topazevolution.com/topaz-one/secure-journey` -- SecureJourney (Anti-fraud & AML)
4. `https://www.topazevolution.com/topaz-one/finchannels` -- FinChannels (Omnichannel Banking)
5. `https://www.topazevolution.com/topaz-one/finxperience` -- FinXperience (AI Personalization)
6. `https://www.topazevolution.com/topaz-one/techpay` -- TechPay (Payment Orchestration)
7. `https://www.topazevolution.com/topaz-one/techinvest` -- TechInvest (Investment Management)
8. `https://www.topazevolution.com/topaz-one/finorigination` -- FinOrigination (Digital Origination)
9. `https://www.topazevolution.com/topaz-one/bankingtools` -- BankingTools (Financial & IT Automation)

**Institutional & sector pages (5 URLs):**
10. `https://www.topazevolution.com/a-topaz/quem-somos/` -- About Topaz (history, mission, team, awards)
11. `https://www.topazevolution.com/setores/bancos` -- Solutions for Banks
12. `https://www.topazevolution.com/setores/fintech` -- Solutions for Fintechs
13. `https://www.topazevolution.com/setores/microfinancas-cooperativas` -- Solutions for Cooperatives
14. `https://www.topazevolution.com/setores/varejo-utilidades-telecomunicacoes` -- Solutions for Retail/Utilities/Telecom

### PHASE 2: READ EXISTING INTERNAL MATERIALS

Read these two files from the workspace. They contain transcriptions of internal video presentations with EXCLUSIVE content not available on the website:

1. `topaz_one.md` -- Contains: sales engagement playbook (how to adapt pitch by audience: CFO, product team, IT team), "start with a pain point and expand" strategy, 80-90% transactional coverage metric, detailed operational cases (Sicredi multi-level with 100+ cooperatives, BNB public bank transformation, PagBank 40M accounts, Banco Vox automotive segment), AI agents for client autonomy vision.

2. `topaz_core_banking.md` -- Contains: complete competitive landscape (local: Matera, Syncia, Pismo, Dock, Dimensa, Outbank; global: Temenos, Tecnicis, Oracle, Fizz, Mambu, Bantotal, Fog Machine), 5 commercial models (SaaS, PaaS, CAPEX licensing, Revenue Share, Hybrid), tech stack (Java, microservices, Kubernetes, OpenShift, JMS, BPM), 3-layer architecture (domain, application logic, services), implementation timeline (8-12 months, agile, incremental), Topaz Open (standard core version for fintechs), cases with granular metrics (Bradescar Mexico 200M txns/R$300bi volume, Agibank 6M clients/14M loans, Aylos 1.7M clients/13 cooperatives, PagBank scaled 3->30M accounts).

### PHASE 3: CREATE SECTION FILES

Create the directory `knowledge_base/sections/` and write one `.md` file per section. Each section must be written in **Brazilian Portuguese (pt-BR)**, with a **professional, sales-oriented tone**. Do NOT include raw transcription text -- only processed, structured information.

Combine the website content (Phase 1) with the exclusive internal material (Phase 2) into each section.

**Files to create (in order):**

| File | Content |
|---|---|
| `01_empresa.md` | **A Empresa Topaz**: who they are, history (4 decades), Stefanini Group, numbers (25 countries, 300+ clients, 550M+ end users, 97% satisfaction, 2000+ employees), mission/vision/values, recognitions (Gartner, Forrester, Celent, ISO 9001/27001/27701, iBeta, PCI), strategic allies (Microsoft Azure, AWS, Google Cloud), 20% revenue reinvested in innovation. Source: "Quem Somos" page + footers. |
| `02_topaz_one.md` | **Topaz One -- Plataforma Full Banking**: overview of the world's first full banking platform, 8 product families summary (one paragraph each), key differentiators (modular architecture, hybrid deployment, scalability, regulatory compliance, low-code autonomy, AI agents), 80-90% transactional coverage metric, functional architecture (front/mid/backend layers). Sources: Topaz One main page + topaz_one.md. |
| `03_financial_core.md` | **FinancialCore -- Core Banking**: executive summary, 4 sub-products (Core Universal, Core Digital, Core Microfinance, ERP Consorcio), features (account management, transaction processing, loan control, card issuance, regulatory compliance, omnichannel integration), benefits (operational efficiency, risk reduction, client experience, regulatory compliance), 3-layer architecture (domain, application logic, services), tech stack (Java, microservices, K8s, OpenShift, JMS, BPM), Topaz Open (standard version), implementation timeline (8-12 months), target audience, ecosystem integration, FAQ. Sources: FinancialCore page + topaz_core_banking.md. |
| `04_secure_journey.md` | **SecureJourney -- Antifraude e Seguranca**: executive summary, modules (decision manager, secure onboarding, fraud prevention, AML/CFT), real-time monitoring with AI/ML, behavioral analysis, iBeta facial authentication certification, 90% Brazilian financial market adoption, false positive reduction, integration with BACEN/PCI-DSS/LGPD, ecosystem integration, FAQ. Source: SecureJourney page + topaz_one.md. |
| `05_fin_channels.md` | **FinChannels -- Omnichannel Banking**: executive summary, modules (channel orchestrator, digital channels, physical channels, specialized services, sales force, self-service), integrable channels list (mobile, internet banking, ATM, chatbots, POS, call center), differentiators (cloud-ready, open finance integration, customizable journey engine), benefits (enhanced CX, loyalty/retention, cost optimization up to 30%, competitive advantage), FAQ. Source: FinChannels page + topaz_one.md. |
| `06_fin_xperience.md` | **FinXperience -- Experiencia Personalizada com IA**: executive summary, modules (retention/loyalty/churn reduction, open experiences), how it personalizes (AI/ML, API integration, real-time data, dynamic journey adaptation, intelligent recommendation engine), differentiators (embedded compliance, sub-second response, native multichannel, legacy compatibility, adjustable decision engine), use cases by segment (banks, fintechs, cooperatives, retailers), practical cases (AI onboarding, behavioral offers, omnichannel service, predictive retention), ecosystem integration, FAQ. Source: FinXperience page + topaz_one.md. |
| `07_tech_pay.md` | **TechPay -- Orquestracao de Pagamentos**: executive summary, modules (digital currencies, instant payments, PSTI certification), what payment orchestration is vs traditional gateway, benefits (cost reduction, autonomy/scalability, specialized support, instant settlement, fraud protection, enhanced UX), transaction types (bills, transfers, commercial, government), PSTI = first certified provider specialized in financial institutions, ecosystem integration, FAQ. Source: TechPay page + topaz_one.md. |
| `08_tech_invest.md` | **TechInvest -- Gestao de Investimentos**: executive summary, modules (fixed income, variable income, fund management, derivatives, wealth management), fixed income products detail (federal bonds, CDBs, LCI/LCA, CRI/CRA, debentures, fixed income funds), distribution channels (Tesouro Direto, home brokers, app/internet banking), private banking & derivatives (futures, options, swaps, NDFs), benefits (cost reduction, scale, API integration, dashboards, operational flexibility), ideal for whom, ecosystem integration, FAQ. Source: TechInvest page + topaz_one.md. |
| `09_fin_origination.md` | **FinOrigination -- Originacao Digital**: executive summary, modules (digital origination, field origination, electronic acceptance), target audience (traditional/digital banks, fintechs, retailers, autonomous agents), product scope (bank accounts, credit products), benefits (time reduction, scalability, compliance, CRM/core integration, client autonomy), differentiators (fast time-to-market, embedded security, proven scalability, local support, customizable UI), ecosystem integration, FAQ. Source: FinOrigination page + topaz_one.md. |
| `10_banking_tools.md` | **BankingTools -- Automacao Financeira e TI**: executive summary, modules (IT tools & automation, regulatory & accounting), how automation works (product issuance, cash flow, audits/reconciliation, accounting entries), benefits (operational optimization, data quality, automatic compliance, IT automation, accounting efficiency), how it frees IT for innovation, differentiators (scalability, compliance-ready, accelerated time-to-market, API integration, local+global support), ecosystem integration, FAQ. Source: BankingTools page + topaz_one.md. |
| `11_setores.md` | **Solucoes por Setor**: For each sector, describe challenges, trends, which Topaz products apply, and a highlight case. **Bancos**: legacy modernization, scalability, regulatory automation, case Banestes. **Fintechs**: go-to-market acceleration, BaaS, scalability, case PagBank (1M to 33M daily txns, 80K txns/min, R$1tri processed). **Cooperativas e Microfinancas**: multi-level management, Topaz Open, compliance Bacen, case Sicredi (1M clients in 3 months). **Varejo, Utilities e Telecom**: fraud prevention, embedded finance, personalization. Sources: 4 sector pages. |
| `12_cases.md` | **Cases de Sucesso**: Consolidated table/list of ALL cases with metrics. **Sicredi**: 100+ cooperatives, multi-level, multi-company, physical channels + anti-fraud + core banking + treasury. **BNB**: public bank, digital transformation, physical/digital channels + core banking. **PagBank**: 40M+ accounts on core, scaled 3->30M accounts, 33M daily txns, 80K txns/min, R$1tri volume, anti-fraud. **Banco Vox**: automotive segment, in-project, configurability/autonomy focus. **Bradescar Mexico**: 2.5M clients, 200M txns, R$300bi annual volume. **Agibank**: 6M clients, 4M txns, 14M loans. **Aylos**: 1.7M clients, 13 cooperatives, 2M loans. **Banestes**: digital transformation, agile account opening. Sources: topaz_one.md + topaz_core_banking.md + sector pages. |
| `13_cenario_competitivo.md` | **Cenario Competitivo**: **Local competitors** (Matera, Syncia, Outbank, Pismo, Dock, Dimensa, Funcoes e Sistemas) -- tend to offer specialized/modular solutions requiring additional integrations. **Global competitors** (Temenos, Tecnicis, Oracle, Fizz, Mambu, Bantotal, Fog Machine) -- robust but complex platforms, high implementation cost, tech dependency, monolithic architectures, less integration capability. **Topaz positioning**: modern architecture, flexibility, lowest TCO, modular full banking platform, 25 countries, Gartner/Celent recognized. Source: topaz_core_banking.md + site mentions. |
| `14_modelos_comerciais.md` | **Modelos Comerciais**: 5 models with description and ideal use case. **SaaS**: monthly fee + variable per transaction, ideal for predictability and scalability. **PaaS**: platform + infrastructure, more tech autonomy. **CAPEX Licensing**: upfront investment + maintenance, for institutions preferring own management. **Revenue Share**: remuneration follows revenue generation, ideal for digital wallets and acquiring. **Hybrid**: setup + monthly + variable, balance between investment and growth. Implementation timeline: 8-12 months average, agile/incremental, modular by business domain, no Big Bang required. Source: topaz_core_banking.md. |
| `15_playbook_vendas.md` | **Playbook de Vendas**: How to engage clients with the platform vision. **By persona**: CFO prioritizes cost reduction and efficiency; Product/Channels team focuses on digital experience and UX; Technology team cares about architecture, robustness, and stack. **Entry strategy**: start with a specific pain point, solve it, then expand engagement showing the broader platform capability. **Key selling arguments**: 80-90% transactional coverage, modular contracting (part by part), low-code autonomy for clients, AI agents for optimization, hybrid deployment (on-premise + multi-cloud), 25-country presence with local expertise, Gartner/Celent recognition. **Platform pitch flow**: 1) Topaz positioning, 2) Platform overview (8 families), 3) Functional architecture, 4) Differentiators adapted to audience, 5) Relevant case study. Source: topaz_one.md. |

### PHASE 4: CREATE BUILD SCRIPT

Create `knowledge_base/build_kb.py` -- a Python script that:
1. Reads all `.md` files from `knowledge_base/sections/` sorted by filename (numeric prefix)
2. Adds a header with metadata (generation date, version, source count)
3. Concatenates all sections with clear `---` separators between them
4. Writes the output to `knowledge_base/topaz_knowledge_base.md`

### PHASE 5: BUILD AND VALIDATE

1. Run `python knowledge_base/build_kb.py` to generate the consolidated file
2. Read the output file and verify:
   - All 15 sections are present
   - No raw transcription text leaked through
   - Content is in pt-BR
   - Competitive analysis from topaz_core_banking.md is included
   - Commercial models from topaz_core_banking.md are included
   - Sales playbook from topaz_one.md is included
   - All 8 cases (Sicredi, BNB, PagBank, Banco Vox, Bradescar, Agibank, Aylos, Banestes) are present
3. Report the final file size (lines and approximate word count)

### WRITING GUIDELINES

- **Language**: Brazilian Portuguese (pt-BR) for all content
- **Tone**: Professional, sales-oriented, confident but not aggressive
- **No raw transcriptions**: Process and structure all information
- **Numbers matter**: Always include metrics, percentages, client counts
- **FAQ sections**: Include relevant FAQs from the website in each product section
- **No marketing fluff**: Be specific and concrete, avoid empty superlatives
- **Heading hierarchy**: H1 for major sections, H2 for sub-sections, H3 for details
- **Target reader**: An LLM agent that answers questions from salespeople about Topaz products, pricing, competitors, implementation, and use cases
