from fastapi import FastAPI
from app.api import health
from app.api import challenges

app = FastAPI(title="Nodox Curriculum Service")
app.include_router(health.router)
app.include_router(challenges.router)