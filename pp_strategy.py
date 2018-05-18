from pp_env import Env 

env = Env(12,5) 


class Util: 
	def __init__(self, warehouse): 
		

class RandomStrategy: 
	def __init__(self): 
		
		
	def random_strategy(): 
	    rack = random.randint(1,12)  
	    return rack 
	    
	def total_rewards(): 
	    total_rewards = 0 
	    requests_list = requests() 
	    for req in requests_list: 
		r = req.split(' ') 
		reward = 0 
		if (r[0].strip() == "STORE"): 
		    rack = random_strategy() #random racks allocated 
		    #print rack 
		    Store(rack, int(r[1]), int(r[2])) 
		else: #Get request 
		    rack, reward = Get(int(r[1]), int(r[2])) 
		    total_rewards = total_rewards + reward 
	    #print_warehouse() 
	    print "Total Rewards =", total_rewards 
	    return total_rewards 

	def cum_rewards(): 
	    cumulative_rewards = 0 
	    reward_array = [] 
	    for i in range(100): #number of episodes 
		total = total_rewards() 
		reward_array.append(total) 
		cumulative_rewards = cumulative_rewards + total 
		total = 0 
	    print "Reward array =", reward_array 
	    print "Cumulative Rewards =", cumulative_rewards 
	    return cumulative_rewards 

	print_warehouse() 
	#c_rewards = cum_rewards() 
