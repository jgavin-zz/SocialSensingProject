from flask import Flask
from flask.ext.cache import Cache
from flask import render_template
from flask.ext.twitter_oembedder import TwitterOEmbedder
from flask import request
from flask import session, make_response, url_for, redirect
from flask.ext.session import Session
import tweepy
from tweepy import OAuthHandler
from fetch_top_tweets import fetch_top_tweets	
from fetch_all_tweets import fetch_all_tweets
from update_retweets import update_retweets
from insert_user import insert_user
from validate_user import validate_user
import requests
import json
import datetime
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'any random string'


cache = Cache(app, config={'CACHE_TYPE': 'simple'})
twitter_oembedder = TwitterOEmbedder(app,cache,debug=True)
app.config['TWITTER_CONSUMER_KEY'] = 'FrTtImImzPxthrIjkTFrsUatY'
app.config['TWITTER_CONSUMER_SECRET'] = 'cbPq4hNVEIj87LKcnP4XgCPAdPVc0By8ZVKH7WWVE5H9FS6ihb'
app.config['TWITTER_ACCESS_TOKEN'] = '635902588-6BuJRUYxXQ63vfmQYcP7auLAjkTgxaCRz70MwP5x'
app.config['TWITTER_TOKEN_SECRET'] = 'YsLyHMKLoUl47cCge1sBb7KfjDhg2wBbjWhBWm4VVOXtd'

@app.route('/')
#@app.route('/teams/')
def home():
	
	if 'key' in session:
		return render_template('home.html', email = session['key'])	
	else:
		return redirect(url_for('login'))
		
    
@app.route('/teams/<team_name>/')
def team_name(team_name):
	if 'key' in session:
		tweet_ids = fetch_top_tweets(team_name)
		return render_template('team_name.html', team_name = team_name, tweet_ids = tweet_ids, email = session['key'])
	else:
		return redirect(url_for('login'))

@app.route('/get_tweets')
def get_tweets():
	tweets = fetch_all_tweets()
	return tweets
                
@app.route('/post_tweets', methods = ['POST'])
def post_tweets():
	data = request.json
	update_retweets(data)
	logfile = open("/var/www/SocialSensingProject/log.txt", 'a')
	logfile.write("Posted tweets at " + str(datetime.datetime.now())+ '\n')
	logfile.close()
	return "posted tweets"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/register_user', methods = ['POST']) 
def register_user():   
	email = request.form.get('email')
	password = request.form.get('password')
	if insert_user(email, password):
		return render_template('message.html', message = "Registered Successfully")
	else:
		return render_template('message.html', message = "Registration Failed")
	
@app.route('/login_user', methods = ['POST']) 
def login_user():   
	email = request.form.get('email')
	password = request.form.get('password')
	if validate_user(email, password):
		session['key'] = str(email)
		return redirect(url_for('home'))
	else:
		return render_template('message.html', message = "Login Failed")

@app.route('/logout') 
def logout():   
	session.clear()
	return redirect(url_for('home'))
	
@app.route('/customize')
def customize():
	if 'key' in session:
		return render_template('custom.html')
	else:
		return redirect(url_for('login'))
	
	
@app.route('/post_customize', methods = ['POST'])
def post_customize():
	virality = int(request.form.get('viralityRangeInput'))
	time = int(request.form.get('timeRangeInput'))
	relevance = int(request.form.get('relevanceRangeInput'))
	
	
	
	return render_template('message.html', message = "Preferences Updated")
