# PCBVision

> **A production-ready PCB inspection platform demonstrating end-to-end Machine Learning Engineering practices.**

PCBVision is an end-to-end Machine Learning Engineering project focused on automated Printed Circuit Board (PCB) defect detection. Rather than demonstrating only model development, the project showcases the complete lifecycle of building, deploying, and maintaining production-ready computer vision systems.

The primary objective is to bridge the gap between machine learning experimentation and production engineering by integrating modern software engineering and MLOps practices into a single industrial application.

---

## 🚀 Project Goals

PCBVision demonstrates:

* Industrial computer vision for PCB defect detection
* Production-ready API development with FastAPI
* Experiment tracking with MLflow
* Containerized deployment using Docker
* Automated testing with Pytest
* Continuous Integration with GitHub Actions
* Clean software architecture and modular design
* Production-focused Machine Learning Engineering workflows

---

## 🛠 Tech Stack

| Layer               | Technology             |
| ------------------- | ---------------------- |
| Backend             | FastAPI, Pydantic      |
| Machine Learning    | PyTorch, YOLO, OpenCV  |
| Database            | PostgreSQL             |
| Experiment Tracking | MLflow                 |
| Containerization    | Docker, Docker Compose |
| CI/CD               | GitHub Actions         |
| Testing             | Pytest                 |

---

## 📌 Current Status

**Sprint 1 – Planning & Design** ✅

### Completed

* [x] Project Vision
* [x] Product Specification
* [x] System Architecture
* [x] Dataset Selection
* [x] Repository Architecture

### Next Milestones

* [ ] Environment setup
* [ ] Baseline YOLO model
* [ ] FastAPI inference service
* [ ] PostgreSQL integration
* [ ] Dockerization
* [ ] MLflow integration
* [ ] Streamlit demo
* [ ] CI/CD pipeline

---

## 📂 Repository Structure

```text
pcbvision/
│
├── app/            # FastAPI application
├── ml/             # Training, inference and evaluation
├── configs/        # Configuration files
├── scripts/        # Utility scripts
├── tests/          # Automated tests
├── notebooks/      # Research and experimentation
├── docker/         # Docker configuration
├── docs/           # Project documentation
└── assets/         # Images, diagrams and media
```

---

## 📚 Documentation

* [Vision](docs/product/vision.md)
* [Product Specification](docs/product/product-spec.md)
* [Architecture](docs/architecture/architecture.md)

---

## 🎯 Project Philosophy

PCBVision is built around one core idea:

> **Move from building machine learning models to building production-ready machine learning products.**

The project emphasizes engineering decisions, maintainability, reproducibility, and clean software architecture as much as model performance.

---

## 📄 License

This project is licensed under the MIT License.
