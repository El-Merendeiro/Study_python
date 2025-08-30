#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola
import random


print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi e le facce.\nEsempio: \033[47;30m3d6\033[0m tre dadi da sei facce\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire: \033[47;30mexit\033[0m\n\n")

#variabili principali
list_dice_option = ["null","max","min","add","notver"]
list_roll_option = ["null","notver"]
mode = ["help","exit","risiko"]
dice_choice = ""
dice_option = ""
roll_option = ""
result =[]

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
#gestione comando exit
    if "exit" in player_choice:
      print("Uscita dal programma. Arrivederci!")
      exit()
    if "risiko" in player_choice:
      print ("modalita risiko")
      risiko_roll ()
#check numero parole e aggiunta se mancano
    if len(player_choice) == 1:
      player_choice.append ("null")
      player_choice.append ("null")
    elif len(player_choice) == 2:
      player_choice.append ("null")
    elif len(player_choice) == 0:
      print ("Digita \033[47;30mhelp\033[0m per aiuto")
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
#fine input

#definizione funzione roll
def simple_roll ():
  dice_pos =[]
  for t in range (1,dice_face+1):
    dice_pos += [t]
  result = [random.choice (dice_pos) for _ in range (dice_number)]
#max_roll
  max_roll = result[0]
  for n in result:
    if n > max_roll:
      max_roll = n
#min_roll
  min_roll = result[0]
  for m in result:
    if m < min_roll:
      min_roll = m
#add_roll
  add_roll = 0
  for a in result:
    add_roll += a
  return max_roll,result,dice_pos, min_roll, add_roll
#fine roll

#input eroll per risiko
def risiko_roll ():
  while True:
    player_choice_ris = input ("︻デ┳═ー ").lower ().split ()


 # dice_pos =[]
  #  for t in range (1,dice_face+1):
   # dice_pos += [t]
  #result = [random.choice (dice_pos) for _ in r
#main output
while True:
  dice_choice, dice_option, roll_option, player_choice, dice_number, dice_face = user_input()
  max_roll, result, dice_pos, min_roll,add_roll = simple_roll ()
  if dice_option == "null" and roll_option == "null":
    print (f"il risultato di \033[47;30m{player_choice[0]}\033[0m e' {result}")
  if dice_option == "max" and roll_option == "null":
    print (f"il risultato di \033[47;30m{player_choice[0]} {player_choice[1]}\033[0m e'{result} --> \033[41;30m{max_roll}\033[0m")
  if dice_option == "min" and roll_option == "null":
    print (f"il risultato di \033[47;30m{player_choice[0]} {player_choice[1]}\033[0m e'{result} --> \033[41;30m{min_roll}\033[0m")
  if dice_option == "add" and roll_option == "null":
    print (f"il risultato di \033[47;30m{player_choice[0]} {player_choice[1]}\033[0m e'{result} --> \033[41;30m{add_roll}\033[0m")
  if dice_option == "notver" and roll_option =="null":
    print (result)
  if dice_option == "max" and roll_option =="notver":
    print (max_roll)
  if dice_option == "min" and roll_option =="notver":
    print (min_roll)
  if dice_option == "add" and roll_option =="notver":
    print (add_roll)


##debugging check variabili
#print ("\n\n\n")
#print ("dice_choice",dice_choice)
#print ("dice_option",dice_option)
#print ("roll_option",roll_option)
#print ("player_choice",player_choice)
#if dice_number !=0:
#  print (dice_number)
#  print (dice_face)
#print ("dice_pos",dice_pos)
#print ("max",max_roll)
#print ("result",result)
#print ("min",min_roll)
#print ("ADD",add_roll)
