
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



	


#adding in some extra variables for animations, including one extra 4th variable I don't quite understand but
#is being sent by animation when calling updateGrid
def updateGrid(fillerVar, nextFrame, grid, N): 

	#Here we will updoot our grid. After that, back in the while loop, print a new grid

	#we need to copy the grid, we will place the FUTURE value after this update in future grid
	futureGrid = grid.copy()

	
	for y in range(N):
		for x in range(N):

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
			"""
			"""
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
	N = 100

	#create Grid
	grid = np.array([])

	#oneSquare(grid, N)

	#For now lets just toss in random numbers, nice format stuff later 
	#Uncomment below for random starting seeds
	#grid = np.random.choice(states, N*N, p=[0.15, 0.85]).reshape(N,N)

	#first line is just rechaping the grid two have two dementions, is required before adding any elements to grid
	grid = np.zeros(N*N).reshape(N, N)
	eGlide(grid, N)


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


	#reusing code from my CSCI 191T project. if work, why fix? 
	#set up, create figure that is used to draw objects, and axes subplot for animation
	gridFig, axES = plt.subplots()

	#set up 
	
	nextFrame = axES.imshow(grid, cmap=plt.cm.gray)


	#a lil libray useage I don't completely understand in order to make things print pretty
	brainsAnimation = animation.FuncAnimation(gridFig, updateGrid, fargs=(nextFrame, grid, N ) ) 

	#actually showing the animation
	plt.show()



if __name__ == '__main__':
		main()