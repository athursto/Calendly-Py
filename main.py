# coding=utf-8

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
r = response.json()
#ok clearly I need to do something to make "response" readable, but what? is it
pyperclip.copy(r["response"]["booking_url"])
#response is working fine
# pyperclip.copy('The text to be copied to the clipboard.')
# pyperclip.copy(response.booking_url)
#pyperclip.copy(["response"]["booking_url"])
#how to access response...
spam = pyperclip.paste()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
