import http.client
import urllib
from push_sec import Auth
# push_sec contains the usertoken and api token for this python script to
# https://www.pushover.net


class C4PushOver():
    def __init__(self):
        self.conn = http.client.HTTPSConnection("api.pushover.net:443")

    def OffLightOn(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": auth.apitoken,
                              "user": auth.usertoken,
                              "message": "office light on",
                              "title": "jibo office light on"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()

    def OffLightOff(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": auth.apitoken,
                              "user": auth.usertoken,
                              "message": "office light off",
                              "title": "jibo office light off"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()

    def OffRoomOff(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": auth.apitoken,
                              "user": auth.usertoken,
                              "message": "office room off",
                              "title": "jibo office room off"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()


auth = Auth()
c4pushover = C4PushOver()
c4pushover.OffRoomOff()
