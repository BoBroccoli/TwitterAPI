import tweepy
from textblob import TextBlob

consumer_key="im5hKrjeWU06oJiatrdc31k0z"
consumer_secret="CJVzWnGr4iLznpACYpWbw1k03nVEMROryd9AwDA6lTwjNKjCyg"

access_token="2975262631-6DPiZSbDv5dG8Gqrw2zMD7Tvd5BfV0Xn9XpeU71"
access_token_secret="a19zOu2IHhLwrofHvKWHKVAd4pVLUVA3cWerBN5BJXWup"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_eggs = api.search("eggs")

for egg in twitter_eggs:
	print(egg.text)
	analysis = TextBlob(egg.text)
	print(analysis.sentiment)