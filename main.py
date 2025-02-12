from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ledger_core.api import router as ledger_router
from app_name.api import router as app_router
from ledger_core.database import engine, Base

app = FastAPI(title="Ledger Service API")

# Include ledger-related routes
app.include_router(ledger_router)
app.include_router(app_router)

@app.get("/")
def root():
    return {"message": "Ledger API is running"}

@app.on_event("startup")
def on_startup():
    # Initialize DB tables (for first-time setup)
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def on_shutdown():
    # Perform any cleanup tasks here
    pass