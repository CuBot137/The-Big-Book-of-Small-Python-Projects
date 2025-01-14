import random
import time


LEFT_WIDTH = 20
RIGHT_WIDTH = 20
GAP_WIDTH = '      '

while True:
    t = random.randint(-1, 1)
    if t == -1:
        LEFT_WIDTH = LEFT_WIDTH - 1
        RIGHT_WIDTH = RIGHT_WIDTH + 1
    elif t == 1:
        LEFT_WIDTH = LEFT_WIDTH + 1
        RIGHT_WIDTH = RIGHT_WIDTH - 1
        
    l = '#'*LEFT_WIDTH
    r = '#'*RIGHT_WIDTH
    cave = l + GAP_WIDTH + r
    print(cave)
    time.sleep(0.8)
    
