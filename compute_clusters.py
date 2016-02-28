#This code needs to compute tweets by iterating over tweets, creating clusters by splitting on 
#a certain diameter

class Cluster:
	def __init__(self, c):
		self.centroid = c
		self.tweets = [c]
def compute__distance(status1, status2):

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

def compute_clusters(tweets):

	clusters = []
	firstCluster = Cluster(tweets[0])
	clusters.append(firstCluster)
	
	for i in range(len(tweets)):
		if i == 0:
			continue;
		min_distance = 1
		tweet = tweets[i]
		closest_cluster = clusters[0]
		for cluster in clusters:
			distance = compute_distance(tweet['text'], cluster.centroid['text'])
			if distance < min_distance:
				min_distance = distance
				closest_cluster = cluster
		
		if min_distance < .1:
			closest_cluster.tweets.append(tweet)
		else:
			newCluster = Cluster(tweet)
			clusters.append(newCluster)

	for cluster in clusters:
		for tweet in cluster.tweets:
			print tweet['text']
		print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
		
				
	
