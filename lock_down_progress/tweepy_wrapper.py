# -*- coding: utf-8 -*-
import os
from tweepy import OAuthHandler, API

class TweepyWrapper(object):
    def __init__(self):
        o_auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        o_auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
        self.t_client = API(o_auth)
        
    
    def send_tweet(self, message):
        self.t_client.update_status(message)

if __name__ == '__main__':
    t = TweepyWrapper()
    t.send_tweet("COVID-19 India Lockdown Progress \U0001F449  Day 0")