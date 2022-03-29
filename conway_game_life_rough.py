
"""
First attempt at Game of life, simple output for now
If time allows, will try to implement pretty animation
"""


import sys, argparse
import numpy as np

ON = 1
OFF = 0
states = [ON, OFF]


def updateGrid(grid, N): 

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
			

			
	grid[:] = futureGrid[:]

def main():
	#set our grid size 
	N = 10

	#create Grid
	grid = np.array([])

	#For now lets just toss in random numbers, nice format stuff later 
	grid = np.random.choice(states, N*N, p=[0.3, 0.7]).reshape(N,N)

	i=0

	print(grid)
	print("first grid")

	while i < 1000:
		i += 1
		updateGrid(grid, N)

		print(grid)




	#our actual output
	print(grid)



if __name__ == '__main__':
		main()