import os, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ml_utils import train_and_save_model, load_model, predict_from_model, dataset_insights
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_CSV = os.path.join(BASE_DIR, '..', 'sample_data.csv')

@csrf_exempt
def train_model(request):
    if request.method != 'POST':
        return JsonResponse({'error':'Use POST to trigger training'}, status=400)
    result = train_and_save_model(SAMPLE_CSV)
    return JsonResponse({'status':'trained','details':result})

@csrf_exempt
def predict_view(request):
    if request.method != 'POST':
        return JsonResponse({'error':'Use POST with JSON body'}, status=400)
    try:
        body = json.loads(request.body)
    except Exception:
        return JsonResponse({'error':'Invalid JSON'}, status=400)
    model = load_model()
    if model is None:
        return JsonResponse({'error':'Model not found. Train first at /api/train/'}, status=400)
    pred, prob = predict_from_model(model, body)
    return JsonResponse({'prediction': 'Interested' if pred==1 else 'Not Interested', 'probability': float(prob)})

def insights_view(request):
    insights = dataset_insights(SAMPLE_CSV)
    return JsonResponse(insights)
