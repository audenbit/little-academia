## colors class from Stack Overflow: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal 
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## items that make school
unlocked_items = []
# needs to be empty by end of game
unlockables = ["wood", "metal", "electricity", "desk chair", "laptop", "laptop cart", "class", "floor", "school"]
# sets default 
for i in range(3):
    unlocked_items.append(unlockables[i])

combos = {
    "metal+wood": "desk chair",
    "wood+metal": "desk chair",
    "metal+electricity": "laptop",
    "electricity+metal": "laptop",
    "laptop+laptop": "laptop cart",
    "laptop cart+desk chair": "class",
    "desk chair+laptop cart": "class",
    "class+class": "floor",
    "floor+floor": "school"
}

def check_combo_usable(inputted_combo):
    if inputted_combo in combos:
        return combos[inputted_combo]
    return None

logo = r"""
  _ _ _   _   _                            _                _       _ 
 | (_) | | | | |                          | |              (_)     | |
 | |_| |_| |_| | ___    __ _  ___ __ _  __| | ___ _ __ ___  _  __ _| |
 | | | __| __| |/ _ \  / _` |/ __/ _` |/ _` |/ _ \ '_ ` _ \| |/ _` | |
 | | | |_| |_| |  __/ | (_| | (_| (_| | (_| |  __/ | | | | | | (_| |_|
 |_|_|\__|\__|_|\___|  \__,_|\___\__,_|\__,_|\___|_| |_| |_|_|\__,_(_)
                                                                      
"""
print(f"{bcolors.CYAN}{bcolors.BOLD}{logo}{bcolors.ENDC}{bcolors.ENDC}")
print("Welcome to Little Academia! In this game, you are given three items (wood, metal, and electricity), and you will have to find out how to create a school just with those simple materials! Good luck! :)")

while True:
    print("\nWhat combo do you want to make? To input a combo, you format it like this: 'wood+wood'. You currently have: ")
    for item in unlocked_items:
        print(f"- {item}")
    
    combo_input = input("\nEnter your combo -> ")
    new_item = check_combo_usable(combo_input)
    
    if new_item:
        if new_item not in unlocked_items:
            unlocked_items.append(new_item)
            print(f"{bcolors.GREEN}Congrats! You have unlocked:{bcolors.ENDC} {bcolors.UNDERLINE}{new_item}{bcolors.ENDC}")
        else:
            print(f"{bcolors.YELLOW}You already have{bcolors.ENDC} {bcolors.UNDERLINE}{new_item}{bcolors.ENDC} {bcolors.YELLOW}unlocked.{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}Invalid combo. Try again.{bcolors.ENDC}")
    
    if "school" in unlocked_items:
        print(f"{bcolors.BOLD}Congratulations! You have successfully created a school!{bcolors.ENDC}")
        break
