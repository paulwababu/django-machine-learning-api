from django.urls import path
from .views import *

urlpatterns = [
    path('', Prediction.as_view(), name = 'prediction'),
    path('emit/', EmissionPrediction.as_view(), name = 'emission_prediction'),
]