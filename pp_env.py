MAX_CAPACITY = 10000 

class Env: 
	
	#Initialise variables 
	def __init__(self, nRacks, nItems): 
		self.nRacks = nRacks 
		self.nItems = nItems 
		self.warehouse = {a: (0,0) for a in range(1, nRacks+1)} 

	def print_warehouse(self): 
	    print 
	    print "    I    " 
	    print 
	    for i in self.warehouse: 
		print str(i) + "->" + str(self.warehouse[i]) + "\t" 
		if i % 3 == 0: 
		    print 
	    print "    O    "
	
	def cyclic(self, rack): 
	    if rack == 1: 
		return self.nRacks  
	    else: 
		return rack-1 

	def warehousefull(self,): 
	    count = 0 
	    for i in range(1, self.nRacks+1): 
		if (self.warehouse[i] == (0,0)): break 
		else: count = count + 1 
	    if (count == self.nRacks): return True
	    else: return False 
	
	def Store(self, rack, item, quantity): 
	    #global MAX_CAPACITY
	    if (rack not in self.warehouse): 
	    	print "No rack {} in warehouse".format(rack) # No such rack exists  
	    elif self.warehouse[rack] == (0,0): # Empty rack 
		 self.warehouse[rack] = (item, quantity) 
		 print("Stored item {} Successfully in an empty rack {} ".format(item, rack)) 
	    elif ((self.warehouse[rack][0] == item) and (self.warehouse[rack][1] + quantity > MAX_CAPACITY)): 
	    	self.warehouse[rack] = (item, MAX_CAPACITY) 
	    	print "Max capacity of rack over. Shifting remaining quantity {} to another rack! --> ".format((self.warehouse[rack][1] + quantity) - MAX_CAPACITY), 
	    	print "cycle rack:", str(self.cyclic(rack)), 
		self.Store(self.cyclic(rack), item, (self.warehouse[rack][1] + quantity) - MAX_CAPACITY) 
	    elif (self.warehouse[rack][0] == item): # Rack already has some qauntity of that item 
		self.warehouse[rack] = (item, self.warehouse[rack][1]+quantity) 
		print "Updated Quantity of item {} in rack {} ".format(item, rack) 
	    elif (self.warehousefull() == True): 
	    	print "Warehouse is Full!" 
	    else: # Some other item is in that rack 
		#print "----------------------------------------------------------" 
		print "Rack {} has item {}. Kindly store item {} somehere else! --> ".format(rack, self.warehouse[rack][0], item),  
		print "cycle rack:", str(self.cyclic(rack)), 
		self.Store(self.cyclic(rack), item, quantity) 

	
	
	def rewards(self, rack): 
	    
	    ''' 
	    1st rack = 100 
	    2nd rack = 200 
	    .
	    .
	    .
	    last rack = nRacks * 100 (nearest to the output bay) 
	    ''' 
	    
	    reward = rack*100 
	    return reward 

	def get_rack_number(self, item): #needs optimization #future (delayed) rewards to be considered 
		rack = 0 #base case. if rack number does not exist, rack = 0 will be returned 
		for i in self.warehouse: 
			if item in self.warehouse[i]: 
			     rack = i #Rack number 
		return rack 
	
	def Get(self, item, quantity): 
	    rack = self.get_rack_number(item)

	    #immediate reward 
	    reward = -100

	    #currently assuming all get requests are below MAX_CAPACITY  
	    if (rack == 0): print "Item {} not in warehouse".format(item) # No such rack exists  
	    elif self.warehouse[rack] == (0,0): # Empty rack 
		 print "Rack {} is an empty rack ".format(rack)
	    elif (self.warehouse[rack][0] == item): # Rack already has some quantity of that item 
		#immediate reward 
		reward = self.rewards(rack)     
		if (self.warehouse[rack][1] >= quantity): 
		    if (self.warehouse[rack][1]-quantity == 0): self.warehouse[rack] = (0,0) 
		    else: self.warehouse[rack] = (item, self.warehouse[rack][1]-quantity) 
		    print "Delivery of item {} Successful".format(item) 
		else: 
		    self.warehouse[rack] = (0,0) 
		    print "Quantity {} of item {} is unavailable currently. Delivered {} quantity as of now! ".format(quantity, item, self.warehouse[rack][1])
	    else: # Some other item is in that rack 
		print "Item {} asked for is in rack {}. Kindly Get is from there. Thank you :)".format(item, rack) 

	    return rack, reward 

	    '''         
	    done = False 
	    info = 'info' 
	    return [warehouse, reward, done, info] 
	    ''' 
	


	def test(self): 
		#print self.nRacks 
		#print self.nItems 
		print self.print_warehouse() #self.warehouse 
		
if __name__ == "__main__": 
	#Object of environment warehouse 
	env = Env(12,5) 
	print"Testing Store() " 
	env.Store(1, 1, 100) #rack, item, quantity 
	env.Store(2, 2, 10) 
	env.Store(5, 2, 10) 
	env.Store(11, 5, 10) 
	env.Store(8, 4, 10) 
	# Testing of Get() function 
	print"Testing Get() " 
	env.Get(5, 5) 
	env.Get(5, 5) 
	env.Get(5, 5) 
	env.Get(2, 4) 
	env.Get(11, 10) # No rack 100 
	env.Get(1,100) # Rack 11 already has item 5 

	env.test() 
