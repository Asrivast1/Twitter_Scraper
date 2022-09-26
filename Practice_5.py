import pandas as pd
import twint
import tweepy

consumer_key = "*******" #Your API/Consumer key 
consumer_secret = "******" #Your API/Consumer Secret Key
access_token = "******"    #Your Access token key
access_token_secret = "*******" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

keywords = ['India', 'Bharat', 'Hindustaan', 
            'Hindustan', 'india', 'hindustaan', 'hindustaan', 
            'bharat', '#india', "#India", "#Bharat", "#bharat", 
            "#hindustaan", "#hindustan"]

no_of_tweets =10000000

try:

    for elements in keywords:

        #The number of tweets we want to retrieved from the search
        tweets = api.search_tweets(q=elements, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text] for tweet in tweets]

        #Creation of column list to rename the columns in the dataframe
        columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

        #Creation of Dataframe
        tweets_df = pd.DataFrame(attributes_container, columns=columns)

        #Saving to a csv file
        tweets_df.to_csv("tweet.csv", mode='a', index=False, header=False)

except BaseException as e:
    print('Status Failed On,',str(e))

