import sys

password = input("Please enter a PW:  ")
attempt_counter = 1
while password != 'opensesame':
    if attempt_counter > 3:
        sys.exit("Too many attempts!")
    password = input("Invald PW, try again:  ")
    attempt_counter += 1
print("Welcome to the SSPWW!")