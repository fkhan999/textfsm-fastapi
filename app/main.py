from fastapi import FastAPI
from app.routes import textfsm_route

app = FastAPI()

# Include the router for textfsm parsing
app.include_router(textfsm_route.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the TextFSM Parser API"}
