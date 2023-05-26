# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start_adventure():
    """
     Allows user to choose a door to continue the game
     Calls on other function for more experience
    """
    print("You fell into a dungeon. Haaaaa!!!!")
    print("You find yourself in a room with two doors...")
    print("The doors are green and red color.")
    
    choice = input("Which one will you choose?\n")

    if choice.lower() == "green":
        green_door()
    elif choice.lower == "red":
        red_door()
    else:
        print("Sorry, you have the wrong answer.\nChoose either red or blue to continue...")

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