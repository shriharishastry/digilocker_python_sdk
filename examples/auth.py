from digilocker.api import Digilocker

api = Digilocker("client_id", "client_secret", "redirect_uri")

# To get authorization URL
api.get_authorization_url("99999999", "ref_number")

# To get Access token
api.get_access_token("code")
