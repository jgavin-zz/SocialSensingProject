import mysql.connector
import mysql.connector.errors
import datetime
if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	tweetfile = open("/var/www/SocialSensingProject/tweets.txt", 'r')
	
	count = 0
	for query in tweetfile:
		cursor.execute(query)
		count = count + 1
	
	cnx.commit()
	cnx.close()
	open("/var/www/SocialSensingProject/tweets.txt", 'w').close()	
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Inserted " + str(count) + " tweets at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
