#password generator 2025.9.11
print ("\n\nThis is a password generator, \n"
"there are 2 mode to create your password,\n\n"
 "Auto mode:\n"
  "Your password will be genereted automaticaly,\n"
  "you need choose only the level of security\n"
  "(weak, medium, strong, very strong)\n\n"
 "User mode:\n"
  "You will choose all option for your password\n"
  "(lenght, alphabet, alphanumeric, special caracter, capital or not)\n\n"
"Type: 'help' for more info\n\n")

#help
def show_help ():
  print ("this is help")

#input
#mode input
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

#auto input option
def auto_input ():
  level = ["weak","normal","strong","very strong"]
  while True:
    level_select = input ("Chose password's security level:\n"
"weak, normal, strong, very strong -> ").lower ()
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



#user input option


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


def user_input ():
  while True:
    lenght_select = input ("How many carachters your password should be? type a number -> ")
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






mode_select = mode_input()
if mode_select == "auto":
  level_select = auto_input ()
elif mode_select == "user":
  lenght_select = user_input ()

  characters_select = ask_y_n ("Do you want include letters in your password? y/n ")
  capital_select = ask_y_n ("Do you want include CAPITAL characters in your password?")
  special_select = ask_y_n ("Do you want include special characters inyour password? y/n")


print (mode_select)
