import GetOldTweets3 as got

crit = got.manager.TweetCriteria().setUsername("billboard").setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(crit)[0]
print(tweet.text)