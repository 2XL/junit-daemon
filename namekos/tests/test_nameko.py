import sys, os

source_path = os.path.dirname(os.path.abspath(__file__))
print source_path
sys.path.insert(0, source_path + '/../')

from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter
from namekos import EmulatorService
from namekos.settings import DAEMON_LANGUAGE, SERVICE_NAME


def test_handle_code_challenge_submissions(container_factory, rabbit_config):
    container = container_factory(EmulatorService, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)

    # print service received payload before execute
    with entrypoint_waiter(
            container=container,
            method_name='check_challenge'):
        # broadcast_event
        dispatch(service_name=SERVICE_NAME,
                 event_type='codechallenge_submitted_{language}'.format(
                     language=DAEMON_LANGUAGE
                 ),
                 event_data={
                     'payload': 'payload_value',
                     'language': DAEMON_LANGUAGE,
                     'token': 'token goes here'
                 })
        pass
