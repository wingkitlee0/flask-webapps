from flask import Flask, render_template, request
import datetime
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   cpuCount = os.cpu_count()
   templateData = {
      'title' : 'Abstract Analyzer',
      'time': timeString,
      'cpucount' : cpuCount
      }
   if request.method == 'GET':
      return render_template('main.html', **templateData)
   elif request.method == 'POST':
      resultText = "You wrote: " + request.form['myTextArea']
      results = {'text' : resultText}
      return render_template('main.html', results=results, **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)