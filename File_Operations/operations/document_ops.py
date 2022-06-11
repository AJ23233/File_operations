# Filename: document_ops.py
# Description: This file contains various search operations to be performed on data
# Author: Ajay Vanara

import os
from pandas import read_csv
from numpy import nan
import re

from config import CONF

class DocOps:
	"""
	This class contains various methods which can perform various search operations on data
	"""

	def __init__(self):
		"""
		This is a constructor of a class and it reloads the data when the object is initialized for a class
		"""

		self.data = os.path.join(os.path.dirname(
						os.path.dirname(os.path.abspath
							(__file__))),
					CONF['directory']['data'],
					CONF['file_names']['csv'])

	def fetch_data(self, rows):
		"""
		this method is used to fetch data
		"""
		try:
			df= read_csv(self.data)
			res = df.iloc[:int(rows)]
			res = DocOps.replace_vals(res)
			response = {"books":str(res.to_dict("records"))}
		except Exception as ex:
			response = {"error" : "Error while searching for data"}
		return response

	@staticmethod
	def replace_vals(df):
		"""
		This method replaces special characters
		to avoid creating invalid json
		"""
		try:
			categorical_feat = [i for i in df.columns if df[i].dtype =='O']
			new_df = df[categorical_feat].fillna("").applymap(lambda x: re.sub(r"'",r"\'",x))
			df[categorical_feat] = new_df
		except Exception as ex:
			df = DataFrame()
		return df

	def search_data(self, query):
		"""
		this method is used to search data
		"""
		try:
			df= read_csv(self.data)
			for k,v in query.items():
				if k in df.columns:
					df = df[df[k]==v]

			res = DocOps.replace_vals(df)
			response = {"books":str(res.to_dict("records"))}
		except Exception as ex:
			response = {"error" : "Error while searching for data"}
		return response
