# TODO Create an empty list to maintain the player names
players = []


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
players_add = input("Would you like to add a player to the list?  (Yes/No)  ")
while players_add.lower() == "yes":
    player_name = input("\nEnter the name of the player to add to the team.: ")
    players.append(name)
    add_player = input("Would you like to add a player to the list?  (Yes/No)  ")
    
 
# TODO print the number of players on the team
print("\nThere are {} players on the team.".format(len(players))   

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in players:
      print("Player {}: {}".format(player_number, player))
      player_number +=1
      


# TODO Select a goalkeeper from the above roster
goalkeeper_select = input("Who should be the goalkeeper? Select by selecting the player Number." "(1-{})".format(len(players))

goalkeeper = int(goalkeeper)

                          
# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great! The goalkeeper of your team is {}".format(players[goalkeeper - 1]))                         
                          

