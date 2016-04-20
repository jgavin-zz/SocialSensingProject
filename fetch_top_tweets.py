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

	tweets.sort(key=lambda x: x['retweets'], reverse=True)
	count = 1
	for tweet in tweets:
		tweet['virality_rank'] = count
		count = count + 1
		print "Rank: " str(tweet['virality_rank']) + ", Retweets: " + str(tweet['retweets'])
		
		
	virality, time, relevance = get_preferences(email)
		
	cnx.commit()
	cnx.close()
	#return ids	
