#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola

print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi e le facce.\nEsempio: \033[47;30m3d6\033[0m tre dadi da sei facce\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire: \033[47;30mexit\033[0m\n\n")

#variabili principali
list_dice_option = ["null","adv","dsv"]
list_roll_option = ["null","ropt1","ropt2"]
mode = ["help","exit","risiko"]
dice_choice = ""
dice_option = ""
roll_option = ""


#definizione della funzione show_help
def show_help ():
  print ("Digita il numero di dadi da lanciare,\n\
seguito da 'd' e poi il numero di facce del dado")


#definizione della funzione di input, user_input. check dell'input, split delle opzioni, e split secondario del numeero di dadi/numero di facce
def user_input ():
#variabili secondarie
  dice_number = 0
  dice_face = 0
#main input
  while True:
    player_choice = input (">>---> ").lower ().split () #main split
#check numero parole e aggiunta se mancano
    if len(player_choice) == 1:
      player_choice.append ("null")
      player_choice.append ("null")
    elif len(player_choice) == 2:
      player_choice.append ("null")
    elif len(player_choice) == 0:
      print ("Digita \033[47;30mhelp\033[0m  per aiuto")
      continue
#check massimo 3 parole e massimo 3 caratteri
#check opzioni
    if len(player_choice) > 3\
or len(player_choice[0]) < 3\
or player_choice[1] not in list_dice_option\
or player_choice[2] not in list_roll_option:
      print ("Hai digitato qualcosa di sbagliato,\nricontrolla le opzioni nella guida digitando \033[47;30mhelp\033[0m.")
      continue
#check caratteri e opzioni, assegnazione varibili opzioni e split secondario di dice_choice
    dice_choice,dice_option,roll_option = player_choice
    if dice_choice in mode and dice_choice != "help":
      break
    elif dice_choice == "help": #digitazione help
      show_help ()
      continue
    if "d" not in dice_choice:
      print (f"\033[47;30m{dice_choice}\033[0m non e' una scelta valida,\nesempio: per lanciare 2 dadi da 6 facce digita \033[47;30m2d6\033[0m.\nPer la guida digita \033[47;30mhelp\033[0m.")
      continue
    dice_choice = dice_choice.split ("d") #split secondario
    if not dice_choice[0].isdigit()\
or not dice_choice[1].isdigit():
      print (f"Hai digitato una scelta non valida,\nesempi validi: 2d6, 3d8, 1d100.\nPer la guida digita \033[47;30mhelp\033[0m ")
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
