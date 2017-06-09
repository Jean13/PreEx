'''
Search for a given organization's users present in LinkedIn.
'''

import search_parser
import time
import requests
import re


class phone_search:
    def __init__(self, f_name, l_name, state, city):
	self.f_name = f_name.replace(' ', '%20')
	self.l_name = l_name.replace(' ', '%20')
	self.state = state.replace(' ', '%20')
	self.city = city.replace(' ', '%20')
	self.results = ""
	self.total_results = ""
	self.user_agent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
	self.headers = {'User-agent': self.user_agent}

	self.web = "phonenumbers.addresses.com"


    def search(self):
        try:
            url = "http://"+ self.web + "/people/" + self.f_name + "+" + self.l_name + "/" + self.city + "+" + self.state

        except Exception, e:
            print e

        try:
            req = requests.get(url, headers=self.headers)

        except Exception, e:
            print e

        self.results = req.content
        self.total_results += self.results


    def find_numbers(self):
	raw = search_parser.parser(self.total_results, self.f_name)
	return raw.phone_numbers()

