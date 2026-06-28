             User

               │

               ▼

        Streamlit UI

               │

               ▼

          FastAPI API

               │

       POST /predict

               │

               ▼

      Inference Service

               │

               ▼

         YOLO Model

               │

               ▼

      Prediction Results

               │

        ┌──────┴──────┐

        ▼             ▼

 PostgreSQL        Streamlit

 (metadata)      Visualization