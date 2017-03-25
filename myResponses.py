# encoding: utf-8
"""
This file exists for the purpose of exporting responses
"""
new_num = "Thanks for subscribing to TUDevAlert!"
not_sub = "You have reached TUDevAlert! Text 'SUB' if you wish to subscribe for text alerts."
mute = "You have muted TUDevAlert, remember to text 'UNMUTE' when you're ready to receive alerts."
listen = "You have unmuted TUDevAlert, welcome back!"
mute_fail = "You have not currently muted TUDevAlert"
not_admin = "We appreciate the message, but only approved numbers are allowed to submit alerts."


def build_alert(msg):
    """
    This method builds and alert to be broadcast
    :param msg: the custom message to send out
    :return: the constructed message
    """
    return "TUDevAlert: " + str(msg) + ". Avoid the area. Area is safe."
