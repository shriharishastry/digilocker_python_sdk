## Digilocker Partner API Python Client

Wrapper over the requests library for communicating with the Digilocker Partner 1.6  API.

API Documentation: [Digilocker 1.6 API](https://partners.digitallocker.gov.in/assets/img/digital_locker_authorized_partner_api_specification_v1.6.pdf)

Usage
-----

- Digilocker Auth flow
```bash
from digilocker.api import Digilocker

api = Digilocker("client_id", "client_secret", "redirect_uri")

# To get authorization URL
api.get_authorization_url("99999999", "ref_number")

# To get Access token
api.get_access_token("code")

```
