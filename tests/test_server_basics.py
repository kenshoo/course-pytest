from mock import patch

from lib.server_basics import get_server_home_page, get_server_health


class TestServerBasics(object):
	def test_should_get_server_home_page(self):
		expected_home_url = "my_home"

		with patch('lib.server_basics.requests.get') as mock_get:
			with patch.dict('lib.globals.environ', dict(HOST=expected_home_url)):
				get_server_home_page()

				mock_get.assert_called_with(expected_home_url)

	def test_should_get_server_healthcheck(self):
		expected_home_url = "my_home"
		token = "****"
		expected_headers = {'Content-type': 'application/json',
				            'Accept': 'application/json',
				            'x-token': token}

		with patch('lib.server_basics.requests.get') as mock_get:
			with patch.dict('lib.globals.environ', dict(HOST=expected_home_url, TOKEN=token)):
				get_server_health()

				mock_get.assert_called_with(f'{expected_home_url}/healthcheck', headers=expected_headers)
