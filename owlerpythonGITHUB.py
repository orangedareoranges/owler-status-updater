import requests
import json
from base64 import b64encode

print("Hey, wanna submit a status?:")
x = input()
print("Your status is: " + x)

username = "INSERTUSERNAMEHERE"
password = "INSERTPASSWORDHERE"
requests.get("https://api.owler.cloud/v1/account/verify_credentials.json", auth=(username, password))
url = "https://api.owler.cloud/v1/statuses/update.json"
requests.post(f"{url}?status={x}", auth=(username, password))
print("Success! Check the public timeline.")
