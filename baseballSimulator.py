#baseballsim.py
#This program simulates n number of baseball games between two MLB baseball teams inputted by the user
#and then outputs the odds that either team will win

from baseball import *


def main():
    n, i, team1, team2, sPitcher1, rPitcher1, sPitcher2, rPitcher2 = intro()
    wincount1 = 0
    wincount2 = 0
    for i in range(n):
        print("\n")
        print("game number:", i + 1, "\n")
        score = oneGame(team1, team2, sPitcher1, rPitcher1, sPitcher2, rPitcher2)
        wincount1, wincount2 = results(n, score, team1, team2, wincount1, wincount2)

def intro():
    team1 = globals()[input("Enter the away team: ")]
    for i in range (len(team1.pitchers)):
        print ("(", i + 1, ") ", team1.pitchers[i], sep = "")
    sPitcher1 = int(input("Enter starting pitcher (pick the corresponding number): "))
    rPitcher1 = int(input("Enter relief pitcher (pick the corresponding number): "))
    team2 = globals()[input("Enter the home team: ")]
    for i in range (len(team2.pitchers)):
        print ("(", i + 1, ")", team2.pitchers[i], sep = "")
    sPitcher2 = int(input("Enter starting pitcher (pick the corresponding number): "))
    rPitcher2 = int(input("Enter relief pitcher (pick the corresponding number): "))
    n = int(input("how many games: "))
    return n, i, team1, team2, sPitcher1, rPitcher1, sPitcher2, rPitcher2

def atBat(batter, startingPitcher, reliefPitcher, inning):
    print ("batter: ", batter)
    if inning < 8:
        print ("pitcher:", startingPitcher)
        p = Player.status(batter, startingPitcher)
    else:
        print ("pitcher:", reliefPitcher)
        p = Player.status(batter, reliefPitcher)
    return p


def oneGame(team1, team2, sPitcher1, rPitcher1, sPitcher2, rPitcher2):
    inning = 1
    outs = 0
    score = [0,0]
    game = True
    ondeck = [0, 0]
    bases1 = [False, False, False, False, False]
    bases2 = [False, False, False, False, False]
    teams = [team1, team2]
    bases = [bases1, bases2]
    sPitcher = [sPitcher1, sPitcher2]
    rPitcher = [rPitcher1, rPitcher2]

    while game:
        if inning % 1 == 0:
            ups = 0
            downs = 1
        else:
            ups = 1
            downs = 0
        x = atBat(teams[ups].lineup[ondeck[ups]], teams[downs].pitchers[sPitcher[downs]-1], teams[downs].pitchers[rPitcher[downs]-1], inning)
        teams[ups].lineup[ondeck[ups]].statusList.append(x)
        if teams[ups].lineup[ondeck[ups]].statusList[-1] == 0:
            print ("Out")
        if teams[ups].lineup[ondeck[ups]].statusList[-1] == 1:
            print ("Single")
        if teams[ups].lineup[ondeck[ups]].statusList[-1] == 2:
            print ("Double")
        if teams[ups].lineup[ondeck[ups]].statusList[-1] == 3:
            print ("Triple")
        if teams[ups].lineup[ondeck[ups]].statusList[-1] == 4:
            print ("HOME RUN!")
        for i in range(3, 0, -1):
            if bases[ups][i]:
                bases[ups][i] = False
                if (i + x) < 4:
                    bases[ups][i + x] = True
                else:
                    score[ups] += 1
        bases[ups][x] = True
        ondeck[ups] += 1
        if bases[ups][0]:
            outs += 1
            bases[ups][0] = False
        if bases[ups][4]:
            score[0] += 1

        print(teams[ups])
        print("inning:", inning, " outs:", outs, " score:", score, sep="")
        print(bases[ups])
        bases[ups][4] = False
        print()

        if outs == 3:
            inning += .5
            bases[ups] = [False, False, False, False, False]
            outs = 0
        if ondeck[ups] == len(teams[ups].lineup):
            ondeck[ups] = 0
        if inning >= 10 and score[0] != score[1] and inning % 1 == 0:
            game = False
    return score

def results(n, score, team1, team2, wincount1, wincount2):
    print("Final Score", score)
    if float(score[0]) > float(score[1]):
        print (team1, "win!")
        wincount1 += 1
    if float(score[1]) > float(score[0]):
        print (team2, "win!")
        wincount2 += 1
    if n == (wincount1 + wincount2):
        print ()
        print (team1, ":", wincount1, sep = "")
        print (team2, ":", wincount2, sep = "")
        percentagewon1 = (wincount1/(wincount1 + wincount2)) * 100
        percentagewon2 = (wincount2/(wincount1 + wincount2)) * 100
        print (team1, " have a ", percentagewon1,"%", " chance of winning", sep = "")
        print (team2, " have a ", percentagewon2,"%", " chance of winning", sep = "")
    return wincount1, wincount2

if __name__ == '__main__':
    main()

"""
TODO:
-add ways for players on base to get thrown out
-add graphics
"""
