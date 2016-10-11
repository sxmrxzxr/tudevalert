from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient

import credentials as c
import myNumbers as n
import twilio.twiml

app = Flask(__name__)
client = TwilioRestClient(c.account_sid, c.auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls with a simple text message."""

	from_num = request.values.get("From", None)
	print(from_num)

	if from_num in n.admins:
		adminAlert = request.values.get("Body")
		messageBody = "TUDevAlert: " + str(adminAlert) + ". Avoid the area. Area is safe." 

		for num in n.subs:
			message = client.messages.create(to=num, from_=c.phone, body=messageBody)
 	else:
		resp = twilio.twiml.Response()
		resp.message("Hello, mobile monkey")
		return str(resp)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)
