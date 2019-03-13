name = input("What is your name? ")
answer = input("Enter Yes or No? ")

while answer.lower() != "yes":
    print("That is totally fine, {}, while loops in Python repeat as long as a certain Boolean condition is met. Do you now understand while Loops in Python, {}? ".format(name, name))
    answer = input("Enter Yes or No? ")
else:
    print("That is great, {}, keep going!".format(name))
    
