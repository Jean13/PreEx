'''
Search for email address and hostnames-IPs for a given domain/company.
'''

import search_parser
import time
import requests
import re


class baidu_search:
    def __init__(self, target, limit):
	self.target = target
	self.results = ""
	self.total_results = ""
	self.server = "www.baidu.com"
	self.user_agent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
	self.headers = {'User-agent': self.user_agent}
	self.limit = int(limit)
	self.counter = 0


    def search(self):
	try:
            url = "http://" + self.server + "/s?wd=%40" + self.target + "&pn=" + str(self.counter)
        except Exception, e:
            print e

        try:
            req = requests.get(url, headers=self.headers)

        except Exception, e:
            print e
        self.results = req.content
        self.total_results += self.results


    def find_emails(self):
	raw = search_parser.parser(self.total_results, self.target)
	return raw.emails()


    def find_hostnames(self):
	raw = search_parser.parser(self.total_results, self.target)
	return raw.hostnames()


    def process(self):
	while self.counter <= self.limit and self.counter <= 1000:
           self.search()
           time.sleep(1)
           print "\tSearching " + str(self.counter) + " results..."
           self.counter += 10
