from nameko.events import event_handler, BROADCAST
import logging, json

logger = logging.getLogger()


class WorkloadGeneratorService(object):
    name = 'workload_generator'

    @event_handler('emulator', 'codechallenge_checked', handler_type=BROADCAST, reliable_delivery=False)
    def codechallenge_checked(self, payload):
        logger.info('nameko | challenge_checked')
        token = payload.get('token')
        logger.info('nameko | challenge_checked.token | {token} '.format(token=token))
        result = payload.get('result')
        status = result.get('status')
        logger.info('nameko | challenge_checked.status | {status} '.format(status=status))
        logger.info('nameko | challenge_checked.result | {result} '.format(result=result))
