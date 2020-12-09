import http.client
import urllib
from tkinter import *
import os
from push_sec import Auth
# push_sec contains the usertoken and api token for this python script to access
# https://www.pushover.net
# The class is simple with members apitoken, which is the API token given from pushover.net when the app was registered
# and usertoken, which is the registered user token from pushover.net. Instanciate an instance of this class Auth() to
# access these members.


class C4PushOver():
    def __init__(self, authref):
        self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.apiToken = authref.apitoken
        self.userToken = authref.usertoken

    def OffLightOn(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office light on",
                              "title": "jibo office light on"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()

    def OffLightOff(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office light off",
                              "title": "jibo office light off"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()

    def OffRoomOff(self):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office room off",
                              "title": "jibo office room off"
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()


mainprog = Tk()
mainprog.title("Gui Office Control")
mainprog.iconbitmap(os.path.join(os.path.dirname(__file__), 'c4_pushover.ico'))
mainprog.geometry("400x400")
c4pushover = C4PushOver(Auth())
mainprog.mainloop()
