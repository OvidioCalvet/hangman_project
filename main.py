import random

# Function that checks players guess
def is_guess_correct(comp_word, status, letter):
   
# Loop iterates through each character in the chose word string and compares it to the players guess
   for l in range(0,len(comp_word)-1):

       if comp_word[l] == letter:

           status = True

   return status

# Function that keeps track of lives
def life_tracker(status, lives):

   if not status:

       lives = lives - 1

   return lives

# Function that builds players word based on guesses
def word_build(status, word_ip, comp_word, letter):
   if status:

       index = []

       for y in range(0, len(chosen_word)-1):

           if comp_word[y] == letter:

               index.append(y)

       for t in range(0, len(index)-1):

           for j in range(0, len(word_ip)-1):

               if word_ip[j] == index[t]:

                   word_ip[j] = letter
   return word_ip

# Function that prints based on all components
def print_guess(status, lives, word_ip):

   if status:
       print("".join(word_ip))
       print(f"Correct! Reminder you still have {lives} lives left.")

   else:
       print("".join(word_ip))
       print(f"Incorrect! You now have {lives} lives left")




# Variable initialization
word_list = ["prada", "europe", "italy", "python", "moncler", "porche", "beach", "perroni"]
temp = word_list[random.randint(0,len(word_list)-1)]
chosen_word = []
for x in range(0, len(temp)-1):
   chosen_word.append(temp[x])

player_word = []
for i in range(0, len(chosen_word)):
   player_word.append("_")

player_lives = 6
game_status = False

# Player interaction code
print("".join(player_word))

while game_status is False:

   guess = input("Guess a letter: ")

   guess_status = False

   guess_status = is_guess_correct(chosen_word, guess_status, guess)
   player_lives = life_tracker(guess_status, player_lives)
   player_word = word_build(guess_status, player_word, chosen_word,guess)

   print_guess(guess_status, player_lives, player_word)

   if player_word == chosen_word or player_lives == 0:

       game_status = True

if player_word == chosen_word and player_lives > 0:

   print("Hooray you win!")

else:

   print("Game Over, you lose!")


