import random
import base64
import json
import requests
class RandomUserAgent(object):
	"""Randomly rotate user agents based on a list of predefined ones"""

	def __init__(self, agents):

		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.getlist('USER_AGENTS'))

	def process_request(self, request, spider):
		#print "**************************" + random.choice(self.agents)
		request.headers.setdefault('User-Agent', random.choice(self.agents))
class ProxyMiddleware(object):
	def process_request(self, request, spider):
		item =json.loads(requests.get('http://127.0.0.1:8000/?types=0').content)
		list1=[]
		for i in item :
			temp=dict()
			temp['ip'] = i['ip']
			temp['port'] = i['port']
    		list1.append(temp)
		i= random.randint(0,len(item)-1)
		proxy = item[i]

		print "**************ProxyMiddleware no pass************" + str(proxy['ip'])+":"+str(proxy['port'])
		request.meta['proxy'] = "http://"+str(proxy['ip'])+":"+str(proxy['port'])
