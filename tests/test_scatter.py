#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath("../"))

import unittest
from pandas import DataFrame

from mlog import setup_logger
logger = setup_logger('hippo_plot_test_scatter')

import hippo_plot as hp

import plotly.express as px

class TestScatter(unittest.TestCase):

	def setUp(self):

		data = [
			dict(x=1, y=1, smiles='Cn1ncc(NC(=O)CC#N)c1NC(=O)C1CCCO1', name='merge'),
			dict(x=2, y=3, smiles='CN1C=NC2=C1C(=O)N(C(=O)N2C)C', name='caffeine'),
		]

		df = DataFrame(data)

		self.fig = px.scatter(df, x='x', y='y', hover_data=data[0].keys())

		# self.fig.update_layout(title='Test Scatter Plot')

	def test_write_scatter(self):
		hp.io.write_html('test_scatter.html', self.fig)
		# logger.writing('test_scatter.html')
		# self.fig.write_html('test_scatter.html', include_plotlyjs=False)

	def tearDown(self):
		...

if __name__ == '__main__':
	unittest.main()
