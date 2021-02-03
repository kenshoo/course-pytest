import requests

from lib.globals import get_host, get_headers


def get_server_home_page():
	host = get_host()

	return requests.get(f"{host}")


def get_server_health():
	host = get_host()
	headers = get_headers()

	return requests.get(f"{host}/healthcheck", headers=headers)
