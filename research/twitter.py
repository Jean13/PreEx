'''
Search for a target's potential profiles in Twitter.
'''

import requests
import re
from subprocess import call


def twitter_search(first_name, last_name, state):

    try:
        search = "https://twitter.com/search?f=users&vertical=default&q=" + first_name + "%20" + last_name + "%20" + near + "%3A%22" + state + "%22%20within%3A15mi&src=tpd"

    except Exception, e:
        print e

    return call(["x-www-browser", search])


