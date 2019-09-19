from flask import render_template
from flask import request

import pandas as pd

import datetime
import os

from gcpredict import app, model

@app.route('/')
@app.route("/test", methods=['GET', 'POST'])
def main():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    cpuCount = os.cpu_count()

    mymodel = model.Model()

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
        date = request.form['date1']
        print(request.args)
        resultText = "You are from {}. The date is {}".format(nationality, date)
        results = {'text' : resultText}
        return render_template('main.html', results=results, **templateData)