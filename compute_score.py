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
	max = 0
	for (rt) in cursor:
		max = rt[0]
	
	max_retweets = float(max)
	virality_score = 1 - (float(retweets) / max_retweets)
	
	now = datetime.datetime.now()
	
#	tweet_time = datetime.datetime.strptime(time_tweeted, '%Y-%m-%d %I:%M')
	tdelta = now - time_tweeted
	seconds = tdelta.total_seconds()
	seconds_in_a_day = 86400
	time_score = float(seconds) / float(seconds_in_a_day)

	score = distance + virality_score + time_score

	logfile = open("/var/www/SocialSensingProject/score_log.txt", 'a')
	logfile.write("Distance: " + str(distance)+ '\n')
	logfile.write("Virality score: " + str(virality_score)+ '\n')
	logfile.write("Time Score: " + str(time_score)+ '\n')
	logfile.write("Total score: " + str(score)+ '\n')
	logfile.write("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
	logfile.close()


	return score
