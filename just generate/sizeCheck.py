#!/usr/in/python

import os
import glob

files = glob.glob('*.csv')
total = 0
for file in files:
	total += os.path.getsize(file)

print total