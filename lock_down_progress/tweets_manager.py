# -*- coding: utf-8 -*-
import random
from datetime import datetime
from tweepy_wrapper import TweepyWrapper
from progress_bar_util import genrate_progress_bar

class TweetsManager(object):
    def __init__(self):
        self.twitter_client = TweepyWrapper()

    def _generate_tweet(self, day_count):
        tweet = "{0} Day {1}: COVID-19 India Lockdown Progress #21DaysLockdown".format('👉', day_count)
        return tweet
        
    def calc_day_progress(self, start_date):
        today = datetime.now()
        diff = today - start_date
        return diff.days

    def send_progress_tweet(self, start_date, end_date):
        total_days_lock_down = (end_date - start_date).days
        days_since_lock_down = t.calc_day_progress(start_date)
        tweet = self._generate_tweet(days_since_lock_down)
        genrate_progress_bar(days_since_lock_down, total_days_lock_down)
        print(tweet)
        image = 'progress_bar.jpg'
        self.twitter_client.send_tweet(tweet, image)



if __name__ == '__main__':
    t = TweetsManager()
    start_date = datetime(2020, 3, 24)
    end_date = datetime(2020, 4, 14)
    t.send_progress_tweet(start_date, end_date)