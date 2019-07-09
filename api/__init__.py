# -*- coding: utf-8 -*-
"""API module."""
import base64
import config
import io
import json

from config import logger
from data import minioClient
from flask import request
from flask_restful import Api, Resource

from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

api = Api(prefix=config.API_PREFIX)


class UploadDataAPI(Resource):
    def post(self):
        data = json.loads(request.data)
        # logger.debug(data["hr"])
        # logger.debug(data["bin"])

        meta = io.BytesIO(bytes(data["hr"]))
        video = io.BytesIO(base64.b64decode(data["bin"]))

        try:
            minioClient.make_bucket(config.PATIENT_ID)
        except BucketAlreadyOwnedByYou:
            pass
        except BucketAlreadyExists:
            pass
        except ResponseError as err:
            logger.exception("MinIO Error")

        try:
            res = minioClient.put_object(config.PATIENT_ID, 'video', video,
                    video.getbuffer().nbytes)
            logger.debug(res)
            res = minioClient.put_object(config.PATIENT_ID, 'meta', meta,
                    meta.getbuffer().nbytes)
            logger.debug(res)
        except Exception:
            logger.exception("MinIO Error")

        return "success", 200


api.add_resource(UploadDataAPI, '/upload')
