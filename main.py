import random

# Function that checks players guess
def is_guess_correct(status):
   
# Loop iterates through each character in the chose word string and compares it to the players guess
   for l in range(0,len(chosen_word)):

       if chosen_word[l] == guess:

           status = True

   return status

# Function that keeps track of lives
def life_tracker(lives):

   if not guess_status:

       lives = lives - 1

   return lives

# Function that builds players word based on guesses
def word_build(word_ip):
   if guess_status:

       for y in range(0, len(chosen_word)):

           if chosen_word[y] == guess:

               word_ip[y] = guess
   
   return word_ip

# Function that prints based on all components
def print_guess():

   if guess_status:
       print("".join(player_word))
       print(f"Correct! Reminder you still have {player_lives} lives left.")

   else:
       print("".join(player_word))
       print(f"Incorrect! You now have {player_lives} lives left")




# Variable initialization
word_list = ["prada", "europe", "italy", "python", "moncler", "porche", "beach", "perroni"]
temp = word_list[random.randint(0,len(word_list)-1)]
chosen_word = []
for x in range(0, len(temp)):
   chosen_word.append(temp[x])

player_word = []
for i in range(0, len(chosen_word)):
   player_word.append("_")


player_lives = 6
game_status = False

print("".join(player_word))


# Player interaction code
while game_status is False:

   guess = input("Guess a letter: ")

   guess_status = False

   guess_status = is_guess_correct(guess_status)
   player_lives = life_tracker(player_lives)
   player_word = word_build(player_word)

   print_guess()

   if player_word == chosen_word or player_lives == 0:

       game_status = True

if player_word == chosen_word and player_lives > 0:

   print("Hooray you win!")

else:

   print("Game Over, you lose!")