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


	#Compute virality ranks
	tweets.sort(key=lambda x: x['retweets'], reverse=False)
	count = 1	
	iterations = 1
	last_score = 0
	for tweet in tweets:
		if iterations == 1:
			iterations = iterations + 1
			last_score = tweet['retweets']
			tweet['virality_rank'] = count
		elif tweet['retweets'] == last_score:
			tweet['virality_rank'] = count
		else:
			count = count + 1
			tweet['virality_rank'] = count
			last_score = tweet['retweets']
		#print "Rank: " + str(tweet['virality_rank']) + ", Retweets: " + str(tweet['retweets'])
		
	virality_ranks = count
		
		
	#Compute time ranks
	tweets.sort(key=lambda x: x['date_tweeted'], reverse=False)
	count = 1
	for tweet in tweets:
		tweet['time_rank'] = count
		#print "Rank: " + str(tweet['time_rank']) + ", Time: " + str(tweet['date_tweeted'])
		count = count + 1
		
	time_ranks = count - 1
	
	#Compute relevance ranks
	tweets.sort(key=lambda x: x['distance'], reverse=True)
	count = 1	
	iterations = 1
	last_score = 0
	for tweet in tweets:
		if iterations == 1:
			iterations = iterations + 1
			last_score = tweet['distance']
			tweet['relevance_rank'] = count
		elif tweet['distance'] == last_score:
			tweet['relevance_rank'] = count
		else:
			count = count + 1
			tweet['relevance_rank'] = count
			last_score = tweet['distance']
		#print "Rank: " + str(tweet['relevance_rank']) + ", Distance: " + str(tweet['distance'])
		
	relevance_ranks = count
	
	print "Virality_ranks: " + str(virality_ranks) + "Time_ranks: " + str(time_ranks) + "Relevance_ranks: " + str(relevance_ranks)
		
	virality, time, relevance = get_preferences(email)
		
	cnx.commit()
	cnx.close()
	#return ids	
