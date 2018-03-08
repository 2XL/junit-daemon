import os

DAEMON_LANGUAGE = os.environ.get('DAEMON_LANGUAGE', 'java')
SERVICE_NAME = os.environ.get('SERVICE_NAME', 'school')
BROKER_URL = os.environ.get('BROKER_URL', None)
