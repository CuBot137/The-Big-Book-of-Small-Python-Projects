import random


num = [1,2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
player_money = 5000

def generate_card():
    rn = random.choice(num)
    rs = random.choice(suits)
    card_shape = f"""
    ___
    |{rn}   |
    | {rs}  |
    |___{rn}|
    """
    return card_shape

print('Welcome to Black Jack!')
print()