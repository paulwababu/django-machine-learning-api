import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class IrisApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris_api'
    MODEL_FILE = os.path.join(settings.MODELS, "WeightPredictionLinRegModel.joblib")
    model = joblib.load(MODEL_FILE)

class EmitApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emit_api'
    MODEL_FILE = os.path.join(settings.MODELS, "CO2EmissionPredictionLinRegModel.joblib")
    model = joblib.load(MODEL_FILE)

class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    model = joblib.load(MODEL_FILE)    