# KisanAI Live – AI-Powered Agricultural Assistant

![KisanAI Logo](https://via.placeholder.com/800x200?text=KisanAI+Live+-+Smarter+Farming)

**KisanAI Live** is an advanced, AI-powered multimodal farming assistant designed to help farmers detect crop diseases, receive treatment advice, and access smart farming insights using KisanAI Intelligence (powered by Google Gemini), MongoDB Atlas, and Auth0.

## 🚀 Key Features

*   **🌱 KisanAI Vision Disease Detection**: Upload crop photos to instantly detect diseases with high accuracy.
*   **💬 KisanAI Advisor**: Chat with a smart AI assistant for real-time advice in any language (Multilingual support).
*   **🎙️ Voice Assistance**: Speak to the app naturally for hands-free operation.
*   **🌾 Crop & Fertilizer Recommendations**: Get tailored recommendations based on soil and weather conditions.
*   **🌦️ Real-time Weather & Market**: Track local weather and crop market prices.
*   **📄 PDF Reports**: Export analysis results as professional PDF reports.
*   **🔐 Secure Authentication**: Enterprise-grade login system powered by Auth0.
*   **☁️ Cloud Native**: Fully scalable architecture using MongoDB Atlas for data persistence.
*   **📊 Smart Dashboard**: Analytics and history tracking for farmers.

---

## 🏗️ Architecture & SDLC

This project follows a strict **Machine Learning SDLC (Software Development Life Cycle)** and uses a modular **Cookiecutter** project structure.

### 🔷 System Architecture
1.  **Frontend**: HTML5/CSS3 (served via Flask) with Multilingual Support.
2.  **Backend**: Python Flask REST API.
3.  **ML Layer**: KisanAI Intelligence (using Google Gemini Pro Vision & Text).
4.  **Database**: MongoDB Atlas for storing scan history and chat logs.
5.  **Logging & Monitoring**: Custom logging pipeline.

### 🔷 ML Pipeline Flow
1.  **Data Ingestion**: Images are uploaded via the `/api/scan` endpoint.
2.  **Data Transformation**: Images are processed (resized/formatted).
3.  **Model Inference**:
    *   **Vision**: Analyzes the image for disease markers.
    *   **Chat**: Handles contextual farming queries.
4.  **Post-Processing**: Results are formatted into JSON and stored in MongoDB.
5.  **Response**: Frontend displays the diagnosis and treatment plan.

---

## 📂 Project Structure

```
kisanai-live/
│
├── app.py                  # Main Flask Application Entry Point
├── requirements.txt        # Project Dependencies
├── .env.example            # Environment Variables Template
├── setup.py                # Package Setup
│
├── config/                 # Configuration Files
│   └── config.yaml
│
├── src/                    # Source Code
│   ├── components/         # ML Components (Ingestion, Trainer, etc.)
│   ├── pipeline/           # Prediction & Training Pipelines
│   ├── database/           # MongoDB Wrapper
│   ├── logger/             # Custom Logger
│   ├── exception/          # Custom Exception Handler
│   └── utils/              # Utility Functions
│
├── api/                    # API Routes (Blueprints)
│
├── notebooks/              # Jupyter Notebooks for Experiments
│
├── artifacts/              # Generated Artifacts (Logs, Data)
│
└── frontend/               # UI Files (HTML/CSS)
```

---

## 🛠️ Setup & Installation

### 0. Prerequisites
*   **Python 3.8+**: [Download & Install Python](https://www.python.org/downloads/)
    *   ⚠️ **IMPORTANT**: During installation, check the box **"Add Python to PATH"**.
*   **Git**: [Download Git](https://git-scm.com/downloads)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/kisanai-live.git
cd kisanai-live
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment
Rename `.env.example` to `.env` and add your API keys:
```ini
GEMINI_API_KEY=your_key
MONGODB_URL=your_connection_string
AUTH0_DOMAIN=...
```

### 5. Run the Application
```bash
python app.py
```
Open `http://localhost:5000` in your browser.

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/scan` | Upload image for disease detection |
| `POST` | `/api/chat` | Chat with AI advisor |
| `POST` | `/api/recommend/crop` | Get crop recommendations |
| `POST` | `/api/recommend/fertilizer` | Get fertilizer recommendations |
| `GET` | `/api/history` | Get scan history from MongoDB |
| `GET` | `/api/profile` | Get user profile details |

---

## 🏆 Hackathon Strategy

This project is built to win by demonstrating:
1.  **Real-world Impact**: Solving a critical problem for farmers.
2.  **Tech Depth**: Full SDLC, custom pipelines, and cloud integration.
3.  **Design Quality**: Professional, responsive UI.
4.  **Completeness**: End-to-end working system from DB to UI to AI.

---

Built with ❤️ by the KisanAI Team.
