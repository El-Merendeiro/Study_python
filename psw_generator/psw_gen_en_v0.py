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
  mode_select = input ("Choose your password genration mode: Auto/User -> ").lower ()
  return mode_select

mode_select = mode_input ()
print (mode_select)
