
f1 = open("20101539_Umme Abira Azmary_CSE422_11_Assignment03_Summer2024_InputFile1.txt", "r")
import random
def AB_pruning(depth, state, alpha, beta):
    child = 2
    given_depth = 5

    if depth == given_depth:
        return random.choice([-1, 1])


    if state:
        eval = -10000000000000     #negative infinity
        for x in range(child):
            val = AB_pruning(depth + 1, False, alpha, beta)
            eval = max(eval, val)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return eval

    else:
        eval = +100000000000000    #positive infinity
        for x in range(child):
            val = AB_pruning(depth + 1, True, alpha, beta)
            eval = min(eval, val)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return eval

#print(AB_pruning(0, True, -100000, 100000000))

def game_playing(player1):
    results = []
    scorpio = 0
    subzero = 0
    rounds = 3
    c_player = None

    if player1 == 0:
        c_player = False
    else:
        c_player = True

    for x in range(1, rounds+1):
        win = AB_pruning(0, c_player, -10000000, 100000000)
        if win == -1:
            scorpio +=1
            results.append(f"Winner of Round {x}: Scorpion")
        else:
            subzero+= 1
            results.append(f"Winner of Round {x}: Sub-Zero")

        if c_player == True:
            c_player = False
        else:
            c_player = True


    if scorpio > subzero:
        T_win = "Scorpian"
    else:
        T_win = "Sub-Zero"

    print(f"Game Winner: {T_win}")
    print(f"Total Rounds Played: {rounds}")
    for p in results:
        print(p)

initial_player = f1.readline()
ini_player = int(initial_player)

game_playing(ini_player)