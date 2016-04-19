import mysql.connector

def insert_user(email, password):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	try:
		query = ("INSERT IGNORE INTO users VALUES (" + str(email) + ',"' + str(password) + ");")
		return 1
	except:
		return 0