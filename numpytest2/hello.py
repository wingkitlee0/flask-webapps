import numpy as np
from flask import Flask
import tensorflow as tf


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is my random number: %f \n The tensorflow version is %s" % (np.random.random() , tf.__version__)

if __name__ == "__main__":
    app.run(debug=True)
