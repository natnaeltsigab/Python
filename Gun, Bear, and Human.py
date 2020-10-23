import math
import random

def get_user_choice(user_input):
  user_input = user_input.lower()
  if (user_input == 'bear') or (user_input == 'human') or (user_input == 'gun'):
    return user_input
  else:
    return "please choose gun, bear or human"

def get_computer_choice():
 random_number = math.floor(random.uniform(0, 3))
 if random_number == 0:
  return "bear"
 if random_number == 1:
   return 'human'
 if random_number == 2:
   return "gun"

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It is a tie, go again"
 
 
  if user_choice == "bear":
   if computer_choice == "human":
    return "Fatality!! you have devoured up a human"
   else:
      return "Oops!! You just got shot!"

 
  if user_choice == "human":
    if computer_choice == "gun":
      return "Good Job! You have disarmed a Gun!!"
    else:
      return "Oops!! You have been devoured by a Bear"
  
  if user_choice == "gun":
    if computer_choice == "human":
      return "Oops!! Your gun has been disarmed by a human!! "
    else:
      return "'Evil Laugh' you have shot a bear!!"
  
def play_game():
  prompt_user_choice = input("Please choose bear, human or gun")
  user_choice = get_user_choice(prompt_user_choice)
  computer_choice = get_computer_choice()
  print(user_choice)
  print(computer_choice)
  print(determine_winner(user_choice, computer_choice))
  
play_game()
  


  
   
      
      

  