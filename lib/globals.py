from os import environ


def get_host():
	return environ['HOST']
	

def get_headers():
	return {'Content-type': 'application/json',
            'Accept': 'application/json',
            'x-token': environ['TOKEN']}
