# c4_pushover
## What does c4pushover do?
### General Description
c4pushover is a python script that utilizes internet websites to do some work
as well as a *Control4* project in the target home.
Once the ground work connections are made, c4pushover makes
use of strings sent from the app, to a web site.
The web then determines the app target, user and app token key
to send the message to the target.
The target receives these *push* notifications, evaluates them,
and then acts upon the messages.
## Set-up
### pushover.net
Create a login to pushover dot net and pay for its use in your projects
Create an app token for your python app.
From this site, you will have a user token and an app token.
These key values are then contained in the auth_sec.py file in an Auth() class
having the local variables apptoken, usertoken. I do not place the copy of my
auth_sec.py file here for obvious reasons. They have *MY* token values in them.
### Control4 project
Have a licensed *Control4* controller and peoject in your home. Add the IFTTT app to the project from the app list.
Pay *ChowMain* for the app to be licensed in your C4 Project.
On the IFTTT icon under programming, set up the action for various **String** messages you expect to receive.
I use Logic detection on both the message title and message itself to determine validity.
Once this is set-up, you can then test the flow from python to your home with the push of a button **guidev branch** or the call of an
API **develop** branch.