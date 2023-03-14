box = {k:"_" for k in ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]}

cIndex = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def game_state(p):

    v = list(box.values())

    print("  1 2 3\n1 {} {} {}\n2 {} {} {}\n3 {} {} {}".format(*v))

    for i in cIndex:

        if all(x == p for x in [v[i[0]], v[i[1]], v[i[2]]]):

            exit(f"Player {p} won!")

    if not "_" in box.values():

        exit("The match was a draw!")

def attempt(p):

    pos = {"row":None, "column":None}

    for key,value in pos.items():

        while not value in [str(i) for i in range(1,4)]:

            value = input(f"Player {p}, which {key} do you play?: ")

            if value == "quit":

                exit("You quit the game.")

        pos.update({key:value})

    box_num = pos.get("row") +","+ pos.get("column")

    attempt(p) if box.get(box_num) in ["X","O"] else box.update({box_num:p})

while True:

    game_state("O")

    attempt("X")

    game_state("X")

    attempt("O")
