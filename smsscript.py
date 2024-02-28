import requests
from contact_list_constants import contact_list
url = 'https://api.twilio.com/2010-04-01/Accounts/'
account_sid = ''
url += account_sid+"/Messages.json"
headers = {
  'Authorization': 'Basic QUNlNjM2OTA5YTAxMWM0ZmQ3NWRiMDgzMzFjMWEzZWI4YTphMzI5YWY0YmNkMTZiMTZmNjIxYTY5ZDZiZmYyNThmNA==',
  'Content-Type': 'application/x-www-form-urlencoded'
}

for contact in contact_list:
    payload = {
        'To': contact['number'],
        'From':'+18283830476',
        'Body': ' नमस्ते अभिभावक '+ contact['name'] + ' जी, आज स्कूल बंद रहेंगे'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
