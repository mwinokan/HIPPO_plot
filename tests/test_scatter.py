#!/usr/bin/env python

import unittest
from pandas import DataFrame

from mlog import setup_logger
logger = setup_logger('HIPPO_plot')

import plotly.express as px

class TestScatter(unittest.TestCase):

	def setUp(self):

		data = [
			dict(x=1, y=1, smiles='Cn1ncc(NC(=O)CC#N)c1NC(=O)C1CCCO1'),
			dict(x=2, y=3, smiles='CN1C=NC2=C1C(=O)N(C(=O)N2C)C'),
		]

		df = DataFrame(data)

		self.fig = px.scatter(df, x='x', y='y', hover_data=data[0].keys())

	def test_write_scatter(self):
		logger.writing('test_scatter.html')
		self.fig.write_html('test_scatter.html', include_plotlyjs=False)

	def tearDown(self):
		...

if __name__ == '__main__':
	unittest.main()
