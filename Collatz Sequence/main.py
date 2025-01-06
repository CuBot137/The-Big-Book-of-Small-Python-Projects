print('The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:')
print("""If n is even, the next number n is n / 2.
If n is odd, the next number n is n * 3 + 1.
If n is 1, stop. Otherwise, repeat.""")

while True:
    n = input('Enter a starting number (greater than 0) or QUIT:\n>')
    if n.lower() is 'quit':
        break
    else:
        n = int(n)
        sequence = [n]
        x = n
    while n > 1:
        if n % 2 == 0:
            n = n /2
            sequence.append(n)
        elif n % 2 == 1:
            n = n * 3 + 1
            sequence.append(n)
        elif n == 1:
            sequence.append(n)
            break
       
    print(f'Collatz sequence for {x} is {sequence}' ) 
    