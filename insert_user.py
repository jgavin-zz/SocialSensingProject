import mysql.connector
from mysql.connector import Error

def insert_user(email, password):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	
	#Check if user already exists
	query = ('select username from users')
	cursor.execute(query)
	users = []
	for (username) in cursor:
		user = str(''.join(username))
		if user == str(email):
			return 0
	
	
	query = ("INSERT IGNORE INTO users VALUES ('" + str(email) + "', '" + str(password) + "');")
	try:
		cursor.execute(query)
		query = ("INSERT IGNORE INTO preferences VALUES ('" + str(email) + "', 0, 0, 0);")
		cnx.commit()
		cnx.close()		
		return 1
	except Error as e:		
		return 0
