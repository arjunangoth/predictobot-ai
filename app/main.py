from fastapi import FastAPI

app = FastAPI(title="PredictoBot AI API", version="0.1.0")

@app.get("/")
async def health_check():
    return {"status": "online", "engine": "PredictoBot Deterministic Evaluator"}
