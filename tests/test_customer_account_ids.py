from lib.customer_account_ids import get_customer_account_ids


class TestGetAcountID(object):
	def test_should_get_single_customer_id():
		customer_accounts = get_customer_account_ids(["Sherry-Stone"])

		assert customer_accounts["Sherry-Stone"] == 5

	def test_should_get_multiple_customer_ids():		
		customer_accounts = get_customer_account_ids(["Sherry-Stone", "Bobby-Jay"])

		assert customer_accounts["Sherry-Stone"] == 5
		assert customer_accounts["Bobby-Jay"] == 11