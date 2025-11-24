Buyer Intent Prediction System (Django + ML)

This project is a Django-based Machine Learning application that predicts whether a homebuyer is Interested or Not Interested based on enquiry data. It also exposes REST APIs for training, prediction, and insights generation.

This solution was submitted as part of a Python Developer Take-Home Assignment.

🚀 Features
✔ Machine Learning (scikit-learn)

Uses RandomForestClassifier

Encodes categorical fields (city, property type)

Trains from CSV dataset

Saves model using joblib

✔ Django REST APIs

POST /api/train/ → Train or retrain ML model

POST /api/predict/ → Predict buyer interest

GET /api/insights/ → Dataset statistics & analytics

✔ Insights Provided

Total enquiries

Number of booked leads

Booking percentage

Top cities

Average income

Useful summary for business teams

✔ Clean, Modular Architecture

ML code inside core/ml_utils.py

REST API logic inside core/views.py

No database dependency

Easy to extend with PostgreSQL

✔ GitHub-Safe

.gitignore ensures:

No venv/

No secrets

No sqlite db

No pycache

Safe for public sharing

📂 Project Structure
buyer_ai_solution/
│
├── buyer_ai/                     # Django project
│   ├── buyer_ai/                 # Settings, URLs
│   └── core/                     # ML + API module
│
├── sample_data.csv               # Training dataset
├── requirements.txt              # Dependencies
├── run_instructions.md           # Setup steps
├── README.md                     # Documentation
└── .gitignore                    # Git-safe rules

🛠️ Tech Stack

Python 3.10+

Django

Django REST Framework

Pandas, NumPy

scikit-learn (RandomForestClassifier)

Joblib

SQLite

🔧 Setup Instructions
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Apply Migrations
cd buyer_ai
python manage.py migrate

4️⃣ Run the Server
python manage.py runserver

📡 API Documentation
🔥 1. Train Model

POST /api/train/

Sample Response:

{
  "status": "trained",
  "details": {
    "accuracy": 0.80,
    "model_path": "buyer_ai/model.joblib"
  }
}

🔥 2. Predict Buyer Intent

POST /api/predict/

Sample Request:

{
  "age": 30,
  "income": 70000,
  "city": "Pune",
  "property_type": "2BHK",
  "budget": 6000000,
  "followups": 2,
  "site_visited": 1
}


Sample Response:

{
  "prediction": "Interested",
  "probability": 0.93
}

🔥 3. Get Insights

GET /api/insights/

Sample Response:

{
  "total_records": 5,
  "booked_count": 3,
  "booking_pct": 60.0,
  "top_cities": {
    "Pune": 2,
    "Mumbai": 1
  },
  "avg_income": 79000
}

📊 Machine Learning Model Details

Algorithm: RandomForestClassifier

Target Variable: booked (1 = Interested, 0 = Not Interested)

Features:

age

income

budget

followups

site_visited

encoded city

encoded property type

Pipeline:

Load CSV

Encode categorical fields

Train model

Save using joblib

Serve predictions via API

🔐 Security & Git Safety

.gitignore excludes:

venv/

.env

*.sqlite3

__pycache__/

Cached model files

No sensitive data in the repository

Fully safe for public GitHub submission

🙋 Developer Notes

This project focuses on:

Clean REST API design

Simple yet functional ML pipeline

Clear coding structure

Easy setup and testing

🎉 Thank You!
