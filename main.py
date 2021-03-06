# coding=utf-8
import json
import pyperclip as pyperclip
#pyperclip allows you to copy things to the keyboard
import requests

def user_id_call():
  # first api call-- getting user id
  getuser_url = "http://api.calendly.com/users/me"
  payload = ""
  url_headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjM1NTM1NDc0LCJqdGkiOiI2YWQzMjQ4Ny1jZDA2LTQ0MGEtYTYwYy1hMThlYjk4Zjc0YzEiLCJ1c2VyX3V1aWQiOiJHRkNBRDdTQlJRRkFSRjJBIn0.LVr64R4bzcQzxF9eafbzt3fvjwMaBFdn4nHFuAQvaRs'
}
  getuser_response = requests.request("GET", getuser_url, headers=url_headers, data=payload)
  getuser_json = getuser_response.json()
  return getuser_json


def event_url_call():
  #second api call -- getting event url
  getevent_url = "https://api.calendly.com/event_types?user=" + user_id_call()["resource"]["uri"]
  payload = ""
  event_headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjM1NTM1NDc0LCJqdGkiOiI2YWQzMjQ4Ny1jZDA2LTQ0MGEtYTYwYy1hMThlYjk4Zjc0YzEiLCJ1c2VyX3V1aWQiOiJHRkNBRDdTQlJRRkFSRjJBIn0.LVr64R4bzcQzxF9eafbzt3fvjwMaBFdn4nHFuAQvaRs'
  }
  getevent_response = requests.request("GET", getevent_url, headers=event_headers, data=payload)
  getevent_json = getevent_response.json()
  return getevent_json


def ideal_search():
  for item in event_url_call()["collection"]:
    if item["scheduling_url"] == "https://calendly.com/alison-metaview/30-min":
      return item["uri"]
#ideal_search() is what we'd use to change users later-- could fill in another recruiters' link
#url = "https://api.calendly.com/scheduling_links?owner=https://api.calendly.com/event_types/CCDI5Z3RHURRGXSV&owner_type=EventType&max_event_count=1"


def event_id_call():
  ideal_url = "https://api.calendly.com/scheduling_links?owner=" + ideal_search() + "&owner_type=EventType&max_event_count=1"#a little stuck on how to reference this dictionary in getevent_json, because
  payload = ""
  headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjM3MDA2MzAyLCJqdGkiOiI1ZjQ3NDVkZS0zNzY2LTRmOGQtODJjNi05ZWMyYmJlMDIzMTgiLCJ1c2VyX3V1aWQiOiJHRkNBRDdTQlJRRkFSRjJBIn0.w9Z9FZS2qA1LX4FR-6Mc93cpNGhzvSmlC-c37mFxrjo'
}
  #token -- to be stored somehow securely but currently in plain text
  response = requests.request("POST", ideal_url, headers=headers, data=payload)
  r = response.json()
  pyperclip.copy(r["resource"]["booking_url"])

def calendly_generator():
  user_id_call()
  event_url_call()
  event_id_call()

calendly_generator()


