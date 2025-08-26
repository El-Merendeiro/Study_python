while True:
  player_choice = input (">>---> ").split () #main split

  if len(player_choice) < 2: #check numero parole
    player_choice.append ("null")
  elif len(player_choice) < 3:
    player_choice.append ("null")
    player_choice.append ("null")


print (player_choice)
