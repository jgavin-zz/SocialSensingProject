#!/bin/bash

./usr/bin/python /var/www/SocialSensingProject/delete_old_bad_tweets.py
./usr/bin/python /var/www/SocialSensingProject/delete_duplicate_tweets.py
./usr/bin/python /var/www/SocialSensingProject/sort_tweets.py
./usr/bin/python /var/www/SocialSensingProject/count_tweets.py
./usr/bin/python /var/www/SocialSensingProject/update_scores.py
