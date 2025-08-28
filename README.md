# MyOnSite-Technical-Assessment
# AI-Powered Database Schema Optimizer & Query Generator

## 📌 Project Overview
This project takes **natural language database requirements** and produces:
- Parsed entities & relationships
- Optimized schema (DDL statements)
- SQL queries based on user intents
- Suggested indexes & optimizations
- Unified JSON contract

Built with **FastAPI** and containerized using **Docker**.

---

## 🚀 Features
- REST API endpoints:
  - `/health` → Service status
  - `/spec/parse` → Parse NL spec into IR
  - `/schema/generate` → Generate schema (DDL + rationale + score)
  - `/query/generate` → Generate SQL queries + indexes
  - `/demo/unified` → Full pipeline in one payload

---

## 🛠️ Setup & Run

### 1. Clone Repo
```bash
git clone https://github.com/your-username/AI-DB-Designer.git
cd AI-DB-Designer
```

### 2. Build & Run with Docker
```bash
docker compose build
docker compose up
```

### 3. Open Swagger UI
Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📊 Example Usage

### Parse Spec
**Input**
```json
{ "text": "Patients, Providers, Visits. Each visit links a patient and provider." }
```

**Response**
```json
{
  "entities": ["Patient", "Provider", "Visit"],
  "warnings": ["No primary key mentioned for Visit"]
}
```

### Generate Schema
**Input**
```json
{ "text": "Generate schema for patient, provider, visit system" }
```

**Response**
```json
{
  "ddl_bundle": [
    "CREATE TABLE patient (id INT PRIMARY KEY, name VARCHAR(100));",
    "CREATE TABLE provider (id INT PRIMARY KEY, specialty VARCHAR(100));",
    "CREATE TABLE visit (id INT PRIMARY KEY, patient_id INT, provider_id INT, FOREIGN KEY(patient_id) REFERENCES patient(id), FOREIGN KEY(provider_id) REFERENCES provider(id));"
  ],
  "rationale": ["Chose INT for IDs for efficiency", "Normalized into 3NF"],
  "quality_score": 0.92
}
```

### Generate Queries
**Input**
```json
{
  "plan_id": "plan-demo",
  "intents": ["list_patients", "visits_by_org"]
}
```

**Response**
```json
{
  "queries": {
    "list_patients": "SELECT * FROM patient;",
    "visits_by_org": "SELECT v.* FROM visit v JOIN provider p ON v.provider_id=p.id;"
  },
  "indexes": ["CREATE INDEX idx_visit_patient ON visit(patient_id);"],
  "explain_notes": ["Index on visit.patient_id accelerates joins"]
}
```

---

## 📽️ Demo Video
👉 [Video Link Here](YOUR_VIDEO_LINK)

---

## 📦 Tech Stack
- FastAPI (Python)
- Docker & Docker Compose
- Swagger UI (auto-generated API docs)

---

## ✅ Conclusion
This project demonstrates an AI-powered pipeline for **database design automation**.  
It runs in Docker and exposes clean REST APIs for schema optimization & query generation.
