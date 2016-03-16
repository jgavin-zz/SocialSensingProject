#This code needs to compute tweets by iterating over tweets, creating clusters by splitting on 
#a certain diameter

class Cluster:
	def __init__(self, c):
		self.centroid = c
		self.tweets = [c]

def compute_centroid(cluster):

	min_average_distance = 1
	new_centroid = cluster.tweets[0]
	cluster_tweets = cluster.tweets
		
	for tweet in cluster.tweets:
		total_distance = 0
			
		for compare_tweet in cluster_tweets:
			distance = compute_distance(tweet['text'], compare_tweet['text'])
			total_distance = total_distance + distance
				
		average_distance = float(total_distance)/float(len(cluster.tweets))
			
		if average_distance < min_average_distance:
			min_average_distance = average_distance
			cluster.centroid = tweet


def compute_distance(status1, status2):

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
	diameter = .5
	
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
		
		if min_distance < diameter:
			closest_cluster.tweets.append(tweet)
			compute_centroid(closest_cluster)
		else:
			newCluster = Cluster(tweet)
			clusters.append(newCluster)


	#for cluster in clusters:
	#	for tweet in cluster.tweets:
	#		print tweet['text']
	#	print "XXXXXXXXXXXXXXXXXXXXXXXXXX"
	
	return clusters
		
				
	
