# -*- coding: utf-8 -*-
"""Settings module."""


class BaseConfig(object):
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    PATIENT_ID = ''
    MINIO_ENDPOINT = ''
    MINIO_ACCESS_KEY = ''
    MINIO_SECRET_KEY = ''
    MINIO_SECURE = False


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    MINIO_ENDPOINT = ''
    MINIO_ACCESS_KEY = ''
    MINIO_SECRET_KEY = ''
    MINIO_SECURE = True


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    MINIO_ENDPOINT = ''
    MINIO_ACCESS_KEY = ''
    MINIO_SECRET_KEY = ''
    MINIO_SECURE = False
