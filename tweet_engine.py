import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import mysql.connector

def compute_jaccard_distance(status, centroid):

	tweet_words = []
	tweet_split = status.text.split(' ')
	for word in tweet_split:
		tweet_words.append(word)
	len1 = len(tweet_words)	
	centroid_words = []
	for word in centroid:
		centroid_words.append(word)
	len2 = len(centroid_words)

	intersection = 0
	words_removed = 1
	
	while words_removed == 1:
		words_removed = 0
		for tweet_word in tweet_words:
			for centroid_word in centroid_words:
				if tweet_word == centroid_word:
					words_removed = 1
					intersection = intersection + 1				
					tweet_words.remove(tweet_word)
					centroid_words.remove(centroid_word)				
					break
					
	union = len1 + len2 - intersection
	return 1 - float(intersection)/float(union)

class TweetListener(StreamListener):
		
	def on_status(self, status):
		cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
		cursor = cnx.cursor()
		status.text = status.text.replace("'", '')
                status.text = status.text.replace('"', "")

		retweets = status.retweet_count
		likes = status.favorite_count
		username = status.user
		tweet_time = status.created_at
		print tweet_time
		
		bulls_distance = compute_jaccard_distance(status, bulls_words)
		lakers_distance = compute_jaccard_distance(status, lakers_words)
		knicks_distance = compute_jaccard_distance(status, knicks_words)
		celtics_distance = compute_jaccard_distance(status, celtics_words)
		warriors_distance = compute_jaccard_distance(status, warriors_words)		
		min_distance = min(bulls_distance, lakers_distance, knicks_distance, celtics_distance, warriors_distance)

		if min_distance < .985:
			if min_distance == bulls_distance:
				team_name = bulls
			elif min_distance == lakers_distance:
				team_name = lakers
			elif min_distance == knicks_distance:
				team_name = knicks
			elif min_distance == celtics_distance:
				team_name = celtics
			else:
				team_name = warriors
			query = ("INSERT INTO " + team_name + "_tweets VALUES (" + str(status.id) + ',"' + status.text + '",' + str(min_distance) + ",CURRENT_TIMESTAMP, STR_TO_DATE(" + tweet_time + ", '%Y-%m-%d %h:%i:%s'" + "), " + retweets + ", " + likes + ", '" + username + "', " + 0 + " );")
			print query
			cursor.execute(query)
		cnx.commit()
        cnx.close()
	def on_error(self, status):
		print(status)
		            
#Perform OAuth
auth = tweepy.OAuthHandler('FrTtImImzPxthrIjkTFrsUatY', 'cbPq4hNVEIj87LKcnP4XgCPAdPVc0By8ZVKH7WWVE5H9FS6ihb')
auth.set_access_token('635902588-6BuJRUYxXQ63vfmQYcP7auLAjkTgxaCRz70MwP5x', 'YsLyHMKLoUl47cCge1sBb7KfjDhg2wBbjWhBWm4VVOXtd')

#Connect to API
api = tweepy.API(auth)

bulls_file = open("dictionaries/bulls.json", 'r')
bulls_json = json.load(bulls_file)
bulls_words = bulls_json['players'] + bulls_json['staff'] + bulls_json['team_info'] + bulls_json['hashtags'] + bulls_json['accounts']
	
lakers_file = open("dictionaries/lakers.json", 'r')
lakers_json = json.load(lakers_file)
lakers_words = lakers_json['players'] + lakers_json['staff'] + lakers_json['team_info'] + lakers_json['hashtags'] + lakers_json['accounts']
	
knicks_file = open("dictionaries/knicks.json", 'r')
knicks_json = json.load(knicks_file)
knicks_words = knicks_json['players'] + knicks_json['staff'] + knicks_json['team_info'] + knicks_json['hashtags'] + knicks_json['accounts']
	
celtics_file = open("dictionaries/celtics.json", 'r')
celtics_json = json.load(celtics_file)
celtics_words = celtics_json['players'] + celtics_json['staff'] + celtics_json['team_info'] + celtics_json['hashtags'] + celtics_json['accounts']
	
warriors_file = open("dictionaries/warriors.json", 'r')
warriors_json = json.load(warriors_file)
warriors_words = warriors_json['players'] + warriors_json['staff'] + warriors_json['team_info'] + warriors_json['hashtags'] + warriors_json['accounts']


track = bulls_words + lakers_words + knicks_words + celtics_words + warriors_words

TweetStream = Stream(auth, TweetListener())
TweetStream.filter(track = track)

