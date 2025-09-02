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

#definizione della funzione show_help e show_help_ris
def show_help ():
  print ("Digita il numero di dadi da lanciare,\n\
seguito da 'd' e poi il numero di facce del dado")

def show_help_ris ():
  print ("help di risiko")

#definizione della funzione di input, user_input. check dell'input, split delle opzioni, e split secondario del numeero di dadi/numero di facce
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
      print ("Digita \033[47;30mhelp\033[0m per aiuto")
      continue
#check massimo 3 parole e massimo 3 caratteri
#check opzioni
    dice_choice,dice_option,roll_option = player_choice
    if dice_choice in mode:
      return dice_choice,dice_option,roll_option,player_choice
    if len(dice_choice) < 3\
or dice_option not in list_dice_option\
or roll_option not in list_roll_option:
      print ("Hai digitato qualcosa di sbagliato,\nricontrolla le opzioni nella guida digitando \033[47;30mhelp\033[0m.")
      continue
#check caratteri e opzioni, assegnazione varibili opzioni e split secondario di dice_choice
    if "d" not in dice_choice:
      print (f"\033[47;30m{dice_choice}\033[0m non e' una scelta valida,\nesempio: per lanciare 2 dadi da 6 facce digita \033[47;30m2d6\033[0m.\nPer la guida digita \033[47;30mhelp\033[0m.")
      continue
    dice_choice = dice_choice.split ("d") #split secondario
    if not dice_choice[0].isdigit()\
or not dice_choice[1].isdigit():
      print (f"Hai digitato una scelta non valida,\nesempi validi: 2d6, 3d8, 1d100.\nPer la guida digita \033[47;30mhelp\033[0m ")
      continue
    return dice_choice,dice_option,roll_option,player_choice
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

#input per risiko
def risiko_input ():
  while True:
    player_choice_ris = input ("︻デ┳═ー ").lower ().split ()
    if "exit" in player_choice_ris:
      print ("uscita risiko")
      print ("sei tornato nella modalita mista")
      red_dice = 0
      blue_dice = 0
      return red_dice,blue_dice
    if "help" in player_choice_ris:
      show_help_ris ()
      continue
    if len(player_choice_ris) < 2 or len(player_choice_ris) >2:
      print ("riprova")
      continue
    red_dice , blue_dice = player_choice_ris
    if "red" not in red_dice or "blue" not in blue_dice:
      print ("Hai sbagliato qualcosa, digita red3 blue3")
      continue
    if len(red_dice) > 4 or len(blue_dice) > 5:
      print ("sbagliato riprova")
      continue
    red_dice = red_dice.split("red")
    red_dice = int(red_dice[1])
    blue_dice = blue_dice.split("blue")
    blue_dice = int(blue_dice[1])
    if red_dice > 3 or blue_dice > 3 or red_dice < 1 or blue_dice < 1:
      print ("puoi lanciare massimo 3 e minimo 1 dado a player")
      continue
    return red_dice, blue_dice

def risiko_roll ():
  dice_pos_ris = [1,2,3,4,5,6]
  result_red = [random.choice (dice_pos_ris) for _ in range (red_dice)]
  result_blue = [random.choice (dice_pos_ris) for _ in range (blue_dice)]
  result_red.sort ()
  result_blue.sort ()
  lost_red = 0
  lost_blue = 0
  max_compare = min(red_dice,blue_dice)

  for g in range(1,max_compare+1):
    if result_blue[-g] >= result_red[-g]:
      lost_red+=1
    else:
      lost_blue+=1
  return lost_red, lost_blue, result_red, result_blue, max_compare

while True:
  dice_choice, dice_option, roll_option, player_choice = user_input()
  if "exit" in player_choice:
      print("Uscita dal programma. Arrivederci!")
      exit()
  if "help" in player_choice:
      show_help ()
      continue
  if "risiko" in player_choice:
    print ("\n\nBenvenuto nella modalita Risiko di \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi dell'attaccante (red),\n\
seguito dal numero di dadi del difensore (blue).\
Esempio: \033[47;30mred3 blue2\033[0m 3 dadi per l'attaccante e 2 per il difensore\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire dalla modalita' risiko: \033[47;30mexit\033[0m\n\n")

  while dice_choice == "risiko":
    red_dice, blue_dice = risiko_input ()
    lost_red, lost_blue, result_red, result_blue, max_compare = risiko_roll ()
    if red_dice == 0 and blue_dice==0:
      dice_choice = "Null"
    else:
      print (f"\nnumero dadi attaccante: {red_dice}. Risultato: {result_red}\n\
numero dadi difensore: {blue_dice}. Risultato: {result_blue}\n\
numero scontri: {max_compare}.\n\
cararmati persi dall'attaccante: {lost_red}.\n\
cararmati persi dal difensore: {lost_blue}.\n\n")
  if dice_choice == "Null":
    continue
  
  dice_number = int(dice_choice[0])
  dice_face = int(dice_choice[1])
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
#print ("player_choice_ris",player_choice_ris)
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
