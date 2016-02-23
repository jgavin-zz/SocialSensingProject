import mysql.connector
from sort_tweets import sort_tweets

#cnx = mysql.connector.connect(user='root', password='bob',
#                              host='127.0.0.1',
#                              database='socialsensing')
#cursor = cnx.cursor()
#query = ("INSERT INTO bulls_tweets VALUES (701828926016851968,0.985294117647,CURRENT_TIMESTAMP);")
#cursor.execute(query)
#cnx.commit()
#cnx.close()


sort_tweets('bulls')
