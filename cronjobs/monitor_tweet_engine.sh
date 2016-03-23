#!/bin/bash

# Check if gedit is running
if ! pgrep -f "python tweet_engine.py" &> /dev/null
then
	#Restart tweet engine
	cd /var/www/SocialSensingProject
	python tweet_engine.py &

	echo Restarted tweet engine at $(date +%Y.%m.%d-%H:%M:%S) >> log.txt
fi

