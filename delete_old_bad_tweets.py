import mysql.connector
import datetime

if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()	
	teams = ['bulls', 'celtics', 'knicks', 'lakers', 'warriors']
		
	tweets = []
	for team_name in teams:
		query = ('select id, date_tweeted, text from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		for (id, date_tweeted, text) in cursor:
			tweet = {'id': id, 'date_tweeted': date_tweeted, 'team_name': team_name, 'text': text}
			tweets.append(tweet)
#	for tweet in tweets:
#		if tweet['team_name'] == 'bulls':
#			print tweet['id']
#			print tweet['date_tweeted']
#			print tweet['text']
#			print "XXXXXXXXXXXXXXXXXXXXXX"
	rows_deleted = 0

	tweets = []
       	for team_name in teams:
		query = ('select id from ' + team_name.lower() + '_top;')
		cursor.execute(query)
		for (id) in cursor:
			tweets.append({'id': str(''.join(id)), 'team_name': team_name})
#	for tweet in tweets:
#		if tweet['team_name'] == 'bulls':
#			print tweet['id']			



	for team_name in teams:
		query = ("DELETE FROM " + team_name + "_tweets WHERE date_tweeted < (NOW() - INTERVAL 1 DAY);")
		rows_deleted = 	cursor.execute(query)
		query = ("DELETE FROM " + team_name + "_tweets  WHERE id NOT IN (SELECT id FROM (SELECT id FROM " + team_name + "_tweets ORDER BY score ASC LIMIT 200 ) foo);")
#		print query
		cursor.execute(query)

	rows_deleted = cursor
	cnx.commit()
        cnx.close()
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Deleted tweets " + str(rows_deleted) + " at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
