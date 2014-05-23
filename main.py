import gmail
import requests
import json
from gmailvariables import *

#login into gmail with a user and a password
g = gmail.login(mylogin, mypass)
#ready the payload

#set the filter/flag on all unread emails
unread = g.inbox().mail(unread=True)
# Iterate through all unread emails IDs
# fetch real emails from IDs
# print body of email

#create a list that will hold all subjects
def read_email():
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
    return subject_array

#Concatanate the email subjects with this "-" char
def concat_array(array):
    return "Subjects: " + " | ".join(array)


#uplifting this function to chunk into SMS size the message.
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


#hold the emails in a subj array
subj = read_email()
#use this function to format subjects
mypayload = concat_array(subj)
#send enough sms based on 140 char limit
sms_text = chunks(mypayload, 140)

for i in sms_text:
    payload['Body'] = i
    #then we can send it to twilio who will then forward it to my email
    #so let's prepare a payload and send it to twilio!
    r = requests.post(furl, data=payload)
