# encoding: utf-8
"""
This file contains the server.
"""
from __future__ import print_function

from os import path

from flask import Flask, request
from twilio.rest import TwilioRestClient

import myNumbers as myNum
import myResponses as myRep

if path.isfile('credentials.py') or path.isfile('credentials.pyc'):
    from . import credentials as c
else:
    from sys import stderr

    print('Credentials file not found', file=stderr)
    exit(1)

app = Flask(__name__)
client = TwilioRestClient(c.account_sid, c.auth_token)

muted = []

subs = myNum.on_open(c.subs_path)


def unsubscribed_sender(number, msg):
    """
    This method handles a message from an unsubscribed sender
    :param number: the phone number from which the message was sent
    :param msg: the message sent by number
    :return: the response 
    """
    if number in subs:
        return
    if msg == 'SUB':
        subs.append(number)
        return myRep.new_num
    if msg == 'MUTE':
        muted.append(number)
        return myRep.mute
    if msg == 'LISTEN':
        if number in muted:
            muted.remove(number)
            return myRep.listen
        else:
            return myRep.mute_fail
    return myRep.not_sub


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    The main method to run the server from '/'
    """
    from_num = request.values.get("From", None)
    from_msg = request.values.get("Body")
    alert_flag = False

    if from_num not in subs:
        message_body = unsubscribed_sender(from_num, from_msg)
    elif from_num in c.admins:
        message_body = myRep.build_alert(from_msg)
        alert_flag = True
    else:
        message_body = myRep.not_admin

    if alert_flag:
        for s in subs:
            client.messages.create(to=s, from_=c.phone, body=message_body)
    else:
        client.messages.create(to=from_num, from_=c.phone, body=message_body)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

myNum.on_close(subs, c.subs_path)
