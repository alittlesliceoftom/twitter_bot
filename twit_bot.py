'''
Author: Tom O'Neill

Twit bot takes the text in a file pointed to by the config and posts it to the account in the secret keys.
'''

import tweepy , time , sys
import configparser

def get_config():
    ##config read
    configFile = 'config.ini'
    config = configparser.ConfigParser()
    config.read(configFile)
    values = dict(config.items('Keys'))
    access_key, consumer_secret, consumer_key, access_secret = [values.get(k) for k in ['access_key', 'consumer_secret', 'consumer_key', 'access_secret']]
    file = config['TweetText']['File']
    return access_key, consumer_secret, consumer_key, access_secret, file

#get config data
access_key, consumer_secret, consumer_key, access_secret, file = get_config()

#setup twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#read in messages
with open(file,'r') as f:
    lns = f.readlines()

for l in lns:
    if len(l) > 140:
        pass # replace with function to breakup and add ...
    else:
        api.update_status(status=l)
        print('tweeted:' + l)
        time.sleep(180)  # Tweet every 3 minutes

