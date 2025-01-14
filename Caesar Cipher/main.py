print('Welcome to Ceaser Cipher.')
print('Enter a message and the number of letters you want to offset it by')

CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt():
    message = input('Enter the message you want to encrypt\n>').upper()
    num = int(input('Enter the key to use\n>'))
    encrypted_message = ''

    for i in range(len(message)):
        message_char = message[i]
        characters_index = CHARACTERS.index(message_char) - num
        encrypted_message += CHARACTERS[characters_index]
    print('Encrypted message:', encrypted_message)
    return encrypted_message

def decrypt():
    message = input('Enter the message you want to decrypt\n>').upper()
    num = int(input('Enter the key you used\n>'))
    decrypted_message = ''
    for i in range(len(message)):
        message_char = message[i]
        characters_index = CHARACTERS.index(message_char) + num
        decrypted_message += CHARACTERS[characters_index]
    print('Decrypted message:', decrypted_message)
    return decrypted_message
  
        
while True:
    print('What do you want to do:\nE or D')
    choice = input('>')
    if choice.upper() == 'E':
        encrypt()
    elif choice.upper() == 'D':
        decrypt()
    else:
        print('Invalid choice. Please try again.')