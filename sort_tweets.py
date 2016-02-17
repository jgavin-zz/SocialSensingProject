def sort_tweets(team_name):
	filename = "tweets/" + team_name.lower() + "_tweets.txt"
	file = open(filename, 'r')
	
	tweets = []
	for line in file:
		line_split = line.split(',')
		id = line_split[0]
		distance = line_split[1]
		tweet = {'id': str(id), 'distance': float(distance)}
		tweets.append(tweet)
	
	tweets.sort(key=lambda x: x['distance'], reverse=False)
	
	count = 0	
	ids = []
	while count < 10:
		tweet = tweets[count]
		
		ids.append(tweet['id'])
		print tweet['distance']
		count = count + 1
		
	return ids