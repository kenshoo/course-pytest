from lib.server_basics import get_server_home_page, get_server_health


class TestServerBasics(object):
	def test_should_get_server_home_page():
		get_server_home_page()

		assert requests.get.assert_called_with(home_url)

	def test_should_get_server_healthcheck():
		get_server_health()

		assert requests.get.assert_called_with(f'{home_url}/healthcheck', headers=headers)
