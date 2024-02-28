import requests
from contact_list_constants import contact_list
url = 'https://api.twilio.com/2010-04-01/Accounts/'
account_sid = 'ACe636909a011c4fd75db08331c1a3eb8a'
auth_token = '[a329af4bcd16b16f621a69d6bff258f4]'
url += account_sid+"/Messages.json"
headers = {
  'Authorization': 'Basic QUNlNjM2OTA5YTAxMWM0ZmQ3NWRiMDgzMzFjMWEzZWI4YTphMzI5YWY0YmNkMTZiMTZmNjIxYTY5ZDZiZmYyNThmNA==',
  'Content-Type': 'application/x-www-form-urlencoded'
}

for contact in contact_list:
    payload = {
        'To': contact['number'],
        'From':'+18283830476',
        'Body': ' Hello My name is '+ contact['name']
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


import requests

url = "https://api.twilio.com/2010-04-01/Accounts/ACe636909a011c4fd75db08331c1a3eb8a/Messages.json"

payload='To=%2B917355438382&From=%2B18283830476&Body=Hello%20I%20am%20Prashant'

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


