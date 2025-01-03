print('Welcome to Ceaser Hacker.')
print('Enter an encrypted message and we will brute force it with every possible key')

CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt():
    decrypted_list = []
    encrypted_message = input('Enter the encrypted message\n>').upper()
    decrypted_message = ''
    for j in range(26):
        if decrypted_message:
            decrypted_message += ', '
        for i in range(len(encrypted_message)):
            encrypted_char = encrypted_message[i]
            characters_index = CHARACTERS.index(encrypted_char)
            decrypted_message += CHARACTERS[(characters_index - j) % len(CHARACTERS)]
    
   
    print('Decrypted message:', decrypted_message)
    
decrypt()

