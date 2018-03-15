import logging, os, sys

from nameko.events import event_handler, SINGLETON

from pipeline import executor
from utils import broadcast_event
from settings import DAEMON_LANGUAGE, SERVICE_NAME

logging.getLogger('raven').setLevel(logging.WARNING)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class EmulatorService(object):
    name = 'emulator'

    # service_target: source-service, event-type
    @event_handler(SERVICE_NAME,
                   'codechallenge_submitted_{language}'.format(language=DAEMON_LANGUAGE),
                   handler_type=SINGLETON, reliable_delivery=True)
    def check_challenge(self, payload):
        token = payload.get('token')
        snippet = payload.get('snippet')
        language = payload.get('language')
        runner_framework = payload.get('runner_framework', 'junit')
        assertion_snippet = payload.get('valid_assertion')

        data = '\n'.join(snippet) + '\n'.join(assertion_snippet)

        # TODO: make all :|
        submission = executor.PipelineExecutor()
        # generate the project directories
        submission.load_queue_from_submission(code=data)
        submission.apply_queue()

        logger.info(
            'nameko request {token} snippet {snippet} assertion {assertion}'.format(token=token, snippet=snippet,
                                                                                    assertion=assertion_snippet))

        status = 'not correct'
        pass

        logger.info('nameko response? {status} +++ [{token}] +++ '.format(status=status, token=token))
