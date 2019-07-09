# -*- coding: utf-8 -*-
"""Main module."""
import config

from api import api
from config import logger
from flask import Flask
from flask import render_template


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
