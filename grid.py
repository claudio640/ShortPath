# Define path_find as instructed in the email
def path_find(n, start_loc, goal_loc, values):
	x_shift = [0,0,-1,1]		#x_shift and y_shift will serve to shift the parent node either up, down, left or right
	y_shift = [-1,1,0,0]
	min_length = 10000		#Initialize min_lenght to a large number (as initial number for testing)
	visited = values		#visited will be an nxn map (initialized with the original values) where -1 entries will imply visited 						nodes in a path. This will serve as a way to stop the algorithm from visiting nodes it already has been
	
	import Queue			#Create a FIFO queue that will hold the nodes to expand on. A node will be comprised of 4 components:
	q = Queue.Queue()		#Current location, Path taken, Lenght of path, Visited array described earlier (in that order)

	q.put((start_loc, [start_loc], 0, visited))	#Place start_loc into the queue as defined above


	while not q.empty():		#While there is still nodes to expand on, remove the node from the queue
		test = q.get()
		
		if test[0] == goal_loc and test[2]<min_length:		#Check whether a path has reached the goal AND if the path length is 	
			min_length = test[2]				#less than the current min_length. If so, change the values of 
			best_path = test[1]				#min_length and best_path
		else: 
			for i in range(0,4):				#Otherwise, loop through all 4 possible directions for a path to take
				row = test[0][0] + x_shift[i]		#NOTE test[0][0] will be the first input of current location (row)
				col = test[0][1] + y_shift[i]

#Check whether the new row and col is still in the grid of values AND whether this new location does not have a -1 in the visited array. If these are all satisfied, set the parent node in the visited array to -1 and place the new child node into the queue after updating all node components.				
				if (row>0 and row<=n and col>0 and col<=n and test[3][row-1][col-1]!=-1):			
					test[3][test[0][0]-1][test[0][1]-1]=-1
					q.put(((row,col), test[1]+[(row,col)], test[2]+1+values[row-1][col-1], test[3]))
			
	return best_path		#The best_path will be returned once all possible paths are considered.

##TESTING

#n = 8	
#start_loc = (2,3)
#goal_loc = (8,7)
#values = [[4,3,3,4,2,3,1,2],[2,4,6,1,3,4,2,2],[3,2,1,5,4,5,3,2],[2,9,3,4,12,5,1,2],[7,4,9,3,3,2,4,2],[3,9,11,3,2,1,8,4],[6,1,1,6,2,5,6,1],[1,14,19,9,4,1,5,2]]

#n = 5	
#start_loc = (1,1)
#goal_loc = (5,4)
#values = [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]

#n = 3
#start_loc = (1,1)
#goal_loc = (3,1)
#values = [[3,1,2],[6,1,3],[2,1,5]]

least_cost_path = path_find(n,start_loc,goal_loc,values)
print(least_cost_path)

