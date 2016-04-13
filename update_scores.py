import mysql.connector
import datetime
from compute_score import compute_score 

if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor(buffered=True)
	
	teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
	for team_name in teams:

		tweets = []
		query = ('select id, distance, retweets, likes, date_tweeted, username from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		count = 1
		new_scores = []
		for (id, distance, retweets, likes, time_tweeted, username) in cursor:
			logfile = open("/var/www/SocialSensingProject/score_log.txt", 'a')
        		logfile.write("Count:  " + str(count) + '\n')
        		logfile.close()
			count = count + 1
			new_score = {'id': id, 'score': compute_score(distance, retweets, likes, time_tweeted, username, team_name)}
			new_scores.append(new_score)	
		
		for score in new_scores:
			id = score['id']
			new_score = score['score']
			query = ("UPDATE " + team_name + "_tweets SET score=" + str(new_score) + " where id=" + id + ";")
			cursor.execute(query)
	cnx.commit()
	cnx.close()
	#logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
     #   logfile.write("Updated tweet scores at " + str(datetime.datetime.now())+ '\n')
      #  logfile.close()
