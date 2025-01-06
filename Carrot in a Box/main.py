import random

RED_BOX = False
GOLD_BOX = False


def game_start():
    global p1_name, p2_name, p1, p2
    print('Welcome to Carrot in a Box!')
    p1_name = input('Enter your name: ')
    p2_name = input('Enter your name: ')

    p1 = (RED_BOX, p1_name)
    p2 = (GOLD_BOX, p2_name)

    print(f'There are 2 boxes in front of you. One belongs to {p1_name} and one belongs to {p2_name}.')
    print('The game works by having 1 player look inside their box and see if they have the carrot or not. The other player must then decide whether or not they want to swap boxes')

    assign_carrot()
    
    r = random.randint(0,1)
    if r == 0:
        print(f'{p1_name} goes first')
        print('Look inside your box...')
        check_box(p1)
    else:
        print(f'{p2_name} goes first')
        print('Look inside your box...')
        check_box(p2)
        
    


def assign_carrot():
    r = random.randint(0,1)
    if r == 0:
        RED_BOX = True
        GOLD_BOX = False
    else:
        GOLD_BOX = True
        RED_BOX = False
    

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
            
game_start()