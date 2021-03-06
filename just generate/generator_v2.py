#!/usr/in/python

import csv
import os
import numpy
import sys
import time
import datetime
import random
import string
from datetime import timedelta, date

sensitivity = ['LA', 'MM', 'UM', 'XX']
shop_mission = ['Small Shop', 'Top Up', 'Full Shop', 'XX']
dominant_mission = ['Fresh', 'Grocery', 'Mixed', 'Non Food', 'XX']
store_format = ['LS', 'MS', 'SS', 'XLS']
lifestage = ['YA', 'OA', 'YF', 'OF', 'PE', 'OT', 'XX']
hour = [str(n) for n in range(0, 24)]
direction = ['W', 'E', 'S', 'N']
basket_size = ['S', 'M', 'L']
chunk_size = 1000000 #monster chunk with a size of 1 million

store_base = 992100100000000
customer_base = 993100100000000
basket_base = 994100100000000


def format_code(prefix, num, digits):
	return prefix + str(num).rjust(digits, '0')

def rand_time_code(start_date, days):
	shop_date = start_date + timedelta(random.randint(0, days))
	return str(shop_date.year) + '%02d' % (shop_date.isocalendar()[1])

def createTime(num_weeks):
	dt = datetime.datetime.now()
	#dt = datetime.datetime.strptime('20160101', '%Y%m%d')
	start_from = dt - timedelta(dt.weekday())

	sequence = 1
	lines = []
	while sequence <= num_weeks:
		time_code = str(start_from.year) + "%02d" % (start_from.isocalendar()[1])
		date_from = str(start_from.year) + "%02d%02d" % (start_from.month, start_from.day)
		end_date = start_from + timedelta(6)
		date_to = str(end_date.year) + "%02d%02d" % (end_date.month, end_date.day)

		line = [sequence, time_code, date_from, date_to]
		lines.append(line)
		sequence += 1
		start_from += timedelta(7)

	with open('Time.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		writer.writerows(lines)

	return dt, (end_date-dt).days

################################################################################################################
def createBaskets(bask_sz, start_date, days):
	bask_id = 0
	with open('Baskets.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		count = 1
		chunk = 1
		num_baskets = 0

		while count > 0:
			lines = []

			for  i in range(chunk):
				line = ["\t" + str(basket_base+bask_id)]
				time_code = rand_time_code(start_date, days)
				sz = random.choice(basket_size)
				bask_sens = random.choice(sensitivity)
				s_mission = random.choice(shop_mission)
				d_mission = random.choice(dominant_mission)
				line.append(time_code)
				line.append(sz)
				line.append(bask_sens)
				line.append(s_mission)
				line.append(d_mission)
				lines.append(line)
				bask_id += 1

			count -= chunk

			if chunk == 1:
				writer.writerow(line)
				csvfile.flush()
				num_baskets = int(bask_sz/os.path.getsize('Baskets.csv'))
				count = num_baskets
				chunk = chunk_size
			else:
				writer.writerows(lines)

			if count < chunk:
				chunk = count

	return bask_id

################################################################################################################
def createProducts(prod_sz):
	prod_id = 0
	with open('Products.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		desc = "description"
		prefixes = ['PRD', 'CL', 'DEP', 'G', 'D']
		count = 1
		chunk = 1
		num_products = 0

		while count > 0:
			lines = []
			for i in range(chunk):
				line = [str(prod_id)]
				for prefix in prefixes:
					line.append(format_code(prefix, prod_id, 5))
					line.append(desc)
				lines.append(line)
				prod_id += 1

			count -= chunk

			if chunk == 1:
				writer.writerow(line)
				csvfile.flush()
				num_products = int(prod_sz/os.path.getsize('Products.csv'))
				count = num_products
				chunk = chunk_size
			else:
				writer.writerows(lines)

			if count < chunk:
				chunk = count

	return prod_id

################################################################################################################
def createStores(stores_sz):
	store_id = 0
	with open('Stores.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		count = 1
		chunk = 1
		num_stores = 0

		while count > 0:
			lines = []
			for i in range(chunk):
				store_code = format_code('STORE', store_id, 5)
				s_format = random.choice(store_format)
				s_region = format_code(random.choice(direction), random.randint(0, 99), 2)
				store_name = 'STORE_' + s_region + format_code('_', store_id, 5) 
				line = ["\t" + str(store_base+store_id)]
				line.append(store_code)
				line.append(store_name)
				line.append(s_format)
				line.append(s_region)
				lines.append(line)
				store_id += 1

			count -= chunk

			if chunk == 1:
				writer.writerow(line)
				csvfile.flush()
				num_stores = int(stores_sz/os.path.getsize('Stores.csv'))
				count = num_stores
				chunk = chunk_size
			else:
				writer.writerows(lines)

			if count - chunk < 0:
				chunk = count

	return store_id

################################################################################################################
def createCustomers(cust_sz, num_store):
	cust_id = 0
	with open('Customers.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		count = 1
		chunk = 1
		num_cust = 0

		while count > 0:
			lines = []
			for i in range(chunk):
				line = ["\t" + str(customer_base+cust_id)]
				line.append(format_code('CUST', cust_id, 10))
				line.append("\t" + str(numpy.random.randint(num_store) +store_base))
				line.append(random.choice(sensitivity))
				line.append(random.choice(lifestage))
				lines.append(line)
				cust_id += 1

			count -= chunk

			if chunk == 1:
				writer.writerow(line)
				csvfile.flush()
				num_cust = int(cust_sz/os.path.getsize('Customers.csv'))
				count = num_cust
				chunk = chunk_size
			else:
				writer.writerows(lines)

			if count < chunk:
				chunk = count

	return cust_id


################################################################################################################
def createTransactions(tx_sz, num_bask, num_prod, num_store, num_cust, start_date, days):
	with open('Transactions.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		count = 1
		chunk = 1
		tx_count = 0

		while count > 0:
			lines = []

			for i in range(chunk):
				line = ["\t" + str(basket_base + random.randint(0, num_bask - 1))] #basket_id
				line.append("\t" + str(random.randint(0, num_prod - 1))) #product_id
				line.append("\t" + str(store_base + random.randint(0, num_store - 1))) #store_id
				line.append("\t" + str(customer_base + random.randint(0, num_cust - 1))) #customer id
				line.append(random.randint(0, 10)) #quantity
				line.append(str(random.randint(0, 20) + random.randint(0, 99)/100.0)) #spend
				shop_date = start_date + timedelta(random.randint(0, days))
				line.append(str(shop_date.year) + '%02d%02d' % (shop_date.month, shop_date.day)) #shop_date
				line.append(str(shop_date.year) + '%02d' % (shop_date.isocalendar()[1])) #time_code
				line.append(shop_date.isoweekday()) #weekday
				line.append(random.choice(hour)) #hour_slot
				tx_count += 1
				lines.append(line)

			count -= chunk
			if chunk == 1:
				writer.writerow(line)
				csvfile.flush()
				num_tx = int(tx_sz/os.path.getsize('Transactions.csv'))
				count = num_tx
				chunk = chunk_size
			else:
				writer.writerows(lines)

			if count - chunk < 0:
				chunk = count

	return tx_count
################################################################################################################
def size_conversion(sz_str):
	measure = sz_str[-2:].upper()
	if measure == 'MB':
		return float(sz_str[:-2])*(1000**2)
	elif measure == 'GB':
		return float(sz_str[:-2])*(1000**3)
	elif measure == 'TB':
		return float(sz_str[:-2])*(1000**4) 
	else:
		return size_conversion(raw_input("Enter at least 1MB\n"))

################################################################################################################

if __name__ == "__main__":
	num_weeks = int(raw_input("Enter an integer as the number of weeks needs to generate\n"))
	time_range = createTime(num_weeks)
	current_sz = os.path.getsize('Time.csv')
	print "current dataset size is %dB\n" % current_sz

	sz_str = raw_input("Enter the total size of the dataset(i.e. 1MB, 1GB. At least 1MB)\n")
	sz_in_bytes = size_conversion(sz_str)

	ratio_sum = 4000000+620000+6600+66+10

	tx_ratio = 4000000.0/ratio_sum
	bask_ratio = 620000.0/ratio_sum
	cust_ratio = 6600.0/ratio_sum
	prod_ratio = 66.0/ratio_sum
	stores_ratio = 10.0/ratio_sum

	'''
	while not (prod_ratio+stores_ratio+cust_ratio+bask_ratio+tx_ratio == 1):
		print "Enter the size ratio of the remaining tables, in the order of Products Stores Customers Baskets Transactions(i.e. 1 1 2 2 4)\n"
		ratio = raw_input("Must add up to 10. Hit enter if set to default: 1 1 2 2 4\n")
		if not ratio:
			ratio = "1 1 2 2 4"

		ratio = ratio.split()
		prod_ratio = float(ratio[0])/10.0
		stores_ratio = float(ratio[1])/10.0
		cust_ratio = float(ratio[2])/10.0
		bask_ratio = float(ratio[3])/10.0
		tx_ratio = float(ratio[4])/10.0
	'''

	remaining_sz = sz_in_bytes - current_sz
	prod_sz = remaining_sz * prod_ratio
	stores_sz = remaining_sz * stores_ratio
	cust_sz = remaining_sz * cust_ratio
	bask_sz = remaining_sz * bask_ratio
	
	print "generating..."

	num_products = createProducts(prod_sz)
	num_stores = createStores(stores_sz)
	num_cust = createCustomers(cust_sz, num_stores)
	num_basket = createBaskets(bask_sz, time_range[0], time_range[1])

	tx_sz = remaining_sz - os.path.getsize('Baskets.csv') - os.path.getsize('Customers.csv') \
			- os.path.getsize('Products.csv') - os.path.getsize('Stores.csv')

	num_tx = createTransactions(tx_sz, num_basket, num_products, num_stores, num_cust, time_range[0], time_range[1])

	print "done generating.\n"
	print "generated\n %i transactions\n %i baskets\n %i customers\n %i products\n %i stores" \
			% (num_tx, num_basket, num_cust, num_products, num_stores)

