import mysql.connector

def fetch_top_tweets(team_name):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	ids = []
	query = ('select id from ' + team_name.lower() + '_top;')
	cursor.execute(query)
	for (id) in cursor:
		ids.append(int(''.join(id)))
		
	cnx.commit()
	cnx.close()
	return ids	
