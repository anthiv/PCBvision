from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.prediction import PredictionResponse
from app.services.inference_service import run_inference
from PIL import Image
from io import BytesIO

router = APIRouter()


@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to PCBVision"}


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@router.post("/predict", response_model=PredictionResponse)
async def predict_image(
    file: UploadFile = File(...),
) -> PredictionResponse:
    allowed_content_types = {"image/jpeg", "image/png"}

    if file.content_type not in allowed_content_types:
        raise HTTPException(
            status_code=415,
            detail="Unsupported file type. Upload a JPEG or PNG image.",
        )

    image_bytes = await file.read()
    try:
        image = Image.open(BytesIO(image_bytes))
        image.verify()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file."
        )
    return run_inference(
        image_bytes=image_bytes,
        filename=file.filename or "unknown",
        content_type=file.content_type,
    )

