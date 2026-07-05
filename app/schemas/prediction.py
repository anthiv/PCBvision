from pydantic import BaseModel

class BoundingBox(BaseModel):
    x_min: int
    y_min: int
    x_max: int
    y_max: int


class Detection(BaseModel):
    defect_class: str
    confidence: float
    bbox: BoundingBox


class PredictionResponse(BaseModel):
    filename: str
    content_type: str
    model_name: str
    detections: list[Detection]