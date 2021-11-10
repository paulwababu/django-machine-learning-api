import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Prediction(APIView):
    def post(self, request):
        #data = request.data
        age= request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ApiConfig.model
        #predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)

class WeightPrediction(APIView):
    def post(self, request):
        #data = request.data
        height = request.GET.get('height')#'175'
        gender = request.GET.get('gender')#'Male'
        if gender == 'Male':
            gender = 0
        elif gender == 'Female':
            gender = 1
        else:
            return Response("Gender field is invalid", status=400)
        lin_reg_model = IrisApiConfig.model
        weight_predicted = lin_reg_model.predict([[gender, height]])[0][0]
        weight_predicted = np.round(weight_predicted, 1)
        response_dict = {"Predicted Weight (kg)": weight_predicted}
        print(response_dict)
        return Response(response_dict, status=200)

class EmissionPrediction(APIView):
    def post(self, request):
        data = request.data
        weight = request.GET.get('weight')
        volume = request.GET.get('volume')
        lin_reg_model = EmitApiConfig.model
        weight_predicted = lin_reg_model.predict([[weight, volume]])
        weight_predicted = np.round(weight_predicted, 1)
        response_dict = {"Predicted CO2 Emission: ": weight_predicted}
        print(response_dict)
        return Response(response_dict, status=200)