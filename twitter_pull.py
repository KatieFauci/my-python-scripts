import tweepy


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


billboard_id = 9695312
user = tweepy.api.get_user('billboard')
#Create authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting access token and secret
auth.set_access_token(access_token, access_token_secret)

# create API object
api = tweepy.API(auth)

def get_tweet_ids():
    print('Get Tweet IDs')

def main():
    print('start')
    print(user.screen_name)
    print(user.followers_count)



if __name__ == "__main__":
    main()
    # get tweet ID's 
    # for every 100 tweet ID's make url