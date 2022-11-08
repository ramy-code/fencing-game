
def display_character(id,pos,state):
    display_head()
    display_hands_with_state(id,state)
    display_legs()

def display_head():
    print("  O")

def display_hands_with_state(id,state):
    if state == 0:
        display_hands_rest(id)
    if state == 1:
        display_hands_attack(id)
    if state == 2:
        display_hands_defense(id)

def display_hands_attack(id):
    if id == 1 :
        print(" /|\\_")
    elif id == 2 :
        print("_/|\\")
    print("  |")
def display_hands_rest(id):
    if id == 1 :
        print(" /|\\")
        print("  | \\")
    elif id == 2 :
        print(" /|\\")
        print("/ | ")        
def display_hands_defense(id):
    if id == 1:
        print(" /|\\|")
        print("  |")
    elif id == 2:
        print("|/|\\")
        print("  |")
def display_legs():
    print(" / \\")
display_character(1,0,1)