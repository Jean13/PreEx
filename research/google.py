'''
Search for email address and hostnames-IPs for a given domain/company.
'''

import search_parser
import time
import requests
import re


class google_search:
    def __init__(self, target, limit, start):
	self.target = target
	self.results = ""
	self.total_results = ""
	self.server = "www.google.com"
	self.user_agent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
	self.headers = {'User-agent': self.user_agent}
	self.quantity = "100"
	self.limit = int(limit)
	self.counter = int(start)


    def search(self):
	try:
            url = "https://" + self.server + "/search?num=" + self.quantity + "&start=" + str(self.counter) + "&hl=en&meta=&q=%40\"" + self.target + "\""
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
           self.counter += 100


