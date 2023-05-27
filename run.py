# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os

os.system("clear")
""" ANSI color codes """
COLORS = {\
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "brown": "\033[0;33m",
    "blue": "\033[0;34m",
    "purple": "\033[0;35m",
    "cyan": "\033[0;36m",
    "cyan-background": "\u001b[46m",
    "black_background": "\u001b[40m",
}
def colorRep(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]",COLORS[color])
    return text

def print_art():
    f = open("title_art.txt","r")
    ascii = "".join(f.readlines())
    title_tag = colorRep(ascii)
    print(title_tag)

def guard():
    """
    player choose to either attack, sneak or check
    attack: player dies while fighting, game over
    sneak: player sneaks past the guard, wins the game
    check: player
    """
    print("You are now approaching the guard")
    print("What do you think its best to do?")
    # Player's response to seeing the guard
    guard_response = {
        "attack": "You run to the guard thinking you are fast enough, but he caught you.",
        "sneak": "You approach the guard, still sleeping. Reaching for the door, you gently opened it and slip out.",
        "check": "You see that he guard is still sleeping, you need to get to the door, don't waste your time."
    }
    while True:
        next_action = input("Attack | Sneak | Check \n").lower()
        if next_action in guard_response.keys():
            if next_action == "sneak":
                print("You have just slipped through the door.")
                print("You are now outside, free atlast!")
                return
            elif next_action == "attack":
                you_died("Guard woke up, reached for his weapons.\nGAME OVER")
            elif next_action == "check":
                print("You need to think fast before we are caught.")
                you_died("Guard woke up.\n GAME OVER")
            else:
                print("Not sure what you meant there.Try again")



def red_door():
    """
    red room experience
    user choose options
    removes treasures from the treasure box
    drop the old weapon back into the box
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
                # List out the treasures
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
                
                # Join the remaining content of the treasure_box
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
    guard()
                    

def you_died(reason):
    """
    prints reason why the game is ending 
    """
    print(f"{reason}, you can no longer continue!")
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
    print(f"Your name is {name.upper()}")
    return name

def main():
    """
     Starts the game
    """
    print_art()

    player_name = get_player_name()
    
    start_adventure()

    print("THE END")
    print(f"THANK YOU FOR PLAYING {player_name.upper()}...")

main()

