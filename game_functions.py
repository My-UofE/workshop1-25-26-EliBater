import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    min_x = 0
    max_x = len(poss_values)-1
    mid_x = (max_x+min_x)//2

    return poss_values[mid_x]

    #x = random.choice(poss_values)   
    #return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    temp = next_val - current_val
    if temp > 0 and user_input == 'h':
        return True
    elif temp < 0 and user_input == 'l':
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    in_word = False
    for i in range(len(word)):
        if letter == word[i]:
            board[i] = letter
            in_word = True
    if in_word == True:
        print(f"Well done! \'{letter}\' is in the word")
        return in_word
    
    print(f"Sorry, \'{letter}\' is not in the word")
    return in_word
