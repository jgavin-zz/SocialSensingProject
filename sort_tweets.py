import mysql.connector
import datetime

if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
	for team_name in teams:
		query = ("DELETE FROM " + team_name.lower() + "_top;")
		cursor.execute(query)

		tweets = []
		query = ('select id, score from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		for (id, score) in cursor:
			tweet = {'id': str(id), 'score': float(score)}
			tweets.append(tweet)
		tweets.sort(key=lambda x: x['score'], reverse=False)
	
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

	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Sorted tweets at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
