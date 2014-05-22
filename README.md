twimail
=======
*THIS HACK IS WORK IN PROGRESS*

##Emails to Twilio and back

#What does it do?
The idea is that once every 6 hours with a CRONJOB this script will allow you to receive one or more SMSs with the titles of all your new emails

If you want to read an email you reply to the SMS with a number and you can get the full body of the email back.

Simple right?

#Cool I like the idea - What works?
It works for GMail and Gmail business *only* for now.

Once run the script or scheduled with cronjob like I do, it will  automatically check for fresh new emails. 
If succesful in finding fresh emails, it will email you a list of email subjects to ur given number in the ```main.py``` file.
Once an email has been detected as "fresh" twimail will label it as dispatched by applying a tag to it.
This way you don't get fresh new emails twice.

#What is planned?
Retrieve the text body of an email through SMS by giving an index to each email's subject you received through SMS.

#Pre Install Requirements
- [This library by charlierguo](https://github.com/charlierguo/gmail)
- Python 2.7+
- [Requests](http://docs.python-requests.org/en/latest/)

#Why this?
Sometimes you're in a different country with no wi-fi for a few hours or days and you still want to see if there are any crucial emails that you want to inspect




