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
        self.title = "c4_pushover Python"

    def OffLightOn(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office light on",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()

    def OffLightOff(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office light off",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()

    def OffRoomOff(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "office room off",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()

    def OffCountry(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "iheartcountry",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()

    def OffTradCountry(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "pandora country",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()

    def OffChristmas(self):
        # self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.apiToken,
                              "user": self.userToken,
                              "message": "iheartchristmas",
                              "title": self.title
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        r1 = self.conn.getresponse()
        print(r1.status, r1.reason)
        r1Data = r1.read()
        print(r1Data)
        # self.conn.close()


mainprog = Tk()
mainprog.title("Gui Office Control")
mainprog.iconbitmap(os.path.join(os.path.dirname(__file__), 'c4_pushover.ico'))
mainprog.geometry("300x200")
c4pushover = C4PushOver(Auth())
m_offOn = Button(mainprog, text="Office Light On", command=c4pushover.OffLightOn)
m_offOn.grid(row=0, column=1, padx=60, ipadx=40)
m_offOff = Button(mainprog, text="Office Light Off", command=c4pushover.OffLightOff)
m_offOff.grid(row=1, column=1, padx=60, ipadx=40)
m_offCountry = Button(mainprog, text="Office IheartCountry", command=c4pushover.OffCountry)
m_offCountry.grid(row=2, column=1, padx=60, ipadx=40)
m_offTradCountry = Button(mainprog, text="Office PandoraCountry", command=c4pushover.OffTradCountry)
m_offTradCountry.grid(row=3, column=1, padx=60, ipadx=40)
m_offChristmas = Button(mainprog, text="Office IheartChristmas", command=c4pushover.OffChristmas)
m_offChristmas.grid(row=4, column=1, padx=60, ipadx=40)
m_OfficeOff = Button(mainprog, text="Office room off", command=c4pushover.OffRoomOff)
m_OfficeOff.grid(row=5, column=1, padx=60, ipadx=40)
mainprog.mainloop()
c4pushover.conn.close()
