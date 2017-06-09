'''
Search for a given organization's users present in LinkedIn.
'''

import search_parser
import time
import requests
import re
from subprocess import call


class linkedin_search:
    def __init__(self, target, limit):
	self.target = target.replace(' ', '%20')
	self.results = ""
	self.total_results = ""
	self.server = "www.google.com"
	self.user_agent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
	self.headers = {'User-agent': self.user_agent}
	self.quantity = "100"
	self.limit = int(limit)
	self.counter = 0

    def search(self):
        try:
            url = "https://"+ self.server + "/search?num=100&start=" + str(self.counter) + "&hl=en&meta=&q=site%3Alinkedin.com/in%20" + self.target

        except Exception, e:
            print e

        try:
            req = requests.get(url, headers=self.headers)

        except Exception, e:
            print e

        self.results = req.content
        self.total_results += self.results


    def find_people(self):
	raw = search_parser.parser(self.total_results, self.target)
	return raw.people_linkedin()


    def process(self):
	while (self.counter <= self.limit):
           self.search()
           print "\tSearching " + str(self.counter) + " results..."
           self.counter += 100


    def target_profile(self, first_name, last_name, company, state):
	try:
           search = "https://www.google.com/search?q=" + first_name + "+" + last_name + "+" + company + "+" + state + "+" + "site:linkedin.com"

	except Exception, e:
           print e

	return call(["x-www-browser", search])

