# lock-down-progress

- Sign up for a twitter account and then use the account to apply for a developer account
- Create a API key pair for twitter API
- Add the keys and access token to the environment variable
- `git clone https://github.com/mithunmanohar/lock-down-progress`

- `pip install pipenv` Tested with Python 3.7
- `pip env shell` to activate venv
-  Edit the [tweets_manager.py](https://github.com/mithunmanohar/lock-down-progress/blob/master/lock_down_progress/tweets_manager.py) with `start_date` and `end_date`
- Schedule a crontab to run the bot at the frequency you want

### Sample tweet by bot
![Sample tweet by bot](https://github.com/mithunmanohar/lock-down-progress/blob/master/sample_tweet.PNG)
