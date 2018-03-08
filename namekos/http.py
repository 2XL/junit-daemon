# http.py

import json, os
from nameko.web.handlers import HttpRequestHandler
from werkzeug.wrappers import Response
from nameko.exceptions import safe_for_serialization
from utils import get_metrics
from settings import SERVICE_NAME


class HttpError(Exception):
    error_code = 'BAD_REQUEST'
    status_code = 400


class InvalidArgumentsError(HttpError):
    error_code = 'INVALID_ARGUMENTS'


class HttpEntrypoint(HttpRequestHandler):
    def response_from_exception(self, exc):
        if isinstance(exc, HttpError):
            response = Response(
                json.dumps({
                    'error': exc.error_code,
                    'message': safe_for_serialization(exc),
                }),
                status=exc.status_code,
                mimetype='application/json'
            )
            return response
        return HttpRequestHandler.response_from_exception(self, exc)


http = HttpEntrypoint.decorator


class Service:
    name = SERVICE_NAME

    @http('GET', '/metrics')
    def get_status(self, request):
        return Response(get_metrics())

    @http('GET', '/ping')
    def get_ping(self, request):
        return Response('pong')

# curl localhost:8000/status | jq '.'
