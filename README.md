# PredictoBot AI — 24/7 Digital Public Examiner

A decoupled multimodal AI evaluation pipeline engineered to bridge the high-stakes evaluation gap for state board higher-secondary students. Prototyped for the Kerala DHSE curriculum, PredictoBot AI separates generative perception from deterministic rule evaluation to eliminate grade hallucinations while providing instant diagnostic feedback.

---

## 📌 Problem Statement

In Kerala's public higher-secondary ecosystem, the Plus One pass rate dropped from 67.30% to 62.28% in 2025, triggering an academic evaluation crisis. While private coaching institutes charge ₹25,000+ annually, public school students face multi-week evaluation delays.

Standard Large Language Models fail state-board grading due to three architectural limitations:
1. **Vernacular & Semantic Barriers:** Inability to reliably normalize colloquial Manglish and handwritten regional accounting notations.
2. **Deterministic Step Grading:** Generative models hallucinate intermediate marks and cannot guarantee zero-variance step-by-step mark deduction.
3. **Curriculum Agnosticism:** Commercial AI tools ignore localized state practical standards (e.g., KITE GNU/Linux LibreOffice Calc workflows).

---

## 🏛️ System Architecture

PredictoBot AI employs an isolated, two-tier decoupled architecture:

```text
[ Student Scan / Notebook / .ods File ]
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│  Tier 1: Semantic Perception & Ingestion (Google Gemini)│
│  - Multimodal handwritten text & table parsing         │
│  - Manglish normalization to canonical syllabus terms   │
│  - SCERT textbook grounding via Context Caching        │
│  - Structured JSON schema extraction (Confidence Check)│
└──────────────────────────┬─────────────────────────────┘
                           │ Strict JSON Output
                           ▼
┌────────────────────────────────────────────────────────┐
│  Tier 2: Deterministic Rule Engine (Isolated Core)     │
│  - Matches student steps against DHSE Valuation Scheme │
│  - Mathematical deduction execution (Zero LLM grading) │
│  - Maps errors to canonical DHSE Rule IDs              │
└──────────────────────────┬─────────────────────────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
┌───────────────────────────┐ ┌──────────────────────────┐
│   Student Instant Audit   │ │ Municipal Heatmap Engine │
│ - 17/20 itemized score    │ │ - School-level deficits │
│ - Bilingual explanations  │ │ - Pre-exam interventions │
└───────────────────────────┘ └──────────────────────────┘
