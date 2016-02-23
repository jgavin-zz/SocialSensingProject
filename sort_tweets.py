import os
from settings import APP_TWEETS
import mysql.connector

def sort_tweets(team_name):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing')
	cursor = cnx.cursor()
	tweets = []
	query = ('select id, distance from ' + team_name.lower() + '_tweets;')
	cursor.execute(query)
	for (id, distance) in cursor:
		tweet = {'id': str(id), 'distance': float(distance)}
		tweets.append(tweet)
	tweets.sort(key=lambda x: x['distance'], reverse=False)
	
	count = 0	
	ids = []
	while count < 10:
		tweet = tweets[count]
		ids.append(tweet['id'])
		count = count + 1
		query = ("INSERT INTO " + team_name.lower() + "_top VALUES (" + str(tweet['id'])+ ");")
		cursor.execute(query)
	cnx.commit()
        cnx.close()
