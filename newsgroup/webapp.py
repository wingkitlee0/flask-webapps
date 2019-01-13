from flask import Flask, render_template, request
import boto3
import uuid
import joblib
import datetime
import os

app = Flask(__name__)


target_name = ['alt.atheism', 'comp.graphics', 'sci.med', 'sci.space']

def loadmodel():
   s3_client = boto3.client('s3')
   #load model
   bucket = 'ml-bucket-2'
   key = 'best_clf.joblib'
   download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
   s3_client.download_file(bucket, key, download_path)
   clf = joblib.load(download_path)
   return clf

@app.route("/", methods=['GET', 'POST'])
def main():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   cpuCount = os.cpu_count()
   templateData = {
      'title' : 'Web App for News Group',
      'time': timeString,
      'cpucount' : cpuCount
      }
   # load the model from s3
   clf = loadmodel()

   if request.method == 'GET':
      return render_template('main.html', **templateData)
   elif request.method == 'POST':
      resultText = "You wrote: " + request.form['myTextArea']
      label = target_name[clf.predict([request.form['myTextArea']])[0]]
      #label = "%s" % (type(request.form['myTextArea']))
      results = {'text' : resultText, 
                 'label' : label}
      return render_template('main.html', results=results, **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)