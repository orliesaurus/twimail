import gmail
import requests
import json
from gmailvariables import *

#login into gmail with a user and a password
g = gmail.login(mylogin, mypass)
head = {'content-type': 'application/json'}

#set the filter/flag on all unread emails
unread = g.inbox().mail(unread=True)
# Iterate through all unread emails IDs
# fetch real emails from IDs
# print body of email

subject_array = []
for unreadmail in unread:
    #unread[unreadmail].fetch()
    #print unread[unreadmail].body
    unreadmail.fetch()

    if "twilio-d" in unreadmail.labels:
        print "skipping"
    else:
        unreadmail.add_label("twilio-d")
        subject_array.append(unreadmail.subject)

payload = {'From':'+441277424151','To':'+447895445918','Body':'hi'}
print json.dumps(payload)
r = requests.post(furl, data=json.dumps(payload))
print r.url
print r.text
