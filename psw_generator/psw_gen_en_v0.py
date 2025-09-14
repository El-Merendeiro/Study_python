#password generator 2025.9.11
print("""
\033[1;36mThis is a Password Generator\033[0m\n
There are two modes to create your password:\n
\033[1;33mAuto Mode:\033[0m
  Your password will be generated automatically.
  You only need to choose the security level:
  \033[32mweak, medium, strong, very strong\033[0m\n
\033[1;33mUser Mode:\033[0m
  You will decide all the options for your password:
  - Length
  - Alphabet
  - Alphanumeric
  - Special characters
  - Capital letters or not\n
Type \033[35m'help'\033[0m for more information.
Type \033[35m'exit'\033[0m to quit.
""")

import string
import random

#help
def show_help ():
  print ("this is help")

#mode input select
def mode_input ():
  while True:
    mode_select = input ("Choose your password genration mode: Auto/User -> ").lower ()
    if mode_select == "help":
      show_help ()
      continue
    elif mode_select == "exit":
      print ("good bye")
      exit ()
    if mode_select == "auto" or mode_select == "user":
      return mode_select
    print ("invalid input.")
    continue

#auto mode, input security level select
def auto_input ():
  level = ["weak","medium","strong","very strong"]
  while True:
    level_select = input ("Chose password's security level:\n"
"weak, medium, strong, very strong -> ").lower ()
    if level_select == "help":
      show_help ()
      continue
    elif level_select == "exit":
      print ("good bye")
      exit ()
    if level_select in level:
      return level_select
    print ("invalid input")
    continue

#user mode, input ask yes or no
def ask_y_n (question):
  while True:
    user_select = input (question).lower ()
    if user_select == "help":
      show_help ()
      continue
    elif user_select == "exit":
      print ("good bye")
      exit ()
    if user_select == "yes" or user_select == "y":
      return True
    elif user_select =="no" or user_select == "n":
      return False
    else:
      print ("invalid input")
      continue

#user mode, input password lenght
def user_input ():
  while True:
    lenght_select = input ("How many characters your password should be? type a number -> ")
    if lenght_select == "help":
      show_help ()
      continue
    elif lenght_select == "exit":
      print ("good bye")
      exit ()
    if not lenght_select.isdigit():
      print ("type a valid nunmber")
      continue
    lenght_select = int(lenght_select)
    if lenght_select > 50:
      print ("type a number smaller than 50")
      continue
    return lenght_select

#auto mode, password generator
def auto_generator ():
  weak_list = list(string.digits)
  medium_list = list(string.ascii_lowercase)+weak_list
  strong_list = list(string.ascii_uppercase)+medium_list+weak_list
  very_strong_list = list(string.punctuation)+strong_list+medium_list+weak_list
  choose_list = level_select
  if choose_list == "weak":
    auto_list = weak_list
    auto_lenght = 8
  elif choose_list == "medium":
    auto_list = medium_list
    auto_lenght = 12
  elif choose_list == "strong":
    auto_list = strong_list
    auto_lenght = 16
  elif choose_list == "very strong":
    auto_list = very_strong_list
    auto_lenght = 20
  password = [random.choice (auto_list) for _ in range(auto_lenght+1)]
  password = "".join (password)
  return password





#main
mode_select = mode_input()
if mode_select == "auto":
  level_select = auto_input ()
  password = auto_generator ()
elif mode_select == "user":
  lenght_select = user_input ()
  characters_select = ask_y_n ("Include letters in your password? y/n ")
  capital_select = ask_y_n ("Include uppercase characters in your password? y/n ")
  special_select = ask_y_n ("Include special characters in your password? y/n ")


print (password)
print (mode_select)
