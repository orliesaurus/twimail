twimail
=======
*THIS HACK IS WORK IN PROGRESS*

##Emails to Twilio and back


#Pre Install Requirements
- [This library by charlierguo](https://github.com/charlierguo/gmail)
- Python 2.7+
- [Requests](http://docs.python-requests.org/en/latest/)

#How to set up
Create a file called gmailvaraibles.py and create these variables
mylogin = "your@gmailusername"
mypassword = "yourpassword"
furl = "https://APIKEY:SecretKey@api.twilio.com/2010-04-01/Accounts/YOURACCID/Messages.json"
payload = {'From': '+SOMENUMBERSHERE', 'To': '+YOURPHONENUMBER'}
Replace your phone number and twilio number in the above obviously, 
and you're ready to go.

#What does it do?
The idea is that once every 6 hours with a CRONJOB this script will allow you to receive one or more SMSs with the titles of all your new emails

If you want to read an email you reply to the SMS with a number and you can get the full body of the email back.

Simple right?

#Cool I like the idea - What works?
It works for GMail and Gmail business *only* for now.

Once you run the script or as part of scheduled  job with cronjob (like I do), it will  automatically check for fresh new emails.

If succesful in finding fresh emails, it will email you a list of email subjects to ur given number in the ```main.py``` file.
Once an email has been detected as "fresh" twimail will label it as dispatched by applying a tag to it.
This way you don't get fresh new emails twice.

#What is planned?
Retrieve the text body of an email through SMS by giving an index to each email's subject you received through SMS.


#Why this?
Sometimes you're in a different country with no wi-fi for a few hours or days and you still want to see if there are any crucial emails that you want to inspect

#Help I'm stuck -OR- Hey I wanna help
Cool thanks for stopping by: open an issue or send a pull request! 

*made with <3 by orliesaurus*



