from fastapi import FastAPI
from app.api import health

app = FastAPI(title="Nodox Curriculum Service")
app.include_router(health.router)