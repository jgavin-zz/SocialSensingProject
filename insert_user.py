import mysql.connector
from mysql.connector import Error

def insert_user(email, password):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	query = ("INSERT IGNORE INTO users VALUES ('" + str(email) + "', '" + str(password) + "');")
	try:
		cursor.execute(query)
		cnx.commit()
		cnx.close()		
		return 'Registered successfully'
	except Error as e:
		
		return "mysql error: %s" % e
