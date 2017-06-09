'''
Credit to laramies.
'''

import sys
import socket


class Confirm():
    def __init__(self, hosts):
        self.hosts = hosts
        self.real_hosts = []


    def check(self):
        for h in self.hosts:
            try:
                res = socket.gethostbyname(h)
                self.real_hosts.append(res + ' : ' + h)
            except Exception, e:
                pass

        return self.real_hosts

