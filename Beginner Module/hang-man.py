from random import choice


hangman_image = {'0':"""
  _______
 |       |
 |       |
 |       |
 |       
 |      
 |      
 |
_|_
""",

'1':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |      
 |      
 |
_|_
""",

'2':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |       |
 |      
 |
_|_
""",

'3':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |       |
 |        \\
 |
_|_
""",

'4':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |       |
 |      / \\
 |
_|_
""",

'5':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |       |\\
 |      / \\
 |
_|_
""",

'6':"""
  _______
 |       |
 |       |
 |       |
 |       o
 |      /|\\
 |      / \\
 |
_|_
"""}


name_of_fruit = ["mango","apple","orange","banana","kiwi","grape","pineapple","watermelon","cherry"]


def get_player_name():
    """Get the name of the player"""

    result = input('Hello,\nWhat is you name?\n->')
    print(f'-------------------------------\nWelcome to HANG-MAN {result}\n-------------------------------')
    return result


def guess_fruit(name_of_fruit):
    """CPU guess of the fruit name player is to guess"""

    result = choice(name_of_fruit)
    return result


def find_all_indexes(string, letter):
    """To find the location of letter in a string"""

    indexes = []
    for i in range(len(string)):
      if string[i] == letter:
        indexes.append(i)
    return indexes


def wrong_guest_display(fruit, no_of_wrong, hangman_image,name):
    """Output if the guess is wrong"""
    if no_of_wrong >= 6:
      result = f"{hangman_image['6']}\nWrong guest. The hangman word: {fruit.upper()} \n{name},You are hanged !!!"

    else:
       result = f"{hangman_image[str(no_of_wrong)]}\nWrong guest. Try again!!!"

    return result


def correct_guest_display(fruit, no_of_correct, hangman_image,fruit_charaters,no_of_wrong,name):
    """Output if the guess is correct"""

    if no_of_correct >= fruit_charaters:
       result = f"{hangman_image[str(no_of_wrong)]}\nCorret guest. The hangman word: {fruit.upper()} \n{name}, You Won!!!"
    else:
       result = f"{hangman_image[str(no_of_wrong)]}\nCorret guest. Keep the good work!!!"
    return result


def hangman_word(fruit, correct):
    """The current state of the hang-man word"""
    word_len = len(fruit)
    word = ["_" for i in range(word_len)]
    for letter in correct: 
      letter_indexes = find_all_indexes(fruit,letter)
      for index in letter_indexes:
         word[index] = letter
  
    result = ' '.join(word) 
    return result


def player_guess(fruit, correct, wrong):
    """Get the guess from the player"""

    while True:
        word = hangman_word(fruit, correct)
        guess = str(input(f"This is the hangman word:{word} \nEnter a single letter Guess of the fruit: ")).lower()
        if len(guess) == 1 and guess not in correct and guess not in wrong:
            break
        if len(guess) != 1:
          print("Please enter a single character.")
        else:
           print("Please enter a different letter")
    print("Correct value")
    result = guess
    return result


def game_code():
    """ The code to run the game logic """

    correct = []
    wrong = []
    no_of_wrong = len(wrong)
    no_of_correct = len(correct)

    player_name  = get_player_name()

    fruit = guess_fruit(name_of_fruit)
    
    fruit_charaters = len(set(fruit))

    while no_of_wrong < 6 and no_of_correct < fruit_charaters:
        guess = player_guess(fruit,correct,wrong)
        
        if guess in fruit:
            correct.append(guess)
            no_of_correct = len(correct)
            print(correct_guest_display(fruit, no_of_correct, hangman_image, fruit_charaters, no_of_wrong, player_name))
        else:
            wrong.append(guess)
            no_of_wrong = len(wrong)
            print(wrong_guest_display(fruit, no_of_wrong, hangman_image, player_name))


def main():
   """ The main code of the hang-man code"""

   start = True
   while start:
      game_code()
      while True:
        replay = str(input('Want to play again? (yes/no):\n->')).lower()
        if replay in ['yes','no']:
           break
        print('Please reply yes or no')
      if replay == 'yes':
         start= True
      else:
         start= False


if __name__=="__main__":
   main()