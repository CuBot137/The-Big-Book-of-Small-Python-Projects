import copy, random, sys, time

WIDTH = 79
HEIGHT = 20

ALIVE = 'O'
DEAD = ' '

next_cells = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD
            
while True:
    print('\n'*50)
    cells = copy.deepcopy(next_cells)
    
    # Print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x, y], end='')
        print()
    print('Press Ctrl-C to quit.')
    
    # Calculate the next steps cells based on the current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edge: 
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            
            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # Top-left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 
                
            if cells[(x,y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                next_cells[(x, y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                next_cells[(x, y)] = ALIVE
            else:
                next_cells[(x, y)] = DEAD
                
            
    try:
        time.sleep(1)  # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.
