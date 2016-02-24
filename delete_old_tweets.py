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
		query = ("DELETE FROM " + team_name + "_tweets WHERE date < (NOW() - INTERVAL 1 DAY)")
		cursor.execute(query)

	cnx.commit()
        cnx.close()
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Deleted tweets at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
