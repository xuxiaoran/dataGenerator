#!/usr/in/python

import csv
import sys

if __name__ == "__main__":
	filename = sys.argv[1]
	data = []
	with open(filename + ".tbl") as file:
		for line in file:
			columns = line.strip().split("|")
			columns.pop()

			for i in range(len(columns)):
				try:
					int(columns[i])
					columns[i] = int(columns[i])
				except ValueError:
					try:
						float(columns[i])
						columns[i] = float(columns[i])
					except ValueError:
						continue
						
			data.append(columns)

	with open(filename+".csv", 'wb') as csvfile:
		writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
		writer.writerows(data)
