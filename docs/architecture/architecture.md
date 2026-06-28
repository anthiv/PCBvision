# Architecture

PCBVision follows a modular architecture separating the application layer, inference logic, database access, ML workflows, and deployment configuration.

## Main Components

- `app/`: FastAPI application and production inference service
- `ml/`: training, evaluation, experimentation, and model development code
- `tests/`: automated tests
- `configs/`: configuration files
- `scripts/`: utility scripts
- `docker/`: Docker-related files
- `docs/`: project documentation