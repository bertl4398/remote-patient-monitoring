from flask import Flask
from flask import render_template
from flask import Response

import numpy as np
import cv2 as cv


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
