#This code needs to compute initial centroids, cluster tweets, and then choose 1 tweet to keep out of each cluster
import mysql.connector
from compute_clusters import compute_clusters
if __name__ == '__main__':
        cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
			      charset='utf8',
                     	      use_unicode=True)
        cursor = cnx.cursor()
        teams = ['bulls', 'celtics', 'knicks', 'lakers', 'warriors']
        for team_name in teams:
		query = ('select id, text from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		tweets = []
		tweets_to_delete = []
		for (id, text) in cursor:
			tweet = {'id': str(id), 'text': text}
			tweets.append(tweet)
		
		clusters = compute_clusters(tweets)
		#remove_tweets(clusters)

	cnx.commit()
	cnx.close()	

		
