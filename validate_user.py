import mysql.connector

def validate_user(email, psw):
	cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
                              charset='utf8',
                              use_unicode=True)
	cursor = cnx.cursor()
	
	#Check if user exists
	query = ('select username from users;')
	cursor.execute(query)
	
	exists = 0
	users = ''
	for (username) in cursor:
		user = str(''.join(username))
		#users = users + user + ' '
		if user == str(email):
			exists = 1
			break
	#return users
		
	if exists == 1:	
		query = ("select password from users where username = '" + str(email) + "';")
		cursor.execute(query)
		cnx.commit()
		cnx.close()
		right_password = 0
		for (password) in cursor:
			p = str(''.join(password))
			if str(psw) == p:
				right_password = 1
		if right_password == 1:
			return "Logged in successfully"
		else:
			return "Wrong Password"
	else:
		return "User does not exist"
