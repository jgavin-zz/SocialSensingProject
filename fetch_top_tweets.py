import mysql.connector
from get_preferences import get_preferences

def fetch_top_tweets(team_name, email):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	query = ('select id, distance, retweets, date_tweeted from ' + team_name.lower() + '_tweets;')
	cursor.execute(query)
	
	
	tweets = []
	for (id, distance, retweets, date_tweeted) in cursor:
		tweet = {'id': id, 'distance': distance, 'retweets': retweets, 'date_tweeted': date_tweeted}
		tweets.append(tweet)
		
	#sorted_by_virality = tweets.sort(key=lambda x: x['retweets'], reverse=False)
	#sorted_by_time = tweets.sort(key=lambda x: x['date_tweeted'], reverse=False)
	#sorted_by_relevance = tweets.sort(key=lambda x: x['distance'], reverse=False)
	tweets.sort(key=lambda x: x['retweets'], reverse=False)
	
	virality, time, relevance = get_preferences(email)
	
	for tweet in tweets:
		print tweet['retweets']
		
	cnx.commit()
	cnx.close()
	#return ids	
