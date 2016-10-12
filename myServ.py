from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient

import credentials as c
import myNumbers as n
import myResponses as m
import twilio.twiml

app = Flask(__name__)
client = TwilioRestClient(c.account_sid, c.auth_token)

subs = []
muted = []

subs = n.on_open(subs, c.subs_path)
messageBody = " "

@app.route("/", methods=['GET', 'POST'])
def main():
	from_num = request.values.get("From", None)
	from_msg = request.values.get("Body")
	alert_flag = False

	if (from_num not in subs):
		if (from_msg == "SUB"):
			subs.append(from_num)
			messageBody = m.new_num
		#BEGIN UNTESTED CODE
		elif (from_msg == "MUTE"):
			muted.append(from_num)
			messageBody = m.mute
		elif (from_msg == "LISTEN"):
			if (from_num in muted):
				muted.remove(from_num)
				messageBody = m.listen
			else:
				messageBody = m.mute_fail
		#END UNTESTED CODE
		else:
			messageBody = m.not_sub
	elif (from_num in c.admins):
		messageBody = m.build_alert(from_msg)
		alert_flag = True
	else:
		messageBody = m.not_admin

	if (alert_flag):
		for s in subs:
			message = client.messages.create(to=s, from_=c.phone, body=messageBody)
	else:
		message = client.messages.create(to=from_num, from_=c.phone, body=messageBody)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)

n.on_close(subs, c.subs_path)
