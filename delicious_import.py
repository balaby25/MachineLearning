"""
thanks to hillary mason
https://github.com/hmason/ml_class/
"""

import sys, re, base64
import urllib.request
import urllib.parse
import urllib.response
import csv
from xml.dom import minidom

class delicious_import(object):
     def __init__(self):
#    def __init__(self, username, passwrod=''):
            # API URL: https://user:passwd@api.del.icio.us/v1/posts/all
#

        # url = "https://api.del.icio.us/v1/posts/all"
        username = "balaby25"
        password = "cbkn1255"
        #url = "https://%s:%s@api.del.icio.us/v1/posts/recent?count=5" % (username, password)
        url="https://api.del.icio.us/v1/posts/recent?count=5"

        p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        p.add_password(None, url, username, password)

        auth_handler = urllib.request.HTTPBasicAuthHandler(p)

        opener = urllib.request.build_opener(auth_handler)

        urllib.request.install_opener(opener)

        try:
            result = opener.open(url)
            messages = result.read()
            print (messages)
        except IOError as e:
            print (e)


        x = minidom.parseString(messages)

        data = []
        # sample post: <post href="http://www.pixelbeat.org/cmdline.html" hash="e3ac1d1e4403d077ee7e65f62a55c406" description="Linux Commands - A practical reference" tag="linux tutorial reference" time="2010-11-29T01:07:35Z" extended="" meta="c79362665abb0303d577b6b9aa341599" />
        post_list = x.getElementsByTagName('post')
        for post_index, post in enumerate(post_list):
            url = post.getAttribute('href')
            desc = post.getAttribute('description')
            tags = ",".join([t for t in post.getAttribute('tag').split()])
            timestamp = post.getAttribute('time')

            data.append([url.encode("utf-8"), tags.encode("utf-8")])

        writer = csv.writer (open("links.csv", 'w'))
        for entry in data:
            writer.writerow(entry)




if __name__ == '__main__':
    try:
        (username, password) = sys.argv[1:]
    except ValueError:
        print ("usage: python delicious_import.py username password")

    d = delicious_import()
