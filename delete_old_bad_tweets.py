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
	for team_name in teams:
		query = ("DELETE FROM " + team_name + "_tweets WHERE date_tweeted < (NOW() - INTERVAL 1 DAY)")
		cursor.execute(query)
		query = ("DELETE FROM " + team_name + "_tweets  WHERE id NOT IN (SELECT id FROM (SELECT id FROM " + team_name + "_tweets ORDER BY score ASC LIMIT 200 ) foo)")
#		print query
		cursor.execute(query)

	cnx.commit()
        cnx.close()
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Deleted tweets at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
