from instagram.client import InstagramAPI
from datetime import datetime
from datetime import date
from datetime import timedelta
import urllib2
import json
import json
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
posts = db.posts

dd = datetime.fromordinal(date.today().toordinal()) - timedelta(days = 31)
dd = dd.isoformat("T") + "Z"
str_yesterday = str(dd)
dd = datetime.fromordinal(date.today().toordinal()) - timedelta(days = 1)
dd = dd.isoformat("T") + "Z"
str_yesterday2 = str(dd)

api = InstagramAPI(client_id='40b505438af94b33b7d7d397ad07458a', client_secret='ce1638efd38b4262a691419d39715bc9')
#popular_media = api.media_search(q="vodafone",count=10,lat=25.282895, lng=51.533922,min_timestamp="str_yesterday",max_timestamp="str_yesterday2")
med=api.user_recent_media(count=10,user_id="561869258")

url = med[1]
jsonn = urllib2.urlopen(url).read()
results = json.loads(jsonn)
#print json.dumps(decoded, sort_keys=True, indent=4)
print results['data'][0]["link"],"link"
for result in results["data"]:
	post={"kind":"Instagram"}
	post.update({"object":result})
	post_id=posts.insert(post)

#	for comment in result["comments"]["data"]:
#		print comment["text"].encode('utf-8')
print results['data'][0]["comments"]["data"][0]["text"].encode('utf-8')
