import hashlib

from datetime import datetime
from pytz import timezone
from urllib.parse import urlencode

from digilocker.constants import AUTH_ENDPOINT, ACCOUNT_VERIFY, ACCESS_TOKEN_URL
from  digilocker.connection import Connection


class Digilocker(object):
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.connection = Connection()

    def get_authorization_url(self, mobile_number, ref_num):
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "state": ref_num
        }
        return "{}?{}".format(AUTH_ENDPOINT, urlencode(params))

    def get_access_token(self, code):
        request_body = {
            "code": code,
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri
        }
        return self.connection.make_request(ACCESS_TOKEN_URL, "POST", data=request_body)

    def account_exists(self, mobile_number):
        timestamp = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Kolkata')).strftime('%s')
        app_hash = hashlib.sha256(
            "{}{}{}{}".format(self.client_secret, self.client_id, mobile_number, timestamp)
        ).hexdigest()
        request_body = {
            "mobile": mobile_number,
            "hmac": app_hash,
            "ts": timestamp,
            "clientid": self.client_id
        }
        return self.connection.make_request(ACCOUNT_VERIFY, "POST", request_body)


