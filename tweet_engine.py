import datetime

tweet_file = open('tweets.txt', 'w')

tweet_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

tweet_file.close()
