from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient

import credentials as c
import myNumbers as n
import myResponses as m
import twilio.twiml

app = Flask(__name__)
client = TwilioRestClient(c.account_sid, c.auth_token)
messageBody = " "

@app.route("/", methods=['GET', 'POST'])
def main():
	from_num = request.values.get("From", None)
	from_msg = request.values.get("Body")
	print(from_num)

	if (from_num not in n.subs):
		if (from_msg == "SUB"):
			n.subs.append(from_num)
			messageBody = m.new_num
		else:
			messageBody = m.not_sub
	elif (from_num in n.admins):
		messageBody = m.build_alert(from_msg)
	else:
		messageBody = m.not_admin

	message = client.messages.create(to=from_num, from_=c.phone, body=messageBody)
	#if from_num not in n.subs:

	#	if (newNumMsg == "SUB"):
	#		n.subs.append(newNumMsg)
	#		messageBody = "Thanks for subscribing to TUDevAlert!"
	#		message = client.messages.create(to=from_num, from_=c.phone, body=messageBody)
	#	else:
	#		messageBody = "You've reached the TUDevAlert phone number, text 'SUB' if you wish to subscribe to alerts"
	#		message = client.messages.create(to=from_num, from_=c.phone, body=messageBody)

#	if from_num in n.admins:
#		adminAlert = request.values.get("Body")
#		messageBody = "TUDevAlert: " + str(adminAlert) + ". Avoid the area. Area is safe." 
#
#		for num in n.subs:
#			message = client.messages.create(to=num, from_=c.phone, body=messageBody)
 #	else:
#		resp = twilio.twiml.Response()
#		resp.message("We appreciate the thought, but only TUDev Officers are allowed to send alerts.")
#		return str(resp)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)
