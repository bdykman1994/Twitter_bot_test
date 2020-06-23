import tweepy
from datetime import date

# Authenticate to Twitter
auth = tweepy.OAuthHandler("","")
auth.set_access_token("", "")

api = tweepy.API(auth)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

today = date.today()
api.update_status(f"The Current Date {today}")