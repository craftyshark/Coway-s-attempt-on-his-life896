
"""
First attempt at Game of life, simple output for now
If time allows, will try to implement pretty animation
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


ON = 1
OFF = 0
states = [ON, OFF]



def eGlide(grid, N): 
	grid[3,1] = ON
	grid[1,2] = grid[3,2] = ON
	grid[2,3] = grid[3,3] = ON

def gosperGun(grid, N):
	grid[26,2] = ON
	grid[24,3] = grid[26,3] = ON
	grid[14,4] = grid[15,4] = grid[22,4] = grid[23,4] = grid[36,4] = grid[37,4] = ON
	grid[13,5] = grid[17,5] = grid[22,5] = grid[23,5] = grid[36,5] = grid[37,5] = ON
	grid[2,6] = grid[3,6] = grid[12,6] = grid[18,6] = grid[22,6] = grid[23,6] = ON
	grid[2,7] = grid[3,7] = grid[12,7] = grid[16,7] = grid[18,7] = grid[19,7] = grid[24,7] = grid[26,7] = ON
	grid[12,8] = grid[18,8] = grid[26,8] = ON
	grid[13,9] = grid[17,9] = ON
	grid[14,10] = grid[15,10] = ON

def fPent(grid, N):
	grid[101,100] = grid[102,100] = ON
	grid[100,101] = grid[101,101] = ON
	grid[101,102] = ON




def gliderLight(grid, N):
	
	grid[2,1] = grid[5,1] = ON
	grid[1,2] = ON
	grid[1,3] = grid[5,3] = ON
	grid[1,4] = grid[2,4] = grid[3,4] = grid[4,4] = ON
	



	


#adding in some extra variables for animations, including one extra 4th variable I don't quite understand but
#is being sent by animation when calling updateGrid
def updateGrid(fillerVar, nextFrame, grid, N): 

	#Here we will updoot our grid. After that, back in the while loop, print a new grid

	#we need to copy the grid, we will place the FUTURE value after this update in future grid
	futureGrid = grid.copy()

	
	for x in range(N):
		for y in range(N):

			#add together a cell's 8 homies
			# we'll ur 'toriodal bounder conditions, ei, we'll basically have any values that 
			# go over 'wrap around' so to speak 
			nearSum = int(grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
				grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N])

			#deBuggin 
			"""
			print((grid[(x-1)%N, (y-1)%N] + grid[x, (y-1)%N] + grid[(x+1)%N, (y-1)%N] +
				grid[(x-1)%N, y] + grid[(x+1)%N, y] +
			   grid[(x-1)%N, (y+1)%N] + grid[x, (y+1)%N] + grid[(x+1)%N, (y+1)%N]))
			
			print( ((x-1)%N, (y-1)%N), (x, (y-1)%N), ((x+1)%N, (y-1)%N),
				((x-1)%N, y) ,((x+1)%N, y) , 
				((x-1)%N, (y+1)%N) , (x, (y+1)%N) , ((x+1)%N, (y+1)%N))
			print(nearSum)
			"""

			#Conwhey thyme
			if grid[x, y] == ON:
				#if it's on and there's less than 2 or more than three, ded				
				if (nearSum < 2) or (nearSum > 3):
					futureGrid[x, y] = OFF
			else:
				#Reproduction
				if nearSum == 3:
					futureGrid[x, y] = ON


	#update the now current recalculated grid, set the next frame and return it animation
	grid[:] = futureGrid[:]
	nextFrame.set_data(grid)

	return nextFrame



def main():

	#set our grid size, have fun and change this to whatever you like :) 
	N = 200

	#create Grid
	grid = np.array([])

	#oneSquare(grid, N)

	#For now lets just toss in random numbers, nice format stuff later 
	#Uncomment below for random starting seeds
	grid = np.random.choice(states, N*N, p=[0.6, 0.4]).reshape(N,N)

	#first line is just rechaping the grid two have two dementions, is required before adding any elements to grid
	#grid = np.zeros(N*N).reshape(N, N)
	#eGlide(grid, N)

	#having fun with new objects
	#grid = np.zeros(N*N).reshape(N, N)
	#gliderLight(grid, N)

	#grid = np.zeros(N*N).reshape(N, N)
	#gosperGun(grid, N)

	#grid = np.zeros(N*N).reshape(N, N)
	#fPent(grid, N)

	"""
	created ealier when just outputing via print to make sure the actual conway code worked. 
	pls ignore
	i=0

	print(grid)
	print("first grid")

	while i < 1000:
		i += 1
		updateGrid(grid, N)

		print(grid)




	#our actual output
	print(grid)

	"""


	#Change me to make the animation go faster or slower
	updootSpeed = 20

	#reusing code from my CSCI 191T project. if work, why fix? 
	#set up, create figure that is used to draw objects, and axes subplot for animation
	gridFig, axES = plt.subplots()

	#set up 
	
	nextFrame = axES.imshow(grid, cmap=plt.cm.gray)

	plt.get_current_fig_manager().window.state('zoomed')
	#a lil libray useage I don't completely understand in order to make things print pretty
	brainsAnimation = animation.FuncAnimation(gridFig, updateGrid, fargs=(nextFrame, grid, N ), frames=60 , interval=updootSpeed ) 

	#actually showing the animation
	plt.show()



if __name__ == '__main__':
		main()
