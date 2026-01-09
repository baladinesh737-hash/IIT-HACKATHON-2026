from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
import json
from datetime import datetime

# =========================
# APP INIT
# =========================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# CONFIG
# =========================
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"
DATA_FILE = "cases.json"

# =========================
# MODELS
# =========================
class LoginRequest(BaseModel):
    username: str
    password: str

class CaseRequest(BaseModel):
    customer: str
    amount: int

# =========================
# UTILS
# =========================
def load_cases():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_cases(cases):
    with open(DATA_FILE, "w") as f:
        json.dump(cases, f, indent=2)

# =========================
# AI ANALYSIS (OLLAMA)
# =========================
def analyze_case(amount):
    prompt = f"""
You are an AI system for Debt Collection Agency.

Given overdue amount ₹{amount},
classify the case priority as:
HIGH, MEDIUM, or LOW.

Give a short reason.

Respond strictly in this format:
Priority: <HIGH|MEDIUM|LOW>
Reason: <one sentence>
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()
        text = data.get("response", "")

        priority = "UNKNOWN"
        reason = "No reason generated"

        for line in text.splitlines():
            if "Priority" in line:
                priority = line.split(":", 1)[1].strip()
            if "Reason" in line:
                reason = line.split(":", 1)[1].strip()

        return priority, reason

    except Exception as e:
        return "ERROR", str(e)

# =========================
# ROUTES
# =========================
@app.get("/")
def home():
    return {"message": "FastAPI backend running successfully"}

@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "1234":
        return {"success": True}
    return {"success": False}

@app.post("/create_case")
def create_case(data: CaseRequest):
    cases = load_cases()

    case = {
        "id": len(cases) + 1,
        "customer": data.customer,
        "amount": data.amount,
        "status": "CREATED",
        "created_at": datetime.now().isoformat()
    }

    cases.append(case)
    save_cases(cases)

    return {
        "message": "Case created successfully",
        "case": case
    }

@app.post("/ai_prioritize")
def ai_prioritize(data: CaseRequest):
    priority, reason = analyze_case(data.amount)
    return {
        "priority": priority,
        "reason": reason
    }

@app.get("/cases")
def get_cases():
    return load_cases()
