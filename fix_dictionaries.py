import json
import re

teams = ['bulls', 'celtics', 'lakers', 'knicks', 'warriors']
for team_name in teams:
	word_file = open("dictionaries/" + team_name + ".json", 'r')
	word_json = json.load(word_file)

	array = []
	new_json = {}
	for s in word_json['players']:
		s = s.lower()
		s = re.sub("[^a-zA-Z ]","", s)
	
		s_split = s.split(' ')
		if len(s_split) > 1:
			array.append(s_split[0])
			array.append(s_split[1])
	new_json['players'] = array



	array = []
	for s in word_json['staff']:
		s = s.lower()
		s = re.sub("[^a-zA-Z ]","", s)
	
		s_split = s.split(' ')
		if len(s_split) > 1:
			array.append(s_split[0])
			array.append(s_split[1])
	new_json['staff'] = array



	array = []
	for s in word_json['team_info']:
		s = s.lower()
		s = re.sub("[^a-zA-Z ]","", s)
	
		s_split = s.split(' ')
		for word in s_split:
			array.append(word)

	new_json['team_info'] = array

	array = []
	for s in word_json['accounts']:
		s = s.lower()
		s = re.sub("[^a-zA-Z ]","", s)
		array.append(s)

	new_json['accounts'] = array

	array = []
	for s in word_json['hashtags']:
		s = s.lower()
		array.append(s)

	new_json['hashtags'] = array

	write_file = open("dictionaries/new_" + team_name + ".json", 'w')
	json.dump(new_json, write_file)