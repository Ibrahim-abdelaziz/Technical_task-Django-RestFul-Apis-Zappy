import os
import time
from slackclient import SlackClient


slack_token = os.environ['jblfEP1xZPq0VPh91PFTLIzQ']
sc = SlackClient(slack_token)
if sc.rtm_connect():
    while sc.server.connected is True:
        print(sc.rtm_read())
        time.sleep(3)
else:
    print("Connection Failed")

