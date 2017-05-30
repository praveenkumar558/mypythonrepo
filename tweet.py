import tweepy
auth = tweepy.OAuthHandler(customer-key, customer-secret)
auth.set_access_token(access-token, access-token-secret)
api = tweepy.API(auth)
user = api.get_user('twitterhandle')
print user.screen_name
print user.followers_count
tweet = "Your tweet content"
status = api.update_status(status=tweet)
