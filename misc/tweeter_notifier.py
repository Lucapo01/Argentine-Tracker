import tweepy
import pandas as pd

consumer_key = "EjmxDsT5TXSvSWBP7LL6ULotz"
consumer_secret = "HDlBW3MTpTuT2vhplGEvVuoid8OTAulYo6F4sUmDxcypLsSEz8"
access_token = "1670909284777951233-MDjH2wfbioFgvolq2huFM3f2JUxV5K"
access_token_secret = "pSeNtLm3BZyheX5seBxHHZqAWF4EaJd71RxQvmApZGZIY"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))