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

#create a list that will hold all subjects
subject_array = []
#iterate through each unread email
for unreadmail in unread:
#first fetch the actual messages
    unreadmail.fetch()
#check if the msg has been processed already
    if "twilio-d" in unreadmail.labels:
        print "skipping"
    else:
        #the message hasnt been twilio'd (marked as read)
        unreadmail.add_label("twilio-d")
        #only  give us the subject
        subject_array.append(unreadmail.subject)

#then we can send it to twilio who will then forward it to my email

payload = {'From':'+441277424151','To':'+447895445918','Body':'hi'}
print json.dumps(payload)
r = requests.post(furl, data=json.dumps(payload))
print r.text
