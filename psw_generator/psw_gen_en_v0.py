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
def mode_input ():
  while True:
    mode_select = input ("Choose your password genration mode: Auto/User -> ").lower ()
    if mode_select == "auto" or mode_select == "user":
      return mode_select
    print ("invalid input.")
    continue

def auto_input ():
  level = ["weak","normal","strong","very strong"]
  while True:
    level_select = input ("Chose password's security level:\n"
"weack, normal, strong, very strong -> ").lower ()
    if level_select in level:
      return level_select
    print ("invalid input")
    continue

def user_input ():
  answer = ["y","yes","n","no"]
  while True:
    lenght_select = input ("How many carachters your password should be? type a number -> ")
    if not lenght_select.isdigit() and lenght_select < 50:
      print ("type a number smaller than 50")
      continue
    carachter_type = input ("Do you want include letter in your password? y/n -> ").lower()
    if not carather_type in answer:
      print ("invalid input")
      continue
    if carachter_type == "yes" or carachter_type == "y":
      carachter_type = True
    elif carachter_type == "no" or carachter_type == "n":
      carachter_type = False


mode_select = mode_input ()
level_select = auto_input ()
print (mode_select)
print (level_select)
