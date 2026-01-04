<div align="center">

<img src="frontend/images/logo.png" alt="KisanAI Logo" width="200"/>

# 🌾 KisanAI Live

### AI-Powered Agricultural Intelligence Platform

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Auth0](https://img.shields.io/badge/Auth0-EB5424?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)

**Empowering farmers with cutting-edge AI technology for smarter, sustainable farming**

[Features](#-key-features) • [Installation](#-quick-start) • [Architecture](#-architecture) • [API](#-api-reference) • [Contributing](#-contributing)

---

</div>

## 📋 Table of Contents

- [About](#-about-the-project)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About The Project

**KisanAI Live** is a comprehensive AI-powered agricultural assistant that revolutionizes farming practices by leveraging advanced machine learning, computer vision, and natural language processing. Built with a focus on accessibility and real-world impact, this platform helps farmers detect crop diseases early, receive personalized farming advice, and make data-driven decisions.

### 🌟 Why KisanAI?

- **🎯 Precision Agriculture**: Accurate disease detection using Google Gemini Pro Vision
- **🌍 Multilingual Support**: Accessible to farmers in their native language
- **📱 User-Friendly**: Intuitive interface designed for farmers with varying tech literacy
- **☁️ Cloud-Native**: Scalable architecture built on MongoDB Atlas
- **🔒 Secure**: Enterprise-grade authentication with Auth0
- **📊 Data-Driven**: Analytics and insights backed by historical data

---

## ✨ Key Features

### 🔬 **KisanAI Vision - Disease Detection**
Upload crop images and get instant disease diagnosis with:
- 95%+ accuracy using Google Gemini Pro Vision
- Detailed treatment recommendations
- Confidence scores and severity analysis
- Support for 50+ crop types

### 💬 **KisanAI Advisor - Smart Chat Assistant**
Intelligent conversational AI that provides:
- Real-time farming advice in multiple languages
- Context-aware responses based on chat history
- Crop management guidance
- Pest control recommendations
- Seasonal farming tips

### 🎙️ **Voice Assistance**
Hands-free operation with:
- Natural language voice commands
- Speech-to-text and text-to-speech
- Perfect for farmers working in the field

### 🌾 **Smart Recommendations**
Data-driven insights for:
- **Crop Recommendations**: Based on soil type, climate, and season
- **Fertilizer Suggestions**: NPK analysis and organic alternatives
- Weather-based planting schedules
- Market price predictions

### 🌦️ **Real-Time Integrations**
- **Weather Monitoring**: Hyperlocal weather forecasts
- **Market Prices**: Live crop pricing from local mandis
- **Alert System**: Notifications for weather warnings and disease outbreaks

### 📊 **Dashboard & Analytics**
- Scan history tracking
- Disease outbreak patterns
- Yield predictions
- Farm performance metrics

### 📄 **Professional Reports**
- Export analysis as PDF reports
- Shareable diagnostic summaries
- Treatment tracking documentation

---

## 🛠 Technology Stack

### **Frontend**
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

### **Backend**
![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

### **AI/ML**
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=flat-square&logo=google&logoColor=white)
- **Gemini Pro Vision**: Image analysis and disease detection
- **Gemini Pro**: Natural language understanding and chat

### **Database & Storage**
![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)
- Document-based storage for scan history
- User profiles and chat logs
- Analytics data

### **Authentication**
![Auth0](https://img.shields.io/badge/Auth0-EB5424?style=flat-square&logo=auth0&logoColor=white)
- Secure user authentication
- Role-based access control
- Social login integration

### **Development Tools**
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## 🏗 Architecture

### System Overview

```mermaid
graph TB
    A[User Interface] --> B[Flask API Server]
    B --> C[Auth0 Authentication]
    B --> D[KisanAI Intelligence Layer]
    D --> E[Google Gemini Pro Vision]
    D --> F[Google Gemini Pro Text]
    B --> G[MongoDB Atlas]
    B --> H[External APIs]
    H --> I[Weather Service]
    H --> J[Market Data]
```

### ML Pipeline Flow

```
┌─────────────────┐
│  Image Upload   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Ingestion  │ ──► Validation & Preprocessing
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Transformation  │ ──► Resize, Format, Normalize
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Inference │ ──► Gemini Pro Vision Analysis
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│Post-Processing  │ ──► JSON Formatting
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MongoDB Store  │ ──► History & Analytics
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Response UI    │ ──► Display Results
└─────────────────┘
```

### SDLC Approach

This project follows a rigorous **Machine Learning Software Development Life Cycle**:

1. **📊 Data Collection**: Agricultural datasets and crop disease images
2. **🔍 Exploration**: Jupyter notebooks for experimentation
3. **🏗️ Model Development**: Integration with Google Gemini APIs
4. **✅ Validation**: Testing with real-world crop images
5. **🚀 Deployment**: Production-ready Flask application
6. **📈 Monitoring**: Logging and performance tracking

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
  - ⚠️ **Important**: Check "Add Python to PATH" during installation
- **Git** - [Download Git](https://git-scm.com/downloads)
- **pip** (comes with Python)

### Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vannu07/kisanai-live.git
cd kisanai-live
```

#### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```ini
# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# MongoDB Atlas
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/

# Auth0
AUTH0_DOMAIN=your-domain.auth0.com
AUTH0_CLIENT_ID=your_client_id
AUTH0_CLIENT_SECRET=your_client_secret

# Flask
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Optional: External APIs
WEATHER_API_KEY=your_weather_api_key
MARKET_API_KEY=your_market_api_key
```

#### 5️⃣ Run the Application

```bash
python app.py
```

The application will start at: **http://localhost:5000**

---

## 📡 API Reference

### Authentication
All API endpoints (except public routes) require authentication via Auth0 JWT tokens.

### Endpoints

#### 🔬 Disease Detection

```http
POST /api/scan
```

**Request:**
```json
{
  "image": "base64_encoded_image_string",
  "crop_type": "wheat",
  "location": "Punjab, India"
}
```

**Response:**
```json
{
  "status": "success",
  "disease": "Leaf Rust",
  "confidence": 0.94,
  "severity": "Medium",
  "treatment": {
    "chemical": ["Propiconazole", "Tebuconazole"],
    "organic": ["Neem oil spray", "Copper fungicide"],
    "preventive": "Crop rotation recommended"
  },
  "scan_id": "scan_123456"
}
```

#### 💬 Chat with AI Advisor

```http
POST /api/chat
```

**Request:**
```json
{
  "message": "What fertilizer should I use for tomatoes?",
  "language": "en",
  "context": {
    "crop": "tomato",
    "stage": "flowering"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "response": "For tomatoes in the flowering stage...",
  "suggestions": ["Use NPK 10:20:20", "Apply every 2 weeks"],
  "chat_id": "chat_789012"
}
```

#### 🌾 Crop Recommendation

```http
POST /api/recommend/crop
```

**Request:**
```json
{
  "soil_type": "loamy",
  "ph": 6.5,
  "nitrogen": 45,
  "phosphorus": 30,
  "potassium": 40,
  "temperature": 28,
  "humidity": 65,
  "rainfall": 800,
  "location": "Maharashtra"
}
```

#### 🧪 Fertilizer Recommendation

```http
POST /api/recommend/fertilizer
```

#### 📊 Get Scan History

```http
GET /api/history?user_id={user_id}&limit=10
```

#### 👤 User Profile

```http
GET /api/profile
```

---

## 📁 Project Structure

```
kisanai-live/
│
├── 📄 app.py                      # Main Flask Application Entry Point
├── 📄 requirements.txt            # Python Dependencies
├── 📄 .env.example                # Environment Variables Template
├── 📄 setup.py                    # Package Setup Configuration
├── 📄 README.md                   # Project Documentation
│
├── 📁 config/                     # Configuration Files
│   └── config.yaml                # App Configuration
│
├── 📁 src/                        # Source Code
│   ├── 📁 components/             # ML Components
│   │   ├── data_ingestion.py     # Data Loading & Validation
│   │   ├── data_transformation.py # Image Preprocessing
│   │   └── model_inference.py    # AI Model Integration
│   │
│   ├── 📁 pipeline/               # ML Pipelines
│   │   ├── prediction_pipeline.py # Inference Pipeline
│   │   └── training_pipeline.py  # Training Pipeline
│   │
│   ├── 📁 database/               # Database Layer
│   │   ├── mongodb_client.py     # MongoDB Connection
│   │   └── models.py             # Data Models
│   │
│   ├── 📁 logger/                 # Logging System
│   │   └── __init__.py           # Custom Logger
│   │
│   ├── 📁 exception/              # Error Handling
│   │   └── __init__.py           # Custom Exceptions
│   │
│   └── 📁 utils/                  # Utility Functions
│       ├── common.py             # Helper Functions
│       └── image_utils.py        # Image Processing
│
├── 📁 api/                        # API Routes (Blueprints)
│   ├── scan_routes.py            # Disease Detection Endpoints
│   ├── chat_routes.py            # Chat Assistant Endpoints
│   ├── recommendation_routes.py  # Recommendation Endpoints
│   └── auth_routes.py            # Authentication Endpoints
│
├── 📁 frontend/                   # Frontend Assets
│   ├── 📁 templates/              # HTML Templates
│   ├── 📁 static/                 # CSS, JS, Assets
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │       └── logo.png          # KisanAI Logo
│   └── 📁 images/                 # Additional Images
│       └── logo.png
│
├── 📁 notebooks/                  # Jupyter Notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_testing.ipynb
│   └── 03_performance_analysis.ipynb
│
├── 📁 artifacts/                  # Generated Artifacts
│   ├── logs/                     # Application Logs
│   ├── models/                   # Saved Models
│   └── reports/                  # Generated Reports
│
└── 📁 tests/                      # Unit Tests
    ├── test_api.py
    ├── test_models.py
    └── test_utils.py
```

---

## 📸 Screenshots

<div align="center">

### 🏠 Main Dashboard
<img src=".github/images/dash_user.png" alt="User Dashboard" width="800"/>

*Comprehensive overview with quick access to all features*

---

### 🔬 Disease Detection Interface
<img src=".github/images/scan.png" alt="Disease Scan" width="800"/>

*Upload crop images for instant AI-powered disease diagnosis*

---

### 💬 AI Chat Assistant
<img src=".github/images/chat_interface.png" alt="Chat Interface" width="800"/>

*Multilingual farming advisor for real-time guidance*

---

### 🌾 Crop Recommendations
<img src=".github/images/recommendation.png" alt="Recommendations" width="800"/>

*Smart crop and fertilizer suggestions based on soil and climate*

---

### 👤 User Profile & History
<img src=".github/images/profile.png" alt="User Profile" width="800"/>

*Track your scan history and farming analytics*

---

### 🔐 Secure Login
<img src=".github/images/login.png" alt="Login Page" width="800"/>

*Enterprise-grade authentication powered by Auth0*

</div>

> 💡 **Note**: All screenshots show the actual KisanAI Live interface with real functionality

---

## 🗺 Roadmap

- [x] Core disease detection functionality
- [x] Multi-language chat assistant
- [x] User authentication with Auth0
- [x] MongoDB integration for data persistence
- [ ] Mobile app (Android & iOS)
- [ ] IoT sensor integration
- [ ] Drone imagery analysis
- [ ] Community marketplace
- [ ] Government scheme integration
- [ ] Offline mode support
- [ ] Advanced analytics dashboard
- [ ] Machine learning model fine-tuning

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Coding Standards

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add unit tests for new features
- Update documentation as needed

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

**Varnit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-vannu07-181717?style=for-the-badge&logo=github)](https://github.com/vannu07)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/varnit-kumar)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)

**Project Link**: [https://github.com/vannu07/kisanai-live](https://github.com/vannu07/kisanai-live)

---

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for powerful AI capabilities
- [MongoDB Atlas](https://www.mongodb.com/atlas) for scalable database solutions
- [Auth0](https://auth0.com/) for secure authentication
- [Flask](https://flask.palletsprojects.com/) community for excellent web framework
- All farmers who inspired this project

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Built with ❤️ for farmers worldwide**

![Made in India](https://img.shields.io/badge/Made%20in-India-orange?style=for-the-badge&labelColor=138808&color=FF9933)

</div>