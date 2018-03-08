import sys, os

source_path = os.path.dirname(os.path.abspath(__file__))
print source_path
sys.path.insert(0, source_path + '/../')

from namekos import Service
import pytest


@pytest.fixture
def web_session(container_factory, web_config, web_session):
    container = container_factory(Service, web_config)
    container.start()
    return web_session


def test_get_metrics(web_session):
    rv = web_session.get('/metrics')
    from pprint import pprint
    pprint(rv.text)
    assert 'status' in rv.text, rv.text


def test_get_ping(web_session):
    rv = web_session.get('/ping')
    from pprint import pprint
    pprint(rv.text)
    assert 'pong' in rv.text, rv.text
