from digilocker.connection import Connection
from digilocker.constants import ISSUED_DOC_ENDPOINT, FETCH_DOC_ENDPOINT


class Documents(object):
    def __init__(self):
        self.connection = Connection()

    def get_issued_document(self, access_token):
        headers = {
            "Authorization": "Bearer {0}".format(access_token)
        }
        # calling the digilocker get issued documents api
        return self.connection.make_request(ISSUED_DOC_ENDPOINT, "POST", headers=headers)

    def get_uploaded_document(self):
        pass

    def get_document(self, access_token, uri, file_format="PDF"):
        headers = {
            "Authorization": "Bearer {0}".format(access_token)
        }
        # calling the digilocker get documents api
        return self.connection.make_request("{}/{}".format(FETCH_DOC_ENDPOINT, uri), "POST", headers=headers)
