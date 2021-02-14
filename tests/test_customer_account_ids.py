from types import SimpleNamespace
from mock import patch

from lib.customer_account_ids import get_customer_account_ids


class TestGetAcountID(object):
	def test_should_get_single_customer_id(self):
		url = "url"
		token = "****"
		response_fixture = SimpleNamespace(json=lambda: {'id': 5})

		with patch('lib.customer_account_ids.requests.get', return_value=response_fixture) as mock_get:
			with patch.dict('lib.globals.environ', dict(HOST=url, TOKEN=token)):
				customer_accounts = get_customer_account_ids(["Sherry-Stone"])

				assert customer_accounts["Sherry-Stone"] == 5

	def test_should_get_multiple_customer_ids(self):	
		url = "url"
		token = "****"
		response_fixture1 = SimpleNamespace(json=lambda: {'id': 5})
		response_fixture2 = SimpleNamespace(json=lambda: {'id': 11})

		with patch('lib.customer_account_ids.requests.get', side_effect= (response_fixture1, response_fixture2)) as mock_get:
			with patch.dict('lib.globals.environ', dict(HOST=url, TOKEN=token)):
				customer_accounts = get_customer_account_ids(["Sherry-Stone", "Bobby-Jay"])

				assert customer_accounts["Sherry-Stone"] == 5
				assert customer_accounts["Bobby-Jay"] == 11