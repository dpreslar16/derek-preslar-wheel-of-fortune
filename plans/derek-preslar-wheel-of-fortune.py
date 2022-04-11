#Wheel of Fortune program!

#Imports:
import random
import time

#Welcome
print("Wheel of Fortune!")

#Contestant Names
contestants_names = ['a', 'b', 'c']
contestants_names[0] = input("Who is the first contestant? ")
contestants_names[1] = input("Who is the second contestant? ")
contestants_names[2] = input("Who is our third contestant? ")
current_player_num = 0

f = open('english-words-unabridged.txt')
word_bank = f.readlines()
f.close()

for i in range(0, len(word_bank)):
    word_bank[i] = word_bank[i][0:len(word_bank[i])-1].lower()

#Create Wheel
g = open('wheel-values.txt')
wheel_values = g.readlines()
g.close()

for i in range(0, len(wheel_values)):
    wheel_values[i] = wheel_values[i][0:len(wheel_values[i])-1].lower()

#Functions
def spin_wheel():
    return random.choice(wheel_values)

def next_player(x):
    if x == 0:
        return x + 1
    elif x == 1:
        return x + 1
    elif x == 2:
        return x - 2

#Initialize contestant totals
round_total = [0,0,0]
current_player_round_total = 0
totals = [0,0,0]

#Round 1
#Initialize the word and guess list for user
target_word = random.choice(word_bank).lower()
temp_list = list(target_word)
target_word_letters = tuple(temp_list)
guess_list = []

for i in target_word_letters:
    guess_list.append("_")
correct_letters_guessed = []
puzzle_solved = False

#Loop to solve first puzzle- cover different input scenarios
while puzzle_solved == False:
    print("The word to solve is: \n")
    print(guess_list)
    player_choice = str(input(contestants_names[current_player_num] + " it is your turn: would you like to spin, buy a vowel, or solve? (You have $" + str(round_total[current_player_num]) + " this round.) ")).lower()
    if player_choice == 'spin':
        current_spin = spin_wheel()
        print("You spun " + current_spin)
        if current_spin == 'lose a turn':
            current_player_num = next_player(current_player_num)
        elif current_spin == 'bankrupt':
            round_total[current_player_num] = 0
            current_player_num = next_player(current_player_num)
        else:
            player_guess = input("Please list a consonant ")
            if player_guess in target_word_letters and player_guess not in ['a', 'e', 'i', 'o', 'u'] and player_guess not in correct_letters_guessed:
                k = 0
                correct_letters_guessed.append(player_guess)
                consonant_count = 0
                for i in target_word_letters:
                    if player_guess == i:
                        j = target_word_letters.index(i,k)
                        guess_list[j] = player_guess
                        consonant_count += 1
                    k += 1      
                round_total[current_player_num] = round_total[current_player_num] + (int(current_spin) * consonant_count)
            else:
                print("That was not a consonant, it was already guessed before, or the letter was not in the word!")
                current_player_num = next_player(current_player_num)
    elif player_choice == 'buy a vowel' and round_total[current_player_num] >= 250:
        player_guess = input("Which vowel would you like to buy? ")
        if player_guess in target_word_letters and player_guess in ['a', 'e', 'i', 'o', 'u']:
            k = 0
            for i in target_word_letters:
                if player_guess == i:
                    j = target_word_letters.index(i,k)
                    guess_list[j] = player_guess
                k += 1     
            round_total[current_player_num] = round_total[current_player_num] - 250
        else:
            print("You either don't have at least $250, that was not a vowel, or the letter was not in the word!")
            current_player_num = next_player(current_player_num)
    elif player_choice == 'solve':
        player_guess = input("What is it? ")
        if player_guess == target_word:
            print("Congratulations, you win this round! You won $" + str(round_total[current_player_num] + 1000))
            totals[current_player_num] += round_total[current_player_num] + 1000    # I added a $1000 dollar bonus for solving the puzzle
            puzzle_solved = True
        else:
            print("That was not correct!")
            current_player_num = next_player(current_player_num)
    else:
        print("You must have misinput your choice! Please enter \"spin\", \"buy a vowel\", or \"solve\". ")

#Round 2
print("Let's begin round 2!")
round_total = [0, 0, 0]
target_word = random.choice(word_bank).lower()
temp_list = list(target_word)
target_word_letters = tuple(temp_list)
guess_list = []

for i in target_word_letters:
    guess_list.append("_")
