from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

from PIL import Image

client = TestClient(app)


def create_test_image(image_format: str) -> BytesIO:
    image_bytes = BytesIO()

    image = Image.new("RGB", (10, 10))
    image.save(image_bytes, format=image_format)

    image_bytes.seek(0)
    return image_bytes

def test_predict_accepts_jpeg_image():
    files = {
        "file": (
            "pcb.jpg",
            BytesIO(b"fake-image-content"),
            "image/jpeg",
        )
    }

    response = client.post("/predict", files=files)

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "pcb.jpg"
    assert data["content_type"] == "image/jpeg"
    assert data["model_name"] == "PCBVision Dummy Model"
    assert isinstance(data["detections"], list)
    assert len(data["detections"]) == 1

    detection = data["detections"][0]

    assert detection["defect_class"] == "missing_hole"
    assert detection["confidence"] == 0.97
    assert detection["bbox"] == {
        "x_min": 120,
        "y_min": 45,
        "x_max": 180,
        "y_max": 90,
    }


def test_predict_accepts_jpeg_image():
    files = {
        "file": (
            "pcb.jpg",
            create_test_image("JPEG"),
            "image/jpeg",
        )
    }

    response = client.post("/predict", files=files)

    assert response.status_code == 200

def test_predict_rejects_invalid_image_content():
    files = {
        "file": (
            "pcb.jpg",
            BytesIO(b"fake-image-content"),
            "image/jpeg",
        )
    }

    response = client.post("/predict", files=files)

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid image file."
    }
    
def test_predict_rejects_unsupported_file_type():
    files = {
        "file": (
            "notes.txt",
            BytesIO(b"not an image"),
            "text/plain",
        )
    }

    response = client.post("/predict", files=files)

    assert response.status_code == 415
    assert response.json() == {
        "detail": "Unsupported file type. Upload a JPEG or PNG image."
    }


def test_predict_requires_a_file():
    response = client.post("/predict")

    assert response.status_code == 422