from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AI-Powered DB Designer", version="1.0.0")


# ----------------------------
# Health Check
# ----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ----------------------------
# Request Models
# ----------------------------
class ParseRequest(BaseModel):
    text: str


class SchemaRequest(BaseModel):
    text: str


class QueryRequest(BaseModel):
    plan_id: str
    intents: List[str]


# ----------------------------
# Endpoints
# ----------------------------
@app.post("/spec/parse")
def parse_spec(req: ParseRequest):
    return {
        "ir": {
            "entities": ["Patient", "Provider", "Visit"],
            "attributes": {"Patient": ["id", "name"], "Provider": ["id", "specialty"], "Visit": ["id", "patient_id", "provider_id"]}
        },
        "ambiguities": ["'Visit' could mean appointment or hospital stay"],
        "warnings": ["No primary key mentioned for Visit"]
    }


@app.post("/schema/generate")
def generate_schema(req: SchemaRequest):
    return {
        "ddl_bundle": [
            "CREATE TABLE patient (id INT PRIMARY KEY, name VARCHAR(100));",
            "CREATE TABLE provider (id INT PRIMARY KEY, specialty VARCHAR(100));",
            "CREATE TABLE visit (id INT PRIMARY KEY, patient_id INT, provider_id INT, FOREIGN KEY(patient_id) REFERENCES patient(id), FOREIGN KEY(provider_id) REFERENCES provider(id));"
        ],
        "rationale": [
            "Chose INT for IDs for efficiency",
            "Normalized into 3NF"
        ],
        "quality_score": 0.92
    }


@app.post("/query/generate")
def generate_queries(req: QueryRequest):
    return {
        "queries": {
            "list_patients": "SELECT * FROM patient;",
            "visits_by_org": "SELECT v.* FROM visit v JOIN provider p ON v.provider_id=p.id;"
        },
        "indexes": ["CREATE INDEX idx_visit_patient ON visit(patient_id);"],
        "explain_notes": ["Index on visit.patient_id accelerates joins"]
    }


@app.get("/demo/unified")
def unified_contract():
    return {
        "ir": {
            "entities": ["Patient", "Provider", "Visit"],
            "relationships": ["Visit.patient_id -> Patient.id", "Visit.provider_id -> Provider.id"]
        },
        "ddl_bundle": [
            "CREATE TABLE patient (...);",
            "CREATE TABLE provider (...);",
            "CREATE TABLE visit (...);"
        ],
        "queries": {
            "list_patients": "SELECT * FROM patient;",
            "visits_by_org": "SELECT v.* FROM visit v JOIN provider p ON v.provider_id=p.id;"
        },
        "indexes": ["CREATE INDEX idx_visit_patient ON visit(patient_id);"],
        "quality_score": 0.92
    }
