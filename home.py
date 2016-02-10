from flask import Flask
from flask.ext.cache import Cache
from flask import render_template
from flask.ext.twitter_oembedder import TwitterOEmbedder
import tweepy
from tweepy import OAuthHandler

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
twitter_oembedder = TwitterOEmbedder(app,cache,debug=True)
app.config['TWITTER_CONSUMER_KEY'] = 'FrTtImImzPxthrIjkTFrsUatY'
app.config['TWITTER_CONSUMER_SECRET'] = 'cbPq4hNVEIj87LKcnP4XgCPAdPVc0By8ZVKH7WWVE5H9FS6ihb'
app.config['TWITTER_ACCESS_TOKEN'] = '635902588-6BuJRUYxXQ63vfmQYcP7auLAjkTgxaCRz70MwP5x'
app.config['TWITTER_TOKEN_SECRET'] = 'YsLyHMKLoUl47cCge1sBb7KfjDhg2wBbjWhBWm4VVOXtd'


auth = tweepy.OAuthHandler('FrTtImImzPxthrIjkTFrsUatY', 'cbPq4hNVEIj87LKcnP4XgCPAdPVc0By8ZVKH7WWVE5H9FS6ihb')
auth.set_access_token('635902588-6BuJRUYxXQ63vfmQYcP7auLAjkTgxaCRz70MwP5x', 'YsLyHMKLoUl47cCge1sBb7KfjDhg2wBbjWhBWm4VVOXtd')
api = tweepy.API(auth)


@app.route('/')
def home():
    return 'Here is the home page!'
    
    
@app.route('/teams/')
def teams():
    return 'Here is the teams page!'
    
    
@app.route('/teams/<team_name>/')
def team_name(team_name):
	query = team_name
	max_tweets = 10
	tweets = api.search(q = query, rpp = max_tweets)
	tweet_ids = []
	count = 0
	for tweet in tweets:
		count = count + 1
		tweet_ids.append(tweet.id)
		if count == 3:
			break
	return render_template('team_name.html', team_name = team_name, tweet_ids = tweet_ids)
	

if __name__ == '__main__':
	app.debug = True
	#app.run(host='0.0.0.0')
	app.run()