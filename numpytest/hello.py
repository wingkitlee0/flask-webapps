import numpy as np
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is my random number: %f" % np.random.random() 

if __name__ == "__main__":
    app.run(debug=True)
