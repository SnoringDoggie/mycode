#!/usr/bin/env python3

round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Guess The Age of the Lush, "AMF 12-23 ______"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == '19': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was 19.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Guess The Age of the Lush, "IPA 21-30 ______"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == '26': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was 26.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Guess The Age of the Lush, "Water 1-100_____"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == 'who drinks water as a lush': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif round == 2:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was who drinks water as a lush.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 2
        print('Sorry. Try again!')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
