
f1 = open("20101539_Umme Abira Azmary_CSE422_11_Assignment03_Summer2024_InputFile2.txt", "r")
def Pac_Minimax(node, depth, playerState, alpha, beta, leaf_lst, darkMagic, c):
    lst = []

    if depth == 3:
        return leaf_lst[node]

    if playerState == True:
        emVal = -1000000000000 # should be (-infinity)
        var = 0
        for x in range(2):

            val = Pac_Minimax(2*node+x, depth +1, False, alpha, beta, leaf_lst, darkMagic, c)

            emVal = max(emVal, val)
            if depth == 0:
                if emVal == val:
                    var = x

            alpha = max(alpha, val)
            if beta <= alpha:
                break
        if depth == 0:
            return (emVal, var)
        return emVal
    else:

        elVal = 1000000000000
        for y in range(2):
            val = Pac_Minimax(2*node+y, depth +1, True, alpha, beta, leaf_lst, darkMagic, c)
            lst.append(val)
            elVal = min(elVal, val)
            beta = min(beta, val)

            if beta <= alpha:
                break

        if darkMagic == True:
            elVal = max(lst)
            return elVal
        else:
            return elVal

def pacman_game(c):

    leaf_lst = [3, 6, 2, 3, 7, 1, 2, 0]

    pacman_magic = Pac_Minimax(0, 0, True, -100000000000000, 1000000000000000, leaf_lst, True, c)
    #print(pacman_magic)

    pacman_moves = Pac_Minimax(0, 0, True, -100000000000000, 1000000000000000, leaf_lst, False, c)

    if pacman_magic[0] - c > pacman_moves[0]:
        if pacman_magic[1] == 0:
            print(f"The new minimax value is {pacman_magic[0]-c}. Pacman goes left and uses dark magic.")
        else:
            print(f"The new minimax value is {pacman_magic[0]-c}. Pacman goes right and uses dark magic.")

    else:
        print(f"The minimax value is {pacman_moves[0]}. Pacman does not use dark magic.")

temp = f1.readline()
c = int(temp)

pacman_game(c)