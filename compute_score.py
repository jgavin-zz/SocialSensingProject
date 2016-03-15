def compute_score(distance, retweets, likes, time_tweeted, username):

	virality_score = 1 - ((float(retweets) + float(likes)) / 1000)

	return distance + virality_score
