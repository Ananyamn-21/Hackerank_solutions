# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

def minion_game(string):
    n = len(string)
    vowels = 0
    cons = 0
    for idx, c in enumerate(string):
        num_substr = n - idx
        if c in 'AEIOU':
            vowels += num_substr
        else:
            cons += num_substr
    if vowels > cons:
        print(f'Kevin {vowels}')
    elif cons > vowels:
        print(f'Stuart {cons}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)