import os
from settings import APP_TWEETS

def sort_tweets(team_name):
	tweetfile = open(os.path.join(APP_TWEETS, team_name.lower() + '_tweets.txt'), 'r')
	tweets = []
	for line in tweetfile:
		line_split = line.split(',')
		id = line_split[0]
		distance = line_split[1]
		tweet = {'id': str(id), 'distance': float(distance)}
		tweets.append(tweet)
	
	tweets.sort(key=lambda x: x['distance'], reverse=False)
	
	count = 0	
	ids = []
	while count < 10:
		tweet = tweets[count]
		
		ids.append(tweet['id'])
		count = count + 1
		
	tweetfile.close()
	return ids
