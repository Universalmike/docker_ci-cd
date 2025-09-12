#  ML API with CI/CD (FastAPI + GitHub Actions + Docker + Render)

A simple **Machine Learning Operations (MLOps)** starter project that shows how to:

- Train a basic ML model (Iris classification)
- Serve predictions through a **FastAPI** web API
- Containerize the app using **Docker**
- Automate testing and deployment with **GitHub Actions**
- Deploy a live API on **Render**

This project is ideal for learning **CI/CD for machine learning** from end-to-end.

---

## 📂 Project Structure

ml_api_cicd/
│── train.py # Train and save the model
│── predict.py # Model prediction logic
│── main.py # FastAPI app
│── requirements.txt # Python dependencies
│── Dockerfile # Container definition
│── tests/
│ └── test_api.py # Pytest-based API tests
│── .github/
│ └── workflows/
│ ├── ci.yml # CI pipeline: run tests/lint
│ └── cd.yml # CD pipeline: build & push Docker image
└── README.md



---

## 🏃‍♂️ Quick Start (Local)

### 1️⃣ Train the Model
```bash
python train.py

**RUN THE API**

uvicorn main:app --reload


Visit http://127.0.0.1:8000/docs
 for interactive Swagger UI.

Make a Prediction

Example curl request:

curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'


Run with Docker

Build and run the container:

docker build -t ml-api .
docker run -p 8000:8000 ml-api


Open http://127.0.0.1:8000/docs
.

**CI/CD Workflow**

Continuous Integration (CI) – .github/workflows/ci.yml

Runs automatically on every push or pull request

Installs dependencies

Runs pytest tests and linter checks

Continuous Deployment (CD) – .github/workflows/cd.yml

Builds the Docker image

Pushes it to Docker Hub / GitHub Container Registry

Render automatically pulls the latest image and redeploys the live API


**Live API**

Base URL: https://<your-render-app-name>.onrender.com

Interactive docs:

https://<your-render-app-name>.onrender.com/docs

**Tech Stack**

Python 3.9

FastAPI – REST API framework

scikit-learn – ML model training

Docker – Containerization

GitHub Actions – CI/CD pipelines

Render – Hosting and deployment

**Contributing**

Feel free to fork this repo, open issues, or submit pull requests if you’d like to improve it.

**License**

This project is released under the MIT License.


---

🔧 **Tip:**  
Replace every `https://<your-render-app-name>.onrender.com` with your actual Render URL so people can try your live endpoint.


**Examples showing how a website (JavaScript/React) and a mobile app (Flutter/Dart) can call your live FastAPI endpoint**

**React Component example**

import React, { useState } from "react";
import axios from "axios";

export default function IrisPredictor() {
  const [features, setFeatures] = useState([5.1, 3.5, 1.4, 0.2]);
  const [prediction, setPrediction] = useState(null);

  const callAPI = async () => {
    try {
      const res = await axios.post(
        "https://<your-render-app-name>.onrender.com/predict",
        { features }
      );
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Iris Prediction</h2>
      <button onClick={callAPI}>Predict</button>
      {prediction !== null && <p>Prediction: {prediction}</p>}
    </div>
  );
}



