import numpy as np
import cv2 as cv

from flask import g


def init_app(app):
    app.teardown_appcontext(close_cap)
    app.teardown_appcontext(close_out)


def get_cap():
    if 'cap' not in g:
        g.cap = cv.VideoCapture(0)

    return g.cap


def get_out():
    if 'out' not in g:
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        g.out = cv.VideoWriter('media/output.mp4', fourcc, 20.0, (640,  480))

    return g.out


def close_cap(e=None):
    cap = g.pop('cap', None)
    if cap is not None:
        cap.release()


def close_out(e=None):
    out = g.pop('out', None)
    if out is not None:
        out.release()
