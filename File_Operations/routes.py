# -*- coding: utf-8 -*-
# Filename: routes.py
# Description: This file contains all the application routes
# Author: Ajay Vanara

# Built-in imports 
import connexion
from flask import request, jsonify

# Application imports
from operations.document_ops import DocOps


app = connexion.App(__name__, specification_dir="./")


@app.route("/v1/ping")
def ping():
	"""
	this method is used for health check of the application
	imput: None
	output: json
	"""
	return jsonify({"data":"Pong"})


@app.route("/v1/fetch_data")
def fetch_details():
	"""
	This method is used for search operations to be performed on the file
	input: rows - Numbers of rows to be fetched from file 
	output: fetched response (json)   
	"""
	rows = request.args.get('rows')
	res = DocOps().fetch_data(rows)
	return res

@app.route("/v1/search_details")
def search():
	"""
	This method is used for search operations to be performed on the file
	input: rows - Numbers of rows to be fetched from file 
	output: search response (json)   
	"""
	data = request.json
	res = DocOps().search_data(data)
	return res
