import pytest
from app import app as current_app

@pytest.fixture()
def app():
	current_app.config.update({
		'TESTING': True
	})
	yield current_app

@pytest.fixture()
def client(app):
	return app.test_client()

division_tests = [
	[10,5,2.0],
	[5,2, 2.5],
	[7,2, 3.5]
]

@pytest.mark.parametrize('args', division_tests)
def test_division_route(client, args):
	a, b, expected = args
	response = client.get(f'/division?a={a}&b={b}')
	assert response.data == str(expected).encode("utf-8")

