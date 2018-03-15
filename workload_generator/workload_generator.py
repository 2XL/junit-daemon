from nameko.standalone.events import event_dispatcher
import yaml, os, random, string
from namekos.settings import BROKER_URL, DAEMON_LANGUAGE


class WorkloadGenerator(object):
    def __init__(self, config=None, language=None):
        if config is None:
            self.config = {
                'AMQP_URI': BROKER_URL
            }

        if language is None:
            self.language = DAEMON_LANGUAGE

        self.token = 'hash_key of the submission'  # todo
        self.submission = None
        self.token_size = 16
        pass

    def _broadcast_event(self, service, event, payload):
        dispatcher = event_dispatcher(self.config, use_confirms=False)
        dispatcher(service, event, payload)
        return True

    def submit(self, payload=None, fixture=None, case='answer'):
        # broadcast submission to emulator-daemon workers
        fixture_payload = None
        if fixture is None:
            pass  # no payload nor fixture for submitted
        elif isinstance(fixture, str):

            if not os.path.exists(fixture):
                fixture = os.path.join('fixture', fixture)

                if not os.path.exists(fixture):
                    exit(4)

            with open(fixture, 'r') as fstream:
                fixture_payload = yaml.load(fstream)
        elif isinstance(fixture, dict):
            fixture_payload = fixture
        else:
            exit(2)
        if fixture_payload is not None:
            payload = fixture_payload

        if payload is None:
            exit(1)

        self._parse_submission(payload)
        self._broadcast_event(
            service='school',
            event='codechallenge_submitted_{language}'.format(
                language=self.language
            ),
            payload=dict(
                token=self.token,
                snippet=self.submission[case],
                language=self.language,
                valid_assertion=self.submission['valid_assertion']
            )
        )

    def _parse_submission(self, payload):
        self.token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.token_size))
        self.submission = payload['challenge']


# if __name__ == "__main__":
#     workload_generator = WorkloadGenerator
#     workload_generator.submit(fixture=yaml.load(fstream))

pass
