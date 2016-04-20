import datetime
import time
import mysql.connector

def compute_score(distance, retweets, likes, time_tweeted, username, team_name):

	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()

	query = ("select MAX(retweets) as rt from " + team_name.lower() + "_tweets;")
	cursor.execute(query)
	max = 1
	for (rt) in cursor:
		max = rt[0]

	if max == 0:
		max = 1		
	max_retweets = float(max)
	virality_score = 1 - (float(retweets) / max_retweets)
	
	now = datetime.datetime.now()
	
	tdelta = now - time_tweeted
	seconds = tdelta.total_seconds()
	seconds_in_a_day = 86400
	time_score = float(seconds) / float(seconds_in_a_day)

	score = distance + virality_score + time_score
	
	cnx.commit()
	cnx.close()


	return viratily_score, time_score
