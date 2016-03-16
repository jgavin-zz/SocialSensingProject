import datetime
import time
def compute_score(distance, retweets, likes, time_tweeted, username):

	virality_score = 1 - ((float(retweets) + float(likes)) / 1000)
	#print "virality score: " + str(virality_score)
	now = datetime.datetime.now()
	#time_tweeted = datetime.datetime.strptime(time_tweeted, '%Y-%m-%d %I:%M')
	tdelta = now - time_tweeted
	seconds = tdelta.total_seconds()
	seconds_in_a_day = 86400
	time_score = float(seconds) / float(seconds_in_a_day)

	return distance + virality_score + time_score
