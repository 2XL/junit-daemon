from os import environ
import logging

if environ.get('SENTRY_DSN') is None:
    raven_logger = logging.getLogger('raven.base.Client')
    raven_logger.setLevel(logging.CRITICAL) # or FATAL
    # https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels

from emulator import EmulatorService
from http import Service
