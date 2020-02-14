# URL endpoints that are used to communicate with digilocker

BASE_URL = "https://api.digitallocker.gov.in/public/oauth2/1"
ACCOUNT_BASE_URL = "https://api.digitallocker.gov.in/public/account/1"

AUTH_ENDPOINT = "{}/authorize".format(BASE_URL)
ISSUED_DOC_ENDPOINT = "{}/files/issued".format(BASE_URL)
ACCESS_TOKEN_URL = "{}/token".format(BASE_URL)
FETCH_DOC_ENDPOINT = "{}/file".format(BASE_URL)
ACCOUNT_VERIFY = "{}/verify".format(ACCOUNT_BASE_URL)
