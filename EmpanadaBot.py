import config
import random
import time
import tweepy

api_key = config.API_KEY
api_key_secret = config.API_KEY_SECRET
bearer_token = config.BEARER_TOKEN
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET

client = tweepy.Client(bearer_token, api_key, api_key_secret,
                       access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(
    api_key, api_key_secret, access_token, access_token_secret)

api = tweepy.API(auth)


def getRandomEmpanada():

    empanadas = ['de carne cortada a cuchillo', 'turca', 'caprese', 'de jamón y queso',
             'choclo', 'de acelga', 'de atún', 'santiagueña', 'salteña', 'de carne', 'de pollo', 'de carne con pasas', 'cuatro quesos', 'de vigilia', 'frita', 'tucumana', 'de camarón con queso', 'de pino', 'jujeña', 'mendocina', 'sanjuanina', 'catamarqueña', 'entrerriana', 'de cebolla y mozzarella', 'de chorizo', 'de entraña', 'de salchicha alemana con mostaza', 'de hongos a la provenzal', 'de humita', 'de ananá']

    tweet = "Tenés cara de empanada " + random.choice(empanadas) + "."

    return tweet


client_id = client.get_me().data.id

start_id = 1

initialization_resp = client.get_users_mentions(client_id)

if initialization_resp.data != None:
    start_id = initialization_resp.data[0].id


while True:
    response = client.get_users_mentions(client_id, since_id=start_id)

    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(
                    in_reply_to_tweet_id=tweet.id, text=getRandomEmpanada())
                start_id = tweet.id
            except Exception as error:
                print(error)

    time.sleep(5)
