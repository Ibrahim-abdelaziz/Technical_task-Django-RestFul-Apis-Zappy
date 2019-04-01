from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests
import twitter


api = twitter.Api(consumer_key='FILL-ME-IN',
  consumer_secret='FILL-ME-IN',
  access_token_key='FILL-ME-IN',
  access_token_secret='FILL-ME-IN')
print(api.VerifyCredentials())
help(api.GetUserTimeline)


auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(token, token_secret)

stream = Stream(auth, listener)
stream.filter(track=['festivus'])


