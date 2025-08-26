#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola

print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi e le facce.\nEsempio: \033[47;30m3d6\033[0m tre dadi da sei facce\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire: \033[47;30mexit\033[0m\n\n")

#variabili
option = ["adv","dsv"]
#input check e main split
player_choice = input (">>---> ").split ()
while len(player_choice[0]) < 3 or len(player_choice[1]) < 3 or player_choice[1] not in option:
  player_choice = input ("scegli ancora >>---> ").split ()

#dice_choice,dice_option,roll_option = player_choice.split()
#dice_number = int(dice_choice [0])
#dice_face = int(dice_choice [2])

#print (dice_choice)
#print (dice_option)
#print (roll_option)
print (player_choice)
#print (dice_number)
#print (dice_face)
