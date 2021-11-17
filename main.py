# coding=utf-8
import json
import pyperclip as pyperclip
#pyperclip allows you to copy things to the keyboard
import requests
url = "https://api.calendly.com/scheduling_links?owner=https://api.calendly.com/event_types/CCDI5Z3RHURRGXSV&owner_type=EventType&max_event_count=1"
#url generated from get request in postman
payload = ""
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjM3MDA2MzAyLCJqdGkiOiI1ZjQ3NDVkZS0zNzY2LTRmOGQtODJjNi05ZWMyYmJlMDIzMTgiLCJ1c2VyX3V1aWQiOiJHRkNBRDdTQlJRRkFSRjJBIn0.w9Z9FZS2qA1LX4FR-6Mc93cpNGhzvSmlC-c37mFxrjo'
}

#token -- to be stored somehow securely but currently in plain text

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
#testing if response received info
r = response.json()
print(r["resource"]["booking_url"])
pyperclip.copy(r["resource"]["booking_url"])

#spam = pyperclip.paste()