correct_letters_guessed = []
puzzle_solved = False
while puzzle_solved == False:
    print("The word to solve is: \n")
    print(guess_list)
    player_choice = str(input(contestants_names[current_player_num] + " it is your turn: would you like to spin, buy a vowel, or solve? (You have $" + str(round_total[current_player_num]) + " this round.) ")).lower()
    if player_choice == 'spin':
        current_spin = spin_wheel()
        print("You spun " + current_spin)
        if current_spin == 'lose a turn':
            current_player_num = next_player(current_player_num)
        elif current_spin == 'bankrupt':
            round_total[current_player_num] = 0
            current_player_num = next_player(current_player_num)
        else:
            player_guess = input("Please list a consonant ")
            if player_guess in target_word_letters and player_guess not in ['a', 'e', 'i', 'o', 'u'] and player_guess not in correct_letters_guessed:
                k = 0
                correct_letters_guessed.append(player_guess)
                consonant_count = 0
                for i in target_word_letters:
                    if player_guess == i:
                        j = target_word_letters.index(i,k)
                        guess_list[j] = player_guess
                        consonant_count += 1
                    k += 1      
                round_total[current_player_num] = round_total[current_player_num] + (int(current_spin) * consonant_count)
            else:
                print("That was not a consonant, it was already guessed before, or the letter was not in the word!")
                current_player_num = next_player(current_player_num)
    elif player_choice == 'buy a vowel' and round_total[current_player_num] >= 250:
        player_guess = input("Which vowel would you like to buy? ")
        if player_guess in target_word_letters and player_guess in ['a', 'e', 'i', 'o', 'u']:
            k = 0
            for i in target_word_letters:
                if player_guess == i:
                    j = target_word_letters.index(i,k)
                    guess_list[j] = player_guess
                k += 1     
            round_total[current_player_num] = round_total[current_player_num] - 250
        else:
            print("You either don't have at least $250, that was not a vowel, or the letter was not in the word!")
            current_player_num = next_player(current_player_num)
    elif player_choice == 'solve':
        player_guess = input("What is it? ")
        if player_guess == target_word:
            print("Congratulations, you win this round! You won $" + str(round_total[current_player_num] + 1000))
            totals[current_player_num] += round_total[current_player_num] + 1000    # I added a $1000 dollar bonus for solving the puzzle
            puzzle_solved = True
        else:
            print("That was not correct!")
            current_player_num = next_player(current_player_num)
    else:
        print("You must have misinput your choice! Please enter \"spin\", \"buy a vowel\", or \"solve\". ")
        
# Bonus Round
if totals[0] > totals[1] and totals[0] > totals[2]:
    current_player_num = 0
elif totals[1] > totals[0] and totals[1] > totals[2]:
    current_player_num = 1
elif totals[2] > totals[0] and totals[2] > totals[1]:
    current_player_num = 2
elif totals[0] == totals[1] and totals[0] > totals[2]:
    pick_winner = [0, 1]
    current_player_num = random.choice(pick_winner)
    print("Looks like we have a tie! We will randomly choose who goes on to the final round. The winner who will be advancing is: " + contestants_names[current_player_num])
elif totals[0] == totals[2] and totals[0] > totals[1]:
    pick_winner = [0, 2]
    current_player_num = random.choice(pick_winner)
    print("Looks like we have a tie! We will randomly choose who goes on to the final round. The winner who will be advancing is: " + contestants_names[current_player_num])
elif totals[1] == totals[2] and totals[1] > totals[0]:
    pick_winner = [1, 2]
    current_player_num = random.choice(pick_winner)
    print("Looks like we have a tie! We will randomly choose who goes on to the final round. The winner who will be advancing is: " + contestants_names[current_player_num])
elif totals[0] == totals[1] and totals[1] == totals[2]:
    pick_winner = [0, 1, 2]
    current_player_num = random.choice(pick_winner)
    print("Looks like we have a tie! We will randomly choose who goes on to the final round. \nThe winner who will be advancing is: " + contestants_names[current_player_num])

print(contestants_names[current_player_num] + ", welcome to the bonus round! We have already added the letters R, S, T, L, N, and E \nand you get to pick three more consonants and a vowel! Once you've entered, you will have 5 seconds to enter the correct answer. Good luck!")
target_word = random.choice(word_bank).lower()
temp_list = list(target_word)
target_word_letters = tuple(temp_list)
guess_list = []
letters_guessed = ['r', 's', 't', 'l', 'n', 'e']
for i in target_word_letters:
    if i not in letters_guessed:
        guess_list.append("_")
    elif i in letters_guessed:
        guess_list.append(i)


print("The word to solve is: \n")
print(guess_list)
vowel_count = 1
bonus_consonant_count = 2
bonus_round_validate = False
while bonus_round_validate== False:
    player_choice = str(input("Please enter one at a time! ")).lower()
    if player_choice in ['a', 'i', 'o', 'u'] and vowel_count == 1:
        k = 0
        vowel_count = 0
        letters_guessed.append(player_guess)
        for i in target_word_letters:
            if player_guess == i:
                j = target_word_letters.index(i,k)
                guess_list[j] = player_guess
                consonant_count += 1
            k += 1
    elif player_choice in ['a', 'i', 'o', 'u'] and vowel_count == 0:
        print("That vowel has already been guessed or you have already guessed a vowel!")
        continue
    elif player_choice in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'p', 'q', 'v', 'w', 'x', 'y', 'z'] and bonus_consonant_count >= 1 and player_choice not in letters_guessed:
        k = 0
        bonus_consonant_count = bonus_consonant_count - 1
        letters_guessed.append(player_guess)
        for i in target_word_letters:
            if player_guess == i:
                j = target_word_letters.index(i,k)
                guess_list[j] = player_guess
            k += 1
    elif player_choice in letters_guessed and player_choice in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'p', 'q', 'v', 'w', 'x', 'y', 'z']:
        print("That consonant has already been guessed!")
        continue
    elif vowel_count == 0 and bonus_consonant_count == 0:
        bonus_round_validate = True
    else:
        print("Please reenter: remember you have to have three consonants and a vowel total, entered one at a time, not including r, s, t, l, n, or e! ")


input("Press enter when you are ready. When you hit enter, you will have 5 seconds to solve the puzzle enter your answer.")
start = time.time()
print(guess_list)
player_guess= input("Enter the solution here: ")
end = time.time()
time_to_solve = end - start

if player_guess == target_word and time_to_solve < 5:
    print("Congratulations, you won another 5000 dollars for a total of " + str(totals[current_player_num] +5000) + "! \nThanks for playing!")
else:
    print("That's incorrect or out of time, how unfortunate! But at least you won " + str(totals[current_player_num]) + "! \nThanks for playing!")