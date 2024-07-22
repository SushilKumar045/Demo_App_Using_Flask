
import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('Demo_app_flask.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    SqFt = float(request.args.get('SqFt'))
    Bedrooms = float(request.args.get('Bedrooms'))
    Bathrooms = float(request.args.get('Bathrooms'))
    Offers = float(request.args.get('Offers'))
    Brick = float(request.args.get('Brick'))
    Neighborhood  = float(request.args.get('Neighborhood'))

    prediction = model.predict([[SqFt, Bedrooms, Bathrooms, Offers, Brick, Neighborhood]])
    return render_template('index.html', prediction_text='Regression Model  has predicted Price for given requirements is : {}'.format(prediction))

if __name__=="__main__":
  app.run(debug=True)
