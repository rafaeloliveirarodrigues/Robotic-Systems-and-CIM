from flask import Flask, request
from flask_restful import Resource, Api

import joblib
import pandas as pd



#give one line from the dataset and the prediction is returned
class ModelPrediction(Resource):
    model = joblib.load("C:/Users/rafae/Desktop/UNI/SRCIM/T2/best_clf.joblib")

    def post(self):
        x = pd.read_json(request.get_json(), typ='series')

        pred = self.model.predict([x])

        return int(pred[0]), 200


app = Flask(__name__)
api = Api(app)

api.add_resource(ModelPrediction, '/modelprediction')

app.run(debug=True)
