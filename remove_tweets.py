import mysql.connector

def remove_tweets(clusters, team_name):

	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
        cursor = cnx.cursor()

	for cluster in clusters:
		keep_tweet = cluster.centroid
		for tweet in cluster.tweets:
			if tweet != keep_tweet:
							 
				query = ("DELETE FROM " + team_name + "_tweets WHERE id = " + "'" + keep_tweet['id'] + "'" )
				cursor.execute(query)

        cnx.commit()
        cnx.close()		
