#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola

print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi e le facce.\nEsempio: \033[47;30m3d6\033[0m tre dadi da sei facce\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire: \033[47;30mexit\033[0m\n\n")

#variabili
list_dice_option = ["null","adv","dsv"]
list_roll_option = ["null","ropt1","ropt2"]
mode = ["help","exit","risiko"]
dice_choice = ""
dice_option = ""
roll_option = ""
dice_number = 0
dice_face = 0

#help
def show_help ():
  print ("Digita il numero di dadi da lanciare,\
seguito da 'd' e poi il numero di facce del dado")

#input check e main split
def user_input ():
  while True:
    player_choice = input (">>---> ").lower ().split () #main split
#check numero parole e aggiunta se mancano
    if len(player_choice) == 1:
      player_choice.append ("null")
      player_choice.append ("null")
    elif len(player_choice) == 2:
      player_choice.append ("null")
    elif len(player_choice) == 0:
      print ("scrivi quslcosa")
      continue
#check massimo 3 parole e massimo 3 caratteri
#check opzioni
    if len(player_choice) > 3\
or len(player_choice[0]) < 3\
or player_choice[1] not in list_dice_option\
or player_choice[2] not in list_roll_option:
      print ("non valido ricontrolla le opzioni")
      continue

#split player_choice check caratteri
    dice_choice,dice_option,roll_option = player_choice
    if dice_choice in mode and dice_choice != "help":
      break
    elif dice_choice == "help":
      show_help ()
      continue
    if "d" not in dice_choice:
      print ("riprova con ex: 3d6")
      continue
    dice_choice = dice_choice.split ("d")
    if not dice_choice[0].isdigit()\
or not dice_choice[1].isdigit():
      print ("non hai scirtto bene i dadi e le loro faccie ex: 2d6")
      continue
    else:
      dice_number = int(dice_choice [0])
      dice_face = int(dice_choice [1])
      break
      return dice_choice, dice_option, roll_option, player_choice, dice_number, dice_face
dice_choice, dice_option, roll_option, player_choice, dice_number, dice_face = user_input()
#fine input

print (dice_choice)
print (dice_option)
print (roll_option)
print (player_choice)
if dice_number !=0:
  print (dice_number)
  print (dice_face)
show_help ()
