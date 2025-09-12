def ask_y_n (user_input):
  while True:
    user_select = input(user_input).lower ()
    if user_select == "yes" or user_select == "y":
      return True
    elif user_select == "no" or user_select == "n":
      return False
    else:
      print("invalid input")
      continue


letter = ask_y_n ("vuoi le lettere??")
print (letter)
