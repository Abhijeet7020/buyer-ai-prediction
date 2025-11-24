import pandas as pd, os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model.joblib')

def _prepare(df):
    df = df.copy()
    le_city = LabelEncoder()
    if 'city' in df.columns:
        df['city_enc'] = le_city.fit_transform(df['city'].astype(str))
    else:
        df['city_enc'] = 0
    le_prop = LabelEncoder()
    df['prop_enc'] = le_prop.fit_transform(df['property_type'].astype(str))
    features = ['age','income','budget','followups','site_visited','city_enc','prop_enc']
    X = df[features].fillna(0)
    y = df['booked'].astype(int)
    return X, y

def train_and_save_model(csv_path):
    df = pd.read_csv(csv_path)
    X, y = _prepare(df)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)
    score = clf.score(X, y)
    joblib.dump(clf, MODEL_PATH)
    return {'accuracy': float(score), 'model_path': MODEL_PATH}

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def predict_from_model(model, payload):
    df = pd.DataFrame([payload])
    df['city_enc'] = 0
    df['prop_enc'] = 0
    features = ['age','income','budget','followups','site_visited','city_enc','prop_enc']
    X = df[features].fillna(0)
    pred = model.predict(X)[0]
    prob = np.max(model.predict_proba(X))
    return int(pred), float(prob)

def dataset_insights(csv_path):
    df = pd.read_csv(csv_path)
    total = len(df)
    booked = df['booked'].sum()
    booking_pct = (booked/total)*100 if total>0 else 0
    top_cities = df['city'].value_counts().head(5).to_dict()
    avg_income = df['income'].mean()
    return {'total_records': int(total), 'booked_count': int(booked), 'booking_pct': booking_pct, 'top_cities': top_cities, 'avg_income': float(avg_income)}
