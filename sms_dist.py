#todo: flesh out more methods that require twilio's api, separate from what will be added in flask server

import credentials as c
import numbers as n
from twilio.rest import TwilioRestClient

client = TwilioRestClient(c.account_sid, c.auth_token)

def send_alert(content):
	for number in n.l:
		alert = client.messages.create(body=content, to=number, from_=c.phone)
		print("Alert sent, " + alert.sid)


