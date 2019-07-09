# -*- coding: utf-8 -*-
"""Data connection module."""
from minio import Minio

import config

minioClient = Minio(config.MINIO_ENDPOINT,
                    access_key=config.MINIO_ACCESS_KEY,
                    secret_key=config.MINIO_SECRET_KEY,
                    secure=config.MINIO_SECURE)
