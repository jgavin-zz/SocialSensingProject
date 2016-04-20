import mysql.connector
import datetime

if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor(buffered=True)
	
	teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
	for team_name in teams:

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
					
		relevance_ranks = count
		
		#Normalize to 1-1000 range	
		virality_multiplier = float(1000/float(virality_ranks))
		time_multiplier = float(1000/float(time_ranks))
		relevance_multiplier = float(1000/float(relevance_ranks))
	
		#Compute scores from normalized rankings
		for tweet in tweets:
			tweet['virality_rank'] = float(tweet['virality_rank'] * virality_multiplier)
			tweet['time_rank'] = float(tweet['time_rank'] * time_multiplier)
			tweet['relevance_rank'] = float(tweet['relevance_rank'] * relevance_multiplier)
		
			tweet['score'] = tweet['virality_rank'] + tweet['time_rank'] + tweet['relevance_rank']	
		
			query = ("UPDATE " + team_name + "_tweets SET score=" + str(tweet['score']) + ", virality_rank=" + str(tweet['virality_rank']) + ", time_score=" + str(tweet['time_rank']) + ", relevance_rank=" + str(tweet['relevance_rank']) + " where id=" + tweet['id'] + ";")
			cursor.execute(query)
			
			
	cnx.commit()
	cnx.close()
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Updated tweet scores at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
