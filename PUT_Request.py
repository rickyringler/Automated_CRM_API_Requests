'''
This script prompts a PUT request to the server.

PUT requests ask a server to PARTIALLY update a record.

This script requests converts a CSV file into a JSON object to iterate a request for each record.

Systems often offer mass-update requests where you can update mulltiple records from one dataset,
but this can be risky and may prompt the request to fail if bad data is being stored.

Enter the information below in respect to the platform you are connecting.
'''

def PUTData():
    import requests
    import pandas as pd
    import json

    clientid = "ENTER CLIENT ID HERE"
    clientsecret = "ENTER CLIENT SECRET HERE"
    refreshtoken = "ENTER TOKEN GENREATED FROM ONE-TIME SCRIPT HERE. AKA refreshtoken"
    payload = pd.read_csv("ENTER THE DATA YOU WANT TO USE TO UPDATE THE PLATFORM HERE.csv")
    url = f"https://FAKELINK/oauth/token?refresh_token={refreshtoken}&client_id={clientid}&client_secret={clientsecret}&grant_type=refresh_token"

    access_token_request = requests.post(url=url, headers={
        "Authorization": refreshtoken})
    if str(access_token_request) != "<Response [200]>":
        raise Exception("Non-200 HTTP response from server.")
    else:
        print("Access token successfully extracted.")

    access_token_string = json.loads(access_token_request.text)
    access_token = access_token_string["access_token"]

    for payload_row in payload.to_dict(orient="records"):

            payload_record = str(payload_row["id"])
            payload_id = payload["id"]
            payload_address = payload["address"]

            payload = { "data": [{"customer_account_id": payload_id, "customer_address":payload_address}]}
            payload_final = json.dumps(payload)

            put_request = requests.put(url=url, data=payload_final, headers={"Authorization": access_token})

            print(put_request.text)
            if str(put_request) != "<Response [200]>":
                raise Exception(f"This customer's values could not be updated {payload_id}.")
            else:
                print(f"Customer {payload_id}'s values were updated with {payload_address}")
PUTData()