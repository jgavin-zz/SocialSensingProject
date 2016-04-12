import json
def check_basketball_keywords(status):

	keywords_file = open("dictionaries/basketball_keywords.json", 'r')
	keywords_json = json.load(keywords_file)
#	keywords_words = keywords_json['basketball_keywords']

	print status
#	words = status.split(' ')	

#	match_count = 0
#	for word in words:		
#		if word in keywords_words:
#			match_count = match_count + 1
			
#	if match_count == 0:
#		return 0
#	else:
#		return 1

	
