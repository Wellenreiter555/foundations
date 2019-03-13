TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate_price(tickets_requested):
    return (tickets_requested * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} remaining Tickets available!".format(tickets_remaining))
    user_name = input("What is your Name?  ")
    tickets_requested = input("Hey {} how many Tickets would you like to buy? ".format(user_name))
    
    try:
        tickets_requested = int(tickets_requested)
        if tickets_requested > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Issue. {}. Please try again".format(err))
    
    else:
        price = calculate_price(tickets_requested)
        print("The {} Tickets would cost {}$, {}.".format(tickets_requested, price, user_name))
        proceed = input("Do you want to proceed and buy the tickets {}? \n(Yes or No?)".format(user_name))
        if proceed.lower() == "yes":
            tickets_remaining -= tickets_requested
            print("SOLD!")
        else:
            print("Thank you anyway, {}!".format(user_name))

print("Sorry all tickets are sold out now!")

        

    
    
    


  

