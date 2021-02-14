import requests

from lib.globals import get_host, get_headers


def get_customer_account_ids(customers):
	return {customer: _get_customer_accounts(customer) for customer in customers}


def _get_customer_accounts(customer):
	host = get_host()
	headers = get_headers()

	response = requests.get(f"{host}/customer/{customer}", headers=headers)
	return response.json()['id']