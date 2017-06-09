'''
Search for a target's potential profiles in Facebook.
'''

import requests
import re
from subprocess import call


def facebook_search(first_name, last_name):

    try:
        search = "https://www.facebook.com/public?query=" + first_name + "+" + last_name + "&init=ffs&nomc=0"

    except Exception, e:
        print e

    return call(["x-www-browser", search])


