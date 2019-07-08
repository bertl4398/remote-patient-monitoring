import os
import threading

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import jsonify


def record_video(cap, out):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.flip(frame, 1)
        out.write(frame)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import video
    video.init_app(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/api/record")
    def record():
        print("Start recording...")
        cap = video.get_cap()
        out = video.get_out()
        if not cap.isOpened():
            print("Cannot open camera")
        else:
            record_thread = threading.Thread(target=record_video,
                                             args=(cap, out,))
            record_thread.start()

        return jsonify()

    @app.route("/api/upload")
    def upload():
        print("Upload data...")
        return jsonify()

    return app
