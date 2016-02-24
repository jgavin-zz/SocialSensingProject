import mysql.connector

#Define database variables
DATABASE_USER = 'root'
DATABASE_HOST = '127.0.0.1'
DATABASE_NAME = 'socialsensing'
DATABASE_PASSWORD = 'bob'

#Create connection to MySQL
cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST)
cursor = cnx.cursor()

###################################
## Create DB if it doesn't exist ##
###################################

createDB = (("CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET latin1") % (DATABASE_NAME))
cursor.execute(createDB)

#########################
## Switch to socialsensing DB ##
#########################

useDB = (("USE %s") % (DATABASE_NAME))
cursor.execute(useDB)

###########################
## Drop all tables first ##
###########################

#Bulls
dropTableQuery = ("DROP TABLE IF EXISTS bulls_tweets")
cursor.execute(dropTableQuery)
dropTableQuery = ("DROP TABLE IF EXISTS bulls_top")
cursor.execute(dropTableQuery)

#Celtics
dropTableQuery = ("DROP TABLE IF EXISTS celtics_tweets")
cursor.execute(dropTableQuery)
dropTableQuery = ("DROP TABLE IF EXISTS celtics_top")
cursor.execute(dropTableQuery)

#Lakers
dropTableQuery = ("DROP TABLE IF EXISTS lakers_tweets")
cursor.execute(dropTableQuery)
dropTableQuery = ("DROP TABLE IF EXISTS lakers_top")
cursor.execute(dropTableQuery)

#Knicks
dropTableQuery = ("DROP TABLE IF EXISTS knicks_tweets")
cursor.execute(dropTableQuery)
dropTableQuery = ("DROP TABLE IF EXISTS knicks_top")
cursor.execute(dropTableQuery)

#Warriors
dropTableQuery = ("DROP TABLE IF EXISTS warriors_tweets")
cursor.execute(dropTableQuery)
dropTableQuery = ("DROP TABLE IF EXISTS warriors_top")
cursor.execute(dropTableQuery)

########################
## Create tables next ##
########################

#bulls_tweets
createTableQuery = ('''CREATE TABLE bulls_tweets (
						id VARCHAR(20) NOT NULL,
						text VARCHAR(200) NOT NULL,
						distance double NOT NULL,
						date timestamp)'''
                    )
cursor.execute(createTableQuery)

#celtics_tweets
createTableQuery = ('''CREATE TABLE celtics_tweets (
                                                id VARCHAR(20) NOT NULL,
                                                text VARCHAR(200) NOT NULL,
                                                distance double NOT NULL,
                                                date timestamp)'''
                    )
cursor.execute(createTableQuery)

#lakers_tweets
createTableQuery = ('''CREATE TABLE lakers_tweets (
                                                id VARCHAR(20) NOT NULL,
                                                text VARCHAR(200) NOT NULL,
                                                distance double NOT NULL,
                                                date timestamp)'''
                    )
cursor.execute(createTableQuery)

#knicks_tweets
createTableQuery = ('''CREATE TABLE knicks_tweets (
                                                id VARCHAR(20) NOT NULL,
                                                text VARCHAR(200) NOT NULL,
                                                distance double NOT NULL,
                                                date timestamp)'''
                    )
cursor.execute(createTableQuery)

#warriors_tweets
createTableQuery = ('''CREATE TABLE warriors_tweets (
                                                id VARCHAR(20) NOT NULL,
                                                text VARCHAR(200) NOT NULL,
                                                distance double NOT NULL,
                                                date timestamp)'''
                    )
cursor.execute(createTableQuery)

#bulls_top
createTableQuery = ('''CREATE TABLE bulls_top (
                                                id VARCHAR(20) NOT NULL
                                              )'''
                    )
cursor.execute(createTableQuery)

#celtics_top
createTableQuery = ('''CREATE TABLE celtics_top (
                                                id VARCHAR(20) NOT NULL
                                              )'''
                    )
cursor.execute(createTableQuery)

#lakers_top
createTableQuery = ('''CREATE TABLE lakers_top (
                                                id VARCHAR(20) NOT NULL
                                              )'''
                    )
cursor.execute(createTableQuery)

#knicks_top
createTableQuery = ('''CREATE TABLE knicks_top (
                                                id VARCHAR(20) NOT NULL
                                              )'''
                    )
cursor.execute(createTableQuery)

#warriors_top
createTableQuery = ('''CREATE TABLE warriors_top (
                                                id VARCHAR(20) NOT NULL
                                              )'''
                    )
cursor.execute(createTableQuery)

#Commit the data and close the connection to MySQL
cnx.commit()
cnx.close()
