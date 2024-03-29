#The game HORSE is a popular basketball shooting game.
#It can be played with any number of players. One-by-one,
#each player takes a shot from anywhere they want. If they
#make the shot, the next person must make the same shot.
#If they do not, they receive a letter: H, then O, then R,
#then S, then E. Once a player receives all 5 letters, they
#are out of the game.
#
#The game continues until all but one player has all five
#letters.
#
#Write a function called check_horse_winner. This function
#will take as input a tuple of at least two, but potentially
#more, strings. 
#
#check_horse_winner should return the following:
#
# - If only one player is left with fewer than 5 letters,
#   return "Player X wins!", where X is the index of the
#   player in the list (which could be 0).
# - If more than one player has fewer than 5 letters,
#   return "Players X, Y: keep playing!", where X, Y, and
#   potentially more numbers are the indices of all players
#   who have not yet been eliminated.
# - If no player has 5 letters, return "Everyone: keep
#   playing!"


#Write your function here!
def check_horse_winner(players):
    playing = []
    i = 0
    for player in players:
        if len(player) < 5:
            playing.append(str(i))
        i += 1
    if len(playing) == len(players):
        return "Everyone: keep playing!"
    elif 1 < len(playing) < len(players):
        return 'Players ' + (", ").join(playing) + ": keep playing!"
    elif len(playing) == 1:
        return "Player " + str(playing[0]) + ' wins!'


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Everyone: keep playing!
#Players 1, 2: keep playing!
#Player 2 wins!
#Players 2, 3, 5, 6: keep playing!
#Players 0, 1, 3, 4: keep playing!
print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "", "HO", "HORSE", "", "HOR")))
print(check_horse_winner(("", "H", "HORSE", "", "HO")))

