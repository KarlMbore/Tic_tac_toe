

def display_board():
    global game
    global one
    global two
    global three
    one = []
    two = []
    three = []

    one = [i for i in range(1,4)]
    two = [i for i in range(4,7)]
    three = [i for i in range(7,10)]


    game = [one, two, three]
display_board()

def box_look():
    for row in game:
        for item in row:
            print(item, end = " ")
        print()
    print()
box_look()

def enter_move():
    index_play = int(input("where do u want to play: "))
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == index_play:
                if game[i][j] != "o" and game[i][j] != int:
                    game[i][j] = "x"
                return game
            
def free_fields():
    global slots_available
    slots_available = []
    free_slot_1 = ()
    free_slot_2 = ()
    free_slot_coordinates = ()
    for i in range(len(game)):
        for j in range(len(game[i])):
            free_slot_1 = i,
            free_slot_2 = j,
            free_slot_coordinates = free_slot_1 + free_slot_2
            checking_type = type(game[i][j])
            if checking_type == int:
                slots_available.append(free_slot_coordinates)
    print(slots_available)


for i in range(len(game)):
    enter_move()
    box_look()
    free_fields()