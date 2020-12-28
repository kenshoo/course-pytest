from operator import itemgetter
from ftplib import FTP, Error as FTPError

from retrying import retry, RetryError

from app.conf import AppConfiguration as app_conf
from app.lib.globals import RETRY_PARAMS
from app.lib.exceptions import UnavailableFTPServer


def is_ftp_error(error):
    return isinstance(error, FTPError)


_get_ftp_details = itemgetter('address', 'user', 'password')


class FTPBucket(object):
    def __init__(self):
        self.address, self.user, self.passwd = _get_ftp_details(app_conf.conf['ftp_access'])

    def put(self, file_name, file):
        try:
            self._put(file_name, file)
        except RetryError:
            raise UnavailableFTPServer

    @retry(retry_on_exception=is_ftp_error, wrap_exception=True, **RETRY_PARAMS)
    def _put(self, file_name, file):
        with FTP(self.address) as ftp:
            ftp.login(self.user, self.passwd)
            ftp.storbinary(file_name, file)