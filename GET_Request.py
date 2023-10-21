'''
This script prompts a GET request to the server.

GET requests ask a server to return data. The data is often in a JSON format.

This script requests JSON-formatted data and returns the data in a CSV file.

Enter the information below in respect to the platform you are connecting.
'''


def RequestData():
    import pandas as pd
    import requests
    import json
    import time
    from io import StringIO
    clientid = "ENTER CLIENT ID HERE"
    clientsecret = "ENTER CLIENT SECRET HERE"
    refreshtoken = "ENTER TOKEN GENREATED FROM ONE-TIME SCRIPT HERE. AKA refreshtoken"
    url = f"https://FAKELINK.com/oauth/token?refresh_token={refreshtoken}&client_id={clientid}&client_secret={clientsecret}&grant_type=refresh_token"

    access_token_request = requests.post(url=url)
    if str(access_token_request) != "<Response [200]>":
        raise Exception("Non-200 HTTP response from server.")
    else:
        print("Access token successfully extracted.")

    clientid = "ENTER CLIENT ID HERE"
    workspaceid = "ENTER WORKSPACE ID HERE"
    viewid = "ENTER VIEW ID HERE"
    access_token_request_string = json.loads(access_token_request.text)
    accesstoken = access_token_request_string
    url1 = f"https://FAKELINK.com/restapi/workspaces/{workspaceid}/views/{viewid}/data"

    request_job = requests.get(url = url1, headers={"Authorization":accesstoken})
    if str(request_job) != "<Response [200]>":
        raise Exception("Non-200 HTTP response from server.")
    else:
        print("Job id succesfully extracted.")

    job_id_string = json.loads(request_job.text)

    job_id_dict = job_id_string["data"]
    job_id_final = job_id_dict["jobId"]

    time.sleep(10)
    crm_data = requests.get(f"https://FAKELINK.com/restapi/v2/bulk/workspaces/{workspaceid}/exportjobs/{job_id_final}/data",
                        headers={"Authorization":accesstoken})
    crm_export = StringIO(crm_data.content.decode("utf-8"))
    crm_export = pd.read_csv(crm_export, sep=",")
    crm_export.reset_index(drop=True, inplace=True)
    crm_export.to_csv("crm_export.csv", index=False)
RequestData()

