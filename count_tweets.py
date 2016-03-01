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
        logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	for team_name in teams:
		query = ('select COUNT(*)as count from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		for (count) in cursor:
			count = int(count[0])		
			logfile.write("There were " + str(count) + " tweets in the " + team_name + " tweets table at " + str(datetime.datetime.now()) + ".\n")
			
	logfile.close()

	cnx.commit()
	cnx.close()	
	
