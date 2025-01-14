import random
import time

def game_start():
    global p1_name, p2_name, p1, p2, r, RED_BOX, GOLD_BOX
    print('Welcome to Carrot in a Box!')
    p1_name = input('Enter your name: ')
    p2_name = input('Enter your name: ')

    RED_BOX, GOLD_BOX = assign_carrot()
    
    p1 = [RED_BOX, p1_name]
    p2 = [GOLD_BOX, p2_name]

    print(f'There are 2 boxes in front of you. One belongs to {p1_name} and one belongs to {p2_name}.')
    print('The game works by having 1 player look inside their box and see if they have the carrot or not. The other player must then decide whether or not they want to swap boxes')
    
    r = random.randint(0,1)
    if r == 0:
        print(f'{p1_name} goes first')
        print('Look inside your box...')
        player_ready_to_check_box(p1)
    else:
        print(f'{p2_name} goes first')
        print('Look inside your box...')
        player_ready_to_check_box(p2)
    
    decide_to_swap_boxes()
    if True in p1:
        print(f'{p1_name} has the carrot!!!\nGame over!!')
        

def assign_carrot():
    ran = random.randint(0,1)
    if ran == 0:
        RED_BOX = True
        GOLD_BOX = False
    else:
        GOLD_BOX = False
        RED_BOX = True
    return RED_BOX, GOLD_BOX
    

def check_box(p):
    if p1_name in p:
        if True in p:
            print(f'{p1_name}, you have the carrot!')
        else:
            print(f'{p1_name}, you do not have the carrot.')
    else:
        if True in p:
            print(f'{p2_name}, you have the carrot!')
        else:
            print(f'{p2_name}, you do not have the carrot.')
            
def player_ready_to_check_box(p):
    while True:
        i = input('Player, are you ready to open the box. Make sure your oponent is not looking...\nY or N\n>')
        if i.lower() == 'y':
            check_box(p)
            time.sleep(5)
            print('\n' * 100)
            break
        elif i.lower() == 'n':
            print('Alright, let\'s try again.')
            

def decide_to_swap_boxes():
    if r == 0:
        i = input(f'{p2_name}, do you want to swap the boxes?\nY or N\n>')
        if i.lower() == 'y':
            print('Swapping boxes')
            p1[0], p2[0] = p2[0], p1[0]
        else:
            print('Not swapping boxes')
    else:
        i = input(f'{p1_name}, do you want to swap the boxes?\nY or N\n>')
        if i.lower() == 'y':
            print('Swapping boxes')
            p1[0], p2[0] = p2[0], p1[0]
        else:
            print('Not swapping boxes')
    
            
game_start()