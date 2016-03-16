#This code needs to compute initial centroids, cluster tweets, and then choose 1 tweet to keep out of each cluster
import mysql.connector
from compute_clusters import compute_clusters
from remove_tweets import remove_tweets
import datetime

if __name__ == '__main__':
	start = datetime.datetime.now()
        cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
			      charset='utf8',
                     	      use_unicode=True)
        cursor = cnx.cursor()
        teams = ['bulls', 'celtics', 'knicks', 'lakers', 'warriors']
        for team_name in teams:
#		query = ("delete t1 from " + team_name + "_tweets t1, " + team_name + "_tweets t2 where t1.date_inserted > t2.date_inserted and t1.id = t2.id")
#		print query
#		cursor.execute(query)
		query = ('select id, text from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		tweets = []
		tweets_to_delete = []
		for (id, text) in cursor:
			tweet = {'id': str(id), 'text': text}
			tweets.append(tweet)
		
		clusters = compute_clusters(tweets)
		remove_tweets(clusters, team_name)


	end = datetime.datetime.now()
	timeelapsed = (end - start).seconds
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Deleted duplicate tweets at " + str(datetime.datetime.now())+ ". It took " + str(timeelapsed) + " seconds." + '\n')
	logfile.close()

	cnx.commit()
	cnx.close()	

		
