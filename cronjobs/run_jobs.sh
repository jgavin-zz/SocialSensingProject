#!/bin/bash

python /var/www/SocialSensingProject/delete_old_bad_tweets.py
python /var/www/SocialSensingProject/delete_duplicate_tweets.py
python /var/www/SocialSensingProject/sort_tweets.py
python /var/www/SocialSensingProject/count_tweets.py
