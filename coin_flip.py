#Basic Requirements
#User Story: As a user I want to be able to guess the outcome
#of a random coin flip(heads/tails).
#User Story: As a user I want to clearly see
#the result of the coin flip. User Story: As a user I want to
#clearly see whether or not I guessed correctly.
import random
def coin_flip():
    print("Guess the outcome of a random coin flip (heads/tails)")
    guess = input()
    possible_choices = ["heads", "tails"]
    flip = random.choice(possible_choices)
    print("The result of a coin flip is " + flip)
    if guess == flip:
        print("You guessed correctly!")
    else:
        print("You didn't guessed correctly!")

#coin_flip()
#intermediate Challenge
#User Story: As a user I want to clearly see the updated guess
# history (correct count/total count).
#User Story: As a user I want to be able to quit the game or go
#again after each cycle.

def coin_flip2():
    correct_count1 = 0
    total_count1 = 0
    while True:
        print("Guess the outcome of a random coin flip (heads/tails)")
        guess1 = input()
        possible_choices = ["heads", "tails"]
        flip = random.choice(possible_choices)
        print("The result of a coin flip is " + flip)
        if guess1 == flip:
            print("You guessed correctly!")
            correct_count1 += 1
            total_count1 += 1
        else:
            print("You didn't guessed correctly!")
            total_count1 += 1
        print("Total count of your guesses is " + str(total_count1))
        print("The number of correct guesses is " + str(correct_count1))
        print("Do you want to play again? Type y for yes and n for no")
        again = input()
        if again == "n":
            break
    return correct_count1, total_count1


#Let’s see if we can expand upon this challenge - what if
#instead of 2 options, there were 6?
#User Story: As a user I want to be able to guess the outcome of a
#6-sided dice roll (1-6), with the same feature set as the coin flip
#(see above).
#s
#You can add this directly to the existing program you’ve already written!
#As an additional challenge see if you can build the program such that the
#the user can choose between the two
#guessing games at startup, and possibly even switch after each cycle.
def dice_roll():
    correct_count = 0
    total_count = 0
    while True:
        print("Guess the outcome of a 6 - sided dice roll (enter a number from 1 to 6)")
        guess = int(input())
        roll = random.randint(1,6)
        print("The result of a dice roll is " + str(roll))
        if guess == roll:
            print("You guessed correctly!")
            correct_count += 1
            total_count += 1
        else:
            print("You didn't guessed correctly!")
            total_count += 1
        print("Total count of your guesses is " + str(total_count))
        print("The number of correct guesses is " + str(correct_count))
        print("Do you want to play again? Type y for yes and n for no")
        again = input()
        if again == "n":
            break
    return correct_count, total_count




def playing_game():
    coin_flip_correct = 0
    coin_flip_total = 0
    dice_roll_correct = 0
    dice_roll_total = 0
    while True:
        print("Which game do you want to play?")
        print("Press 1 for coin flip, 2 for 6 - sided dice roll and 3 to quit")
        game = int(input())
        if game == 1:
            a, b = coin_flip2()
            coin_flip_correct += a
            coin_flip_total += b
            print("You scored " + str(coin_flip_correct) + " correct guesses in the coin flip game overall.")
            print("You had " + str(coin_flip_total) + " total number of guesses in the coin flip game.")
        elif game == 2:
            e, f = dice_roll()
            dice_roll_correct += e
            dice_roll_total += f
            print("You scored " + str(dice_roll_correct) + " corrects guesses in the dice roll game.")
            print("You had " + str(dice_roll_total) + " total number of guesses in the dice roll game")
        else:
            break
    print("Thank you for your game.")
    print("You scored " + str(coin_flip_correct + dice_roll_correct) + " corrects guesses in both games.")
    print("You tried " + str(coin_flip_total + dice_roll_total) + " times.")

playing_game()
