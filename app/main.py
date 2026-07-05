from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.inference_service import run_inference
from app.schemas.prediction import PredictionResponse

app = FastAPI(title="PCBVision")


@app.get("/")
def root():
    return {"message": "Welcome to PCBVision"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must be a JPEG or PNG image.",
        )

    image_bytes = await file.read()

    return run_inference(
        image_bytes=image_bytes,
        filename=file.filename,
        content_type=file.content_type,
    )