import json
import mysql.connector

def fetch_all_tweets():
#if __name__ == '__main__':
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
	tweets = {'bulls': [], 'celtics': [], 'lakers': [], 'knicks': [], 'warriors': []}
	for team_name in teams:
		query = ('select id from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		for (id) in cursor:
			tweets[team_name].append(''.join(id))
			
	cnx.commit()
	cnx.close()
	return json.dumps(tweets)
	#return tweets
	
