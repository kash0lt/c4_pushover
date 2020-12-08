import http.client
import urllib
from push_sec import Auth
# push_sec contains the usertoken and api token for this python script to
# https://www.pushover.net


auth = Auth()
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
             urllib.parse.urlencode({
                 "token": auth.apitoken,
                 "user": auth.usertoken,
                 "message": "office light on",
                 "title": "jibo office light on"
             }), {"Content-type": "application/x-www-form-urlencoded"})
conn.getresponse()
