import json, socket, time

from psutil import cpu_percent, virtual_memory
from nameko.standalone.events import event_dispatcher
from settings import BROKER_URL

hostname = socket.gethostname()


def get_metrics():
    cpu = cpu_percent()
    ram = virtual_memory()
    return json.dumps(
        {
            'status': {
                'cpu': {
                    'percent': cpu
                },
                'ram': {
                    'percent': ram.percent,
                    'used': ram.used / (1024.0 * 1024),
                    'total': ram.total / (1024.0 * 1024),

                }
            },
            'hostname': hostname,
            'time': time.time() * 1000000  # nano seconds
        }
    )


def broadcast_event(service, event, payload, confirms=False):
    config = {
        'AMQP_URI': BROKER_URL
    }
    dispatcher = event_dispatcher(config, use_confirms=confirms)
    dispatcher(service, event, payload)
    return True
