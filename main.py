#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------
# Google App Engine Demo
# Playing with Flask in Python
# GET returns number-th position in the container 
# POST appends to the container
# ----------------------------------------------


from flask import Flask, jsonify


app = Flask(__name__)
container = ['Hello World!', 'Google']

@app.route('/mainpage/')
def mainpage():
	return jsonify(container)

@app.route('/get/<number>')
def get(number):
	if int(number) > len(container):
		return 'That number is greater than the size of the container'
	else:
		return jsonify(container[int(number)])

@app.route('/post/<word>')
def post(word):
	container.append(word)
	return jsonify(word)

@app.route('/delete/<number>')
def delete(number):
	if int(number) > len(container):
		return 'That number is greater than the size of the container'
	else:
		container.pop(int(number))
		return 'Success'

if __name__ == '__main__':
	app.run(debug=True)

