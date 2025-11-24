
Buyer Intent Prediction System (Django + ML)

This project is a Django-based Machine Learning application that predicts whether a homebuyer is Interested or Not Interested based on enquiry data. It also exposes REST APIs for training, prediction, and insights generation.

This solution was submitted as part of a Python Developer Take-Home Assignment.

FEATURES
- Machine Learning (scikit-learn)
  • Uses RandomForestClassifier
  • Encodes categorical fields
  • Trains from CSV dataset
  • Saves model using joblib
  
- Django REST APIs
  • POST /api/train/
  • POST /api/predict/
  • GET /api/insights/
- Insights Provided
  • Total enquiries, booked leads, booking percentage
  • Top cities, average income
- Clean Modular Architecture
  • All ML logic inside core/ml_utils.py
  • API inside core/views.py
- GitHub-Safe
  • .gitignore excludes venv, secrets, DB files

SETUP INSTRUCTIONS
1) Create Virtual Environment:
   python -m venv venv
   venv\Scripts\activate

2) Install Dependencies:
   pip install -r requirements.txt

3) Apply Migrations:
   cd buyer_ai
   python manage.py migrate

4) Run the Server:
   python manage.py runserver

API DOCUMENTATION
1. TRAIN MODEL (POST /api/train/)
Sample Response:
{ "status": "trained", "details": { "accuracy": 0.80, "model_path": "buyer_ai/model.joblib" }}

2. PREDICT (POST /api/predict/)
Body:
{ "age": 30, "income": 70000, "city": "Pune", "property_type": "2BHK", "budget": 6000000, "followups": 2, "site_visited": 1 }

3. INSIGHTS (GET /api/insights/)
Sample Response:
{ "total_records": 5, "booked_count": 3, "booking_pct": 60.0 }

MACHINE LEARNING DETAILS
- Algorithm: RandomForestClassifier
- Features: age, income, budget, followups, site_visited, encoded city & property type
- Pipeline: load CSV, encode categories, train, save model, predict via API

SECURITY
- .gitignore excludes venv, .env, DB files, pycache.

Thank You.

