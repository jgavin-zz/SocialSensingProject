import mysql.connector
import json
def update_retweets(data):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
	for team_name in teams:
		tweets = data[team_name]
		for tweet in tweets:
			id = tweet['id']
			retweets = tweet['retweets']
			likes = tweet['likes']

			query = ("UPDATE " + team_name + "_tweets SET retweets=" + str(retweets) + " where id=" + str(id) + ";")
			cursor.execute(query)

	cnx.commit()
	cnx.close()
		
