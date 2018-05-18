import random 
import numpy as np 
nRacks = 12 
nItems = 5 

warehouse = {a: (0,0) for a in range(1,nRacks+1)} 

def initialise_warehouse(): 
	
	warehouse = {a: (0,0) for a in range(1,nRacks+1)} 

	warehouse = initialise_util(3, 1, 10) 
	warehouse = initialise_util(5, 3, 10) 
	warehouse = initialise_util(9, 2, 10) 
	warehouse = initialise_util(11, 5, 10) 
	warehouse = initialise_util(1, 4, 10) 
	

def print_warehouse(warehouse): 
	print 
	for i in warehouse: 7
		print str(i) + "->" + str(warehouse[i]) + "\t"
		if i % 3 == 0: 
			print 

def initialise_util(rack, item, quantity): 
	if rack not in warehouse: print "No rack {} exists".format(rack) # No such rack exists 
	elif warehouse[rack] == (0,0): # Rack is empty 
		warehouse[rack] = (item, quantity) 
		
def get_util(warehouse, rack, item, quantity): 
	if (rack not in warehouse) and (warehouse[rack][0] != item): return warehouse # No such rack exists  
	elif ((warehouse[rack][1] == quantity) or (warehouse[rack][1] < quantity)): # Rack has exact qauntity or doesnot have enough quantity 
		warehouse[rack] = (0, 0) 
		return warehouse 
	else: 
		warehouse[rack] = (item, warehouse[rack][1] - quantity) # update quantity on rack 
		return warehouse

def store_util(warehouse, rack, item, quantity): 
	if (rack not in warehouse): return warehouse # No such rack exists  
	elif warehouse[rack] == (0,0): # Empty rack 
		 warehouse[rack] = (item, quantity) 
		 return warehouse 
	elif (warehouse[rack][0] == item): # Rack already has some qauntity of that item 
		warehouse[rack] = (item, warehouse[rack][1]+quantity) 
		return warehouse 
	else: # Some other item is in that rack 
		return warehouse
		
def get_requests(warehouse, item, quantity): # Assuming all quantity is taken 
	for i in warehouse: 
		if item in warehouse[i]: 
			 rack = i # Rack number 
	warehouse = get_util(warehouse, rack, item, quantity) 
	#warehouse[rack] = (0,0) # Assuming all quantity is taken 
	immediate_reward = rewards(warehouse, rack) 
	return warehouse, immediate_reward, rack 

def store_requests(warehouse, rack, item, quantity): 
	warehouse = store_util(warehouse, rack, item, quantity)	
	return warehouse 

''' 
Reward Table: 
Racks:  1,2,3 -------> 	-40 
		4,5,6 -------> 	-30 
		7,8,9 -------> 	-20 
		10,11,12 ---->  -10 
''' 

def rewards(warehouse, rack): 
	if rack in range(1,4): return -40 
	elif rack in range(4,7): return -30 
	elif rack in range(7,10): return -20 
	elif rack in range(10,13): return -10 
	else: return 0 # Wrong rack 

def test_warehouse(warehouse): 
	return warehouse 
def test(): 
	warehouse = {} 
	warehouse = initialise_warehouse(warehouse) 
	warehouse = test_warehouse(warehouse) 
	print "Hello jii" 
	print_warehouse(warehouse) 
	
	''' 
	# test get_requests 
	print "Check get_requests" 

	warehouse, immediate_reward, rack = get_requests(warehouse, 2, 5) 
	print_warehouse(warehouse) 
	print "Immediate Reward =", immediate_reward 
	print "Obtained from Rack =", rack 
	''' 

	'''
	# test store_requests 

	warehouse = store_requests(warehouse, 1, 4, 100) 
	print_warehouse(warehouse) 
	''' 
	
	requests = ["STORE 3 4 100", "STORE 4 5 100", "STORE 1 1 100", "STORE 9 2 100", "STORE 11 3 100", "STORE 12 2 100", "STORE 2 1 100", 
				"GET 4 20", "GET 3 20", "GET 2 20", "GET 1 20", "GET 5 20", "STORE 3 4 100", "STORE 7 2 100", "STORE 8 1 100", ]

	for request in requests: 
		request = request.split(' ') 
		if(request[0]) == "GET": 
			warehouse = get_requests(warehouse, int(request[1]), int(request[2])) 
			print_warehouse(warehouse) 
		else: 
			print "Hi dude!" 
			warehouse = store_requests(warehouse, random.randint(1,12), int(request[1]), int(request[2])) 
			print_warehouse(warehouse)
	

''' 
def test_requests(): 
	requests = ["STORE 3 4 100", "STORE 4 5 100", "STORE 1 1 100", "STORE 9 2 100", "STORE 11 3 100", "STORE 12 2 100", "STORE 2 1 100", 
				"GET 4 20", "GET 3 20", "GET 2 20", "GET 1 20", "GET 5 20", "STORE 3 4 100", "STORE 7 2 100", "STORE 8 1 100", ]

def break_requests(request): 
	request = request.split(' ') 
	if(request[0]) == "GET": get_requests()
''' 
test() 
