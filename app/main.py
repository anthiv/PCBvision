from fastapi import FastAPI

app = FastAPI(title="PCBVision")

@app.get("/")
def root():
    return {"message": "Welcome to PCBVision"}

@app.get("/health")
def health():
    return {"status": "healthy"}