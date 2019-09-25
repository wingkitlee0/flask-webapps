from flask import render_template
from flask import request

import pandas as pd

import datetime
import os

from gcpredict import app, model

MODELFILE = 'data/clf.joblib'

@app.route('/')
@app.route("/test", methods=['GET', 'POST'])
def main():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    cpuCount = os.cpu_count()

    mymodel = model.Model(modelfile=os.path.join(app.static_folder, MODELFILE))

    templateData = {
        'title' : 'Green Card Predictor',
        'time': timeString,
        'cpucount' : cpuCount,
        'country' : 'HK',
        'category_list' : mymodel.category_list,
    }
    if request.method == 'GET':
        return render_template('main.html', **templateData)
    elif request.method == 'POST':
        #nationality = request.args.getlist('myCountry')
        nationality = request.form['myCountry']
        category = request.form['myCategory']
        date1 = request.form['date1']
        has_rfe = request.form['myRFE']

        params = {
            'nationality' : nationality,
            'category' : category,
            'date1' : date1,
            'has_rfe' : has_rfe
        }

        prediction_date = mymodel.predict(**params)
        print(request.args)
        resultText = "You are from {} and applied the GC on {}.".format(nationality, date1)
        results = {
            'text' : resultText,
            'prediction_date' : prediction_date,
        }
        return render_template('main.html', results=results, **templateData)