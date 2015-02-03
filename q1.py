from bottle import Bottle, request, run
from time import time
from datetime import datetime
from sys import argv
from bottle import template
import urllib2
import json
import d3py
import collections
import string

app = Bottle()

@app.route('/')
def index():
	return open('home.html').read()

@app.route('/show')
def show():
	name = request.GET['query']
	url = "https://api.angel.co/1/search?query="+name+"&type=User"
	res = urllib2.urlopen(url)
	data = json.load(res)
	ans = collections.OrderedDict()
	for i in range(5):
		tmp = data[i]["name"]
		tmp = tmp.replace(" ","")
		for char in tmp:
			char = char.decode('utf-8').lower()
			if ans.has_key(char):
				ans[char] += 1
			else:
				ans[char] = 1
	res = []
	for index in ans:
		if ans.has_key(index):
			res.append({"alpha":index,"count":ans[index]})
	#return str(ans)
	return template(open('show.html').read(),query=json.dumps(res))
app.run(host='localhost', port=8080)
