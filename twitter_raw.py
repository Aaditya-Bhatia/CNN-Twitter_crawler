'''author: Aaditya Bhatia
version: 1.0
Published Date: 7-01-2018
Functionality: This module consumes the API keys for Trump twitter account(https://twitter.com/realDonaldTrump)
Tweetpy provides access to the entire twitter RESTful API methods for Twitter
'''
import tweepy

def getTweets(public_account):
    #   Authenticating iva API keys
    auth = tweepy.OAuthHandler(	"dQ97sZq8yn74dDJmJ0S9OmPR0", "1hNk24ntlIvl9FIHAeqYxCYPnw9VYS6S40iqZwuOYA1n3ExVwf")
    auth.set_access_token("1373994198-7AvrHE1qbht8FAqmyO0Ekytc0vHYto0o10kZMuC", "NEAMzRRhlqJYiEOonsNs4sHpdfjZ6bbQmpmtSszUQCc2O")
    api = tweepy.API(auth)

    #   Getting the tweets
    public_tweets = api.user_timeline(public_account, count=25)

    #   Filtering URLs in the tweets and returning filtered Tweets
    tweets = []
    for iterNo, tweet in enumerate(public_tweets):
        tweets.append( tweet.text.split("https")[0])
        # print tweet.text.split("https")[0]              #   Debugging the results

    return tweets

if __name__ == '__main__':
    public_account = "realDonaldTrump"
    getTweets(public_account)