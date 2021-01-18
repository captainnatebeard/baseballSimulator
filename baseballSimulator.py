#!/usr/bin/env python3

"""
This program simulates n number of baseball games between
two MLB baseball teams inputted by the user
and then outputs the odds that either team will win
"""

from baseball import *


def main():
    n, team1, team2, s_pitcher1, r_pitcher1, s_pitcher2, r_pitcher2 = intro()
    win_count1 = 0
    win_count2 = 0
    for i in range(n):
        print("\n")
        print("game number:", i + 1, "\n")
        score = one_game(team1, team2, s_pitcher1, r_pitcher1, s_pitcher2, r_pitcher2)
        win_count1, win_count2 = results(n, score, team1, team2, win_count1, win_count2)


def intro():
    """
    takes no arguments, asks user to select two teams, and their pitchers
    and the number of games to simulate
    returns the number of games to simulate (n int), the away team (team1, Team)
    the home team (team2 Team), and the index of the starting and relief
    pitcher for both teams (s_pitcher1, s_pitcher2, r_pitcher1, r_pitcher2 int)
    """
    team1 = globals()[input("Enter the away team: ")]
    for i in range(len(team1.pitchers)):
        print("(", i + 1, ") ", team1.pitchers[i], sep="")
    s_pitcher1 = int(input("Enter starting pitcher (pick the corresponding number): "))
    r_pitcher1 = int(input("Enter relief pitcher (pick the corresponding number): "))
    team2 = globals()[input("Enter the home team: ")]
    for i in range(len(team2.pitchers)):
        print("(", i + 1, ")", team2.pitchers[i], sep="")
    s_pitcher2 = int(input("Enter starting pitcher (pick the corresponding number): "))
    r_pitcher2 = int(input("Enter relief pitcher (pick the corresponding number): "))
    n = int(input("how many games: "))
    return n, team1, team2, s_pitcher1, r_pitcher1, s_pitcher2, r_pitcher2


def at_bat(batter, starting_pitcher, relief_pitcher, inning):
    """
    takes as input a batter (batter Player), starting pitcher 
    (starting_pitcher, Pitcher), relief pitcher (relief_pitcher Pitcher), and
    the current inning in the simulated game (inning int)
    simulates a single at bat for a single player/pitcher interaction and
    prints some of the information to the screen
    """
    print("batter: ", batter)
    if inning < 8:
        print("pitcher:", starting_pitcher)
        p = Player.status(batter, starting_pitcher)
    else:
        print("pitcher:", relief_pitcher)
        p = Player.status(batter, relief_pitcher)
    return p


def one_game(team1, team2, s_pitcher1, r_pitcher1, s_pitcher2, r_pitcher2):
    inning = 1
    outs = 0
    score = [0, 0]
    game = True
    ondeck = [0, 0]
    bases1 = [False, False, False, False, False]
    bases2 = [False, False, False, False, False]
    teams = [team1, team2]
    bases = [bases1, bases2]
    s_pitcher = [s_pitcher1, s_pitcher2]
    r_pitcher = [r_pitcher1, r_pitcher2]

    while game:
        if inning % 1 == 0:
            ups = 0
            downs = 1
        else:
            ups = 1
            downs = 0
        x = at_bat(teams[ups].lineup[ondeck[ups]],
                   teams[downs].pitchers[s_pitcher[downs]-1],
                   teams[downs].pitchers[r_pitcher[downs]-1],
                   inning)
        teams[ups].lineup[ondeck[ups]].status_list.append(x)
        if teams[ups].lineup[ondeck[ups]].status_list[-1] == 0:
            print ("Out")
        if teams[ups].lineup[ondeck[ups]].status_list[-1] == 1:
            print ("Single")
        if teams[ups].lineup[ondeck[ups]].status_list[-1] == 2:
            print ("Double")
        if teams[ups].lineup[ondeck[ups]].status_list[-1] == 3:
            print ("Triple")
        if teams[ups].lineup[ondeck[ups]].status_list[-1] == 4:
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
        if ondeck[ups] == len(teams[ups].lineup):
            ondeck[ups] = 0
        if (outs == 3) & (inning >= 10) and (score[0] != score[1]) and (inning % 1 == 0):
            game = False
        if outs == 3:
            outs = 0
    return score


def results(n, score, team1, team2, win_count1, win_count2):
    print("Final Score", score)
    if float(score[0]) > float(score[1]):
        print(team1, "win!")
        win_count1 += 1
    elif float(score[1]) > float(score[0]):
        print(team2, "win!")
        win_count2 += 1
    else:
        breakpoint()
    if n == (win_count1 + win_count2):
        print()
        print(team1, ":", win_count1, sep="")
        print(team2, ":", win_count2, sep="")
        percentage_won1 = (win_count1/(win_count1 + win_count2)) * 100
        percentage_won2 = (win_count2/(win_count1 + win_count2)) * 100
        print(team1, " have a ", percentage_won1, "%", " chance of winning", sep="")
        print(team2, " have a ", percentage_won2, "%", " chance of winning", sep="")
    return win_count1, win_count2


if __name__ == '__main__':
    main()

"""
TODO:
-add ways for players on base to get thrown out
-add graphics
"""
