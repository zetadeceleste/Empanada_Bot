# Empanada Bot
An experimental bot using Python3 Tweepy library.

## Installation

You can install Tweepy using the pip package manager.
```
pip3 install tweepy
pip3 install --upgrade tweepy
```

## Credentials

Next, we need to link our Twitter account to our Python script. Go to [Twitter](apps.twitter.com) and sign in with your account. Create a Twitter application and generate a API Key, API Key Secret, Bearer Token, Access Token, and Access Token Secret.
Check out this video to make sure you have all the necessary permissions and access -> https://www.youtube.com/watch?v=BdmUhQnPToM&ab_channel=CreepyD

Then store the credentials within variables in a config.py file at the same level as EmpanadaBot.py file

```
API_KEY = 'your consumer key'
API_KEY_SECRET = 'your consumer secrets'
BEARER_TOKEN = 'your bearer token'
ACCESS_TOKEN = 'your access token'
ACCESS_TOKEN_SECRET = 'your access token secret'
```

## Empanada Bot

This Bot is meant to:

- Replies an user who mentions it what kind of "empanada" (typical dish in Argentina) is.
