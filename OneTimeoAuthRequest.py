'''
This is a one-time authentication token.

You will likely need to create a scope to perform this action. Please refer to .README.

Execute this script to generate a refresh token.

You will use the refresh token to make other HTTP requests (GET, PUT, POST, etc) to the server.

Enter the information below in respect to the platform you are connecting.
'''

import json
import requests

clientid = "ENTER CLIENT ID HERE"
clientsecret = "ENTER CLIENT SECRET HERE"
token = "ENTER ONE-TIME TOKEN HERE"
url = f"https://FAKELINK.com/token?grant_type=authorization_code&client_id={clientid}&client_secret={clientsecret}&code={token}"

CRM_initial_token_request = requests.post(url=url)
if str(CRM_initial_token_request) != "<Response [200]>":
    raise Exception("Non-200 HTTP response from server.")
else:
    print("Initial token authorization process completed.")

CRM_initial_token_request_response = json.loads(CRM_initial_token_request.text)

refresh_token = CRM_initial_token_request_response["access_token"]
print("This is your refresh token : ", refresh_token)