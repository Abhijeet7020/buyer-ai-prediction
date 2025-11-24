from django.urls import path
from . import views
urlpatterns = [path('train/', views.train_model), path('predict/', views.predict_view), path('insights/', views.insights_view)]
