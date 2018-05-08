import dateutil
import tweepy
from datetime import *
from dateutil.relativedelta import *
from secrets import *

# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

# Construct the API instance
api = tweepy.API(auth) # create an API object

FIRST_PC = datetime(2017, 2, 16)
TODAY = date.today()

delta = relativedelta(TODAY, FIRST_PC)

years = delta.years
months = delta.months
days = delta.days

if years == 1:
    syears = ""
else:
    syears = "s"
if months == 1:
    smonths = ""
else:
    smonths = "s"
if days == 1:
    sdays = ""
else:
    sdays = "s"

tweet = "It has been {} year{}, {} month{}, and {} day{} since @realDonaldTrump held a press conference. @PressSec #MAGA"

formatted_tweet = tweet.format(delta.years, syears, delta.months, smonths, delta.days, sdays)

api.update_status(formatted_tweet)
