#!/usr/bin/python
import sys, traceback, os
import requests
import subprocess
import json
from datetime import datetime, timedelta
import ConfigParser

base_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config_file = base_folder + '/scripts/script.config'
webhook_url = ''
user = ''

def load_properties():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.optionxform = str
    config.read(config_file)
    global webhook_url, user
    webhook_url = config.get('webhook', 'url')
    user = config.get('users', 'id')


def send_to_slack(alert):
   # Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
    #slack_data = {'text': "{}".format(alert), "icon_emoji": ":robot_face:", "username": "monbot", "channel": "#home"}
    alert = "Hey <!{}>, it's Friday :smile:".format(user)
    slack_data = {'text': "{}".format(alert), "icon_emoji": ":robot_face:", "username": "monbot", "channel": "#home"}
    

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


if __name__ == "__main__":
    load_properties()
    send_to_slack('hello world')
