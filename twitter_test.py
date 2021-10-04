import tweepy,json
import time

access_token = '1928540977-pjQdrxZvmsTnps6rFVk3pOZRVNjPsRc5V4SXbA9'
access_token_secret = 'c576g05in3LIaHEZqhAiupP2Gh9Rem7ltj1QKZfh63vZI'
consumer_key = 'b1s7YjRWM0odDGvEHwoMzmNEw'
consumer_secret = 'w21WRFOWXDq06ibyixTujewyeDgJSP6Tba2jRjgRu2zvFaHKKl'

bb_id = '9695312'

start_time = time.time()
prev_time = start_time
curr_time = 0;

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def update_progress(prev_time, curr_time):
    curr_time = time.time()
    if curr_time-prev_time >= 5:
        print('Searching ...')
        prev_time = curr_time


tweet_list = []
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api = None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("OUTPUT/tweet.txt", "w")
        print(f'START >>> {start_time}')

    def on_status(self, status):
        tweet = status._json
        if tweet['user'].screen_name in 'billboard':
       # if not tweet['retweeted'] and 'RT @' not in tweet['text'] and '@billboard' not in tweet['text']:
            print('FOUND TWEET')
            self.file.write(json.dumps(tweet) + '\n')
            tweet_list.append(status)
            self.num_tweets+=1
            if self.num_tweets<10:
                return True
            else:
                return False
            self.file.close()
        update_progress(prev_time, curr_time)


# create streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)


# this line filters twiter streams to capture data
#stream.filter(track=['BTS'])
stream.filter(follow=[bb_id])

print(f'TOTAL RUN TIME >>>> {time.time() - start_time}')
