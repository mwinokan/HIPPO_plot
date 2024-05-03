#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath("../"))


import unittest
# from pandas import DataFrame

from mlog import setup_logger
logger = setup_logger('hippo_plot_2a_hippo')

import hippo
import hippo_plot as hp

from pathlib import Path

# import plotly.express as px

class Test2aHIPPO(unittest.TestCase):

	def setUp(self):

		hippo_install = os.environ['HIPPO']

		assert hippo_install

		if not hippo_install: 
			logger.error(f'Please set environment variable HIPPO to hippo-db install location')
			raise Exception

		hippo_install = Path(hippo_install)

		test_db = hippo_install / "tests" / "test_A71EV2A.sqlite"

		if not test_db.exists():
			logger.error(f'Please run {hippo_install / "tests" / "test_A71EV2A.py"} first')
			raise Exception

		self.animal = hippo.HIPPO('Test2aHIPPO', test_db)

	def test_compound_scatter(self):
		fig = self.animal.plot_compound_property(['id', 'num_heavy_atoms'], style='scatter')
		hp.io.write_html('test_2a_compound_scatter.html', fig)
		logger.debug('view the figure by running: python -m hippo_plot.cli tests/test_2a_compound_scatter.html')

	def tearDown(self):
		self.animal.db.close()

if __name__ == '__main__':
	unittest.main()
