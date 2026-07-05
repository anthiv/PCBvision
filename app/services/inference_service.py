from app.schemas.prediction import BoundingBox, Detection, PredictionResponse

def run_inference(image_bytes: bytes, filename: str, content_type: str) -> PredictionResponse:
    return PredictionResponse(
        filename=filename,
        content_type=content_type,
        model_name="PCBVision Dummy Model",
        detections=[
            Detection(
                defect_class="missing_hole",
                confidence=0.97,
                bbox=BoundingBox(
                    x_min=120,
                    y_min=45,
                    x_max=180,
                    y_max=90,
                ),
            )
        ],
    )