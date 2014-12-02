import urlfetch
from facepy import GraphAPI
from datetime import datetime
from datetime import date
from datetime import timedelta
import json
import pymongo
from pymongo import MongoClient

scope = 'https://graph.facebook.com/oauth/access_token'
grant_type = 'client_credentials'
client_id = '270560493086575'   
client_secret = '6f376a7000da63e53353948a3e5292f5'
format = 'json'
fb_command = scope+'?grant_type='+grant_type+'&client_id='+client_id+'&client_secret='+client_secret+'&format='+format
access_token = urlfetch.fetch(fb_command).content.split('=')[1]
print access_token
graph = GraphAPI(access_token)

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
posts = db.posts
class Facebook():
    def get_posts(self):
        
        dd = datetime.fromordinal(date.today().toordinal()) - timedelta(days = 31)
        dd = dd.isoformat("T") + "Z"
        str_yesterday = str(dd)
        print str_yesterday,"sst"
        result = graph.search(term = "vodafone", type = 'post', page = False, retry = 2, 
		since = str_yesterday)
        while len(result['data']) != 0:
            for ele in result['data']:
                post={
                "kind":"Facebook"}
                post.update({"object":ele})
                post_id = posts.insert(post)
                #post['object']['message']
                #print json.dumps(post['object'], sort_keys=True, indent=4),"eleeeeeeee"
                
            #print posts.find_one({"type":"video"}),"edeee"
            
            if 'paging' in result:
                resultt=json.loads(urlfetch.fetch(result['paging']['next']).content)
                if result==resultt:
                    result['data']=""
                    print "iiiii"
                else:
                    try:
                        print "uuuuuu"
                        result = resultt
                    except Exception:
                        pass
            else:
                print "pppppppp"
                result['data']=""
				
        
    def get_comments(self):
        res=graph.fql("SELECT first_name,last_name,birthday FROM user WHERE uid = '337711220169'")
        print res,"rrr"

        
get=Facebook()
get.get_posts()
