import mysql.connector


def compute_jaccard_distance(status1, status2):

	tweet1_words = []
	tweet1_split = status1.split(' ')
	for word in tweet1_split:
		tweet1_words.append(word)
	len1 = len(tweet1_words)
	
	tweet2_words = []
        tweet2_split = status2.split(' ')
        for word in tweet2_split:
                tweet2_words.append(word)
	len2 = len(tweet2_words)
	
	intersection = 0
	words_removed = 1
	
	while words_removed == 1:
		words_removed = 0
		for tweet1_word in tweet1_words:
			for tweet2_word in tweet2_words:
				if tweet1_word == tweet2_word:
					words_removed = 1
					intersection = intersection + 1				
					tweet1_words.remove(tweet1_word)
					tweet2_words.remove(tweet2_word)				
					break
					
	union = len1 + len2 - intersection
	return 1 - float(intersection)/float(union)

if __name__ == '__main__':
        cnx = mysql.connector.connect(user='root', password='bob',
                              host='127.0.0.1',
                              database='socialsensing',
			      charset='utf8',
                     	      use_unicode=True)
        cursor = cnx.cursor()
        teams = ['bulls', 'celtics', 'knicks', 'lakers', 'warriors']
        for team_name in teams:
		query = ('select id, text from ' + team_name.lower() + '_tweets;')
		cursor.execute(query)
		tweets = []
		tweets_to_delete = []
		for (id, text) in cursor:
			tweet = {'id': str(id), 'text': text}
			tweets.append(tweet)
		for tweet1 in tweets:
			for tweet2 in tweets:
				distance = compute_jaccard_distance(tweet1['text'], tweet2['text'])
				if distance < .1 and tweet1['id'] != tweet2['id']:
					print tweet1['text']
					print tweet2['text']		

	cnx.commit()
	cnx.close()	

		
