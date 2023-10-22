CONTEXT:
1. Generating a scope from a CRM console.
2. Getting data from a job GET request. Ex: Salesforce Analytics.
3. Updating records from a PUT request.

Why?
API requests can be automated to reduce manual labor and enforce data consistency.

How?
Applications, especially formal business platforms like CRMs, often have APIs.
APIs allow developers and external users to send data between the platform and other, often unassociated, platforms.

What does this project do?
This project serves as a framework and step-by-step guide to begin sending requests to your target API.
This project considers a highly-structured API that involves "scopes".
Scopes allow users to generate a one-time authentication token to subsequently generate refresh and authentication/access tokens.
Many APIs do not require any form of token or only one authentication token, so requiring multiple tokens just to make one request can be confusing.

How do I use this project?
Begin by making the one-time authentication request.
You will likely be required to generate a scope in your platform's console. This will output a refresh token.
After you have acquired the refresh token, you are able to make PUT and GET requests.
