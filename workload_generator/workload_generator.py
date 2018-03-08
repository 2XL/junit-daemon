from nameko.standalone.events import event_dispatcher

from namekos.settings import BROKER_URL, DAEMON_LANGUAGE


class WorkloadGenerator():
    def __init__(self, config=None, language=None):
        if config is None:
            self.config = {
                'AMQP_URI': BROKER_URL
            }

        if language is None:
            self.language = DAEMON_LANGUAGE

        self.token = 'hash_key of the submission'  # todo
        self.submission = None
        pass

    def broadcast_event(self, service, event, payload):
        dispatcher = event_dispatcher(self.config, use_confirms=False)
        dispatcher(service, event, payload)
        return True

    def submit(self, case='answer'):
        # broadcast submission to emulator-daemon workers
        self.broadcast_event(
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

    def parse_submission(self):
        pass


if __name__ == "__main__":
    workload_generator = WorkloadGenerator

    workload_generator.parse_submission(payload)

    workload_generator.submit()

    pass
