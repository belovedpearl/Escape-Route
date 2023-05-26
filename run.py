# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def red_door():
    """
    red room experience

    """
    treasure_box = ["diamond", "gold", "silver", "sword"]
    print("You have come into the red room.")
    print("There lies a treasure box to the left of the room.")
    print("Right beside the box is a guard directly opposite the door.\nA very giant one at that...")
    print("Pick one: Treasure, Box, Left, Guard, Right, Giant")
    action = input("What do you pick?\n")

    if action.lower() in ["treasure", "box", "left"]:
        print("Wowww... Treasure!!!")

        print("Press 1 to open the box")
        print("Press 2 to leave it")
        choice = input("Enter your choice\n")
        if choice == "1":
            print("Let's see what's in there.")
            print("The guard is still fast asleep.")
            print("You find some....")

            for treasure in treasure_box:
                print(treasure.capitalize())
        
            print("What will you like to do with your found items?")
            length_treasure_box = len(treasure_box)

            print(f"Take all {length_treasure_box} treasures; press 1")
            print("Continue the adventure, press 2")

            treasure_choice = input("Press 1 or 2\n")

            if treasure_choice == "1":
                # Remove sword from the treasure box
                treasure_box.remove("sword")
                print("You just got a new sword from the box. This sword is very sharp and pointy.")
                print("I think you can face more dragons.")

                treasure_list = ",".join(treasure_box)
                print(f"You also found {treasure_list} in the box.") 

                # Make a copy of the remaining items in treasure box
                copy_treasure_box = treasure_box[:]

                for treasure in copy_treasure_box:
                    # Remove each item from the treasure box
                    treasure_box.remove(treasure)
                print("Now, you are fully equiped... Well done")
                
                # Drop the old sword into the treasure box
                treasure_box.append("old sword")

                print(f"You close the treasure box, it now has only the {treasure_box[0]}")
                print("Who knows someone might need it. Smiles....")
                print("Now, you need to get past the guard. Be careful not to wake him!!!")
            elif treasure_choice == "2":
                print("It will still be here, right after I get past this guard.")
        elif choice == "2":
            print("There is no need for treasure in this hole. Let's find our way out of here.")
    elif action.lower() in ["guard", "right", "giant"]:
        print("OK, Let's take the guard's path")
    else:
        print("There is no option here. I think we can quietly go through the guard.")
    
                    

                





        elif choice == "2":
            print("No need for treasure, I need to find my way out.")

def you_died(reason):
    """
    prints reason why the game is ending 
    """
    print(f"{reason}, you can no longer continue! Good job")
    exit()

def green_door():
    """
     Green room experience
     User selects what to do
    """
    print("There live a great dragon")
    print("Staring at you.")

    action = input("Do you FLEE or STAY?\n")
    if action.lower() == "flee":
        start_adventure()
    else:
        you_died("The dragon ate you")

    
def start_adventure():
    """
     Allows user to choose a door to continue the game
     Calls on other function for more experience
    """
    print("You fell into a dungeon. Haaaaa!!!!")
    print("You find yourself in a room with two doors...")
    print("The doors are GREEN and RED color.")
    
    choice = input("Which one will you choose?\n")

    if choice.lower() == "green":
        green_door()
    elif choice.lower() == "red":
        red_door()
    else:
        print("Sorry, you have the wrong answer.\nChoose either green or red to continue...")

def get_player_name():
    """
     Prompts user to enter name
    """
    name = input("Enter your name: \n")
    print(f"Your name is {name}")
    return name

def main():
    """
     Starts the game
    """
    
    player_name = get_player_name()
    
    start_adventure()

main()