import tweepy as tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymongo
from pymongo import MongoClient
import json
#from tweepy import tweepy
credentials = {
            'consumer_key' : 'vk9ivGoO3YZja5bsMUTQ',
            'consumer_secret' : 't2mSb7zu3tu1FyQ9s3M4GOIl0PfwHC7CTGDcOuSZzZ4',
            'access_token_key' : '1157418127-gU3bUzLK0MgTA9pzWvgMpwD6E0R4Wi1dWp8FV9W',
            'access_token_secret' : 'k8C5jEYh4F4Ej2C4kDasHWx61ZWPzi9MgzpbNCevoCwSH'
        }
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token_key'], credentials['access_token_secret'])
api = tweepy.API(auth)
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
posts = db.posts

class get_old_tweets():
    
    def main(self):
        results = api.search(q = 'vodafone', count = 6, result_type = "recent")
        for result in results:
            
            post={
                "kind":"Twitter"}
            if 'text' in result.__dict__:
                post["text"]=(result.text).encode('utf-8')
            if 'name' in result.user.__dict__:
                post["name"]=(result.user.name).encode('utf-8'),
            if 'location' in result.author.__dict__:
                post["location"]=result.author.location,
            if 'screen_name' in result.user.__dict__:
                post["screen_name"]=(result.user.screen_name).encode('utf-8'),
            if 'profile_image_url' in result.user.__dict__:
                post["profile_image"]=(result.user.profile_image_url).encode('utf-8'),
            if 'created_at' in result.__dict__:
                post["created_at"]=result.created_at
            if 'followers_count' in result.author.__dict__:
                post["followers_count"]=result.author.followers_count
            if 'description' in result.author.__dict__:
                post["description"]=result.author.description
            if 'retweet_count' in result.__dict__:
                post["retweet_count"]=result.retweet_count
            if 'favourites_count' in result.author.__dict__:
                post["favourites_count"]=result.author.favourites_count
            
            post_id = posts.insert(post)
            print post
            print "#####################"
            #print posts.find_one({"kind":"Twitter"}),"resss"
            
        

class get_new_tweets(StreamListener):
    
    def on_data(self,result):
    		print result
    		post={
                "kind":"Twitter"}
    		if 'created_at' in result:
                    decoded = json.loads(result)
                    #json_result=json.dumps(decoded, sort_keys=True, indent=4)
                    post["text"]=decoded["text"]
                    post["created_at"]=decoded["created_at"]
                    post["name"]=decoded["name"]
                    post["screen_name"]=decoded["screen_name"]
                    post["location"]=decoded["location"]
                    post["description"]=decoded["description"]
                    post["profile_image_url"]=decoded["profile_image_url"]
                    post["followers_count"]=decoded["followers_count"]
                    
    		post_id = posts.insert(post)
    		return True

    def on_error(self,status):
        print status
class analyse():
    from operator import attrgetter
    import operator
    def useattr(attr):
        def kicker(obj):
            return getattr(obj, attr)
        return kicker
    def get_influencers(self):
        collection = db.test_collection
        print collection
        #db.posts.remove()
        print posts.find_one({"kind":"Twitter"})
        list=[]
        for post in posts.find({"kind":"Twitter"}):
            list.append(post)

        import operator
        
        #list=sorted(list,key=getattr('favourites_count'f))
        #li.sort(key='favourites_count', reverse=False)
        #li.sort(key=lambda x: x.favourites_count, reverse=True)


#get new
#twitter_stream=Stream(auth,get_new_tweets())
#twitter_stream.filter(track=["vodafone"])
#get old
old=get_old_tweets()
old.main()
#analyse
#analyse=analyse()
#analyse.get_influencers()