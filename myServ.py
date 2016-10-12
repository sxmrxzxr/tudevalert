from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient

import credentials as c
import myNumbers as n
import myResponses as m
import twilio.twiml

app = Flask(__name__)
client = TwilioRestClient(c.account_sid, c.auth_token)
n.on_open()
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

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)

n.on_close()
