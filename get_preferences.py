import mysql.connector

def get_preferences(email):
	
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	query = ("select virality, time, relevance from preferences where username='" + email + "';")
	cursor.execute(query)
	new_scores = []
	for (virality, time, relevance) in cursor:
		v = str(virality)
		t = str(time)
		r = str(relevance)
	print v, t, r