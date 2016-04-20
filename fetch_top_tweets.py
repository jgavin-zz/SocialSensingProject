import mysql.connector
from get_preferences import get_preferences

def fetch_top_tweets(team_name, email):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	query = ('select id, virality_rank, time_rank, relevance_rank from ' + team_name.lower() + '_tweets;')
	cursor.execute(query)
	
	
	tweets = []
	for (id, virality_rank, time_rank, relevance_rank) in cursor:
		tweet = {'id': id, 'virality_rank': virality_rank, 'time_rank': time_rank, 'relevance_rank': relevance_rank}
		tweets.append(tweet)
	
	#Get user preferences
	v, t, r = get_preferences(email)
	v_preference = int(v)
	t_preference = int(t)
	r_preference = int(r)
	
	#Compute scores from normalized rankings and preferences
	for tweet in tweets:
		tweet['virality_score'] = tweet['virality_rank'] * (v_preference + 1)
		tweet['time_score'] = tweet['time_rank'] * (t_preference + 1)
		tweet['relevance_score'] = tweet['relevance_rank'] * (r_preference + 1)
		
		tweet['score'] = tweet['virality_score'] + tweet['time_score'] + tweet['relevance_score']
		
	#Sort by score
	ids = []
	tweets.sort(key=lambda x: x['score'], reverse=True)
	
	count = 0
	for tweet in tweets:
		if count == 10:
			break
		else:
			ids.append(tweet['id'])
			count = count + 1
				
	cnx.commit()
	cnx.close()
	return ids	
