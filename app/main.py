from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tickets
from app.database import create_tables

app = FastAPI(title="AI Ticket System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_tables()

app.include_router(tickets.router)

@app.get("/")
def root():
    return {"status": "running", "message": "AI Ticket System API"}