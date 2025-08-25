#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola

print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n\n\
Digita il numero di dadi e le facce.\nEsempio: \033[47;30m3d6\033[0m tre dadi da sei facce\n\
Opzioni digita: \033[47;30mhelp\033[0m, \
per uscire: \033[47;30mexit\033[0m\n\n")


player_choice = input (">>---> ") + ("secon")
while len(player_choice) < 3:
  player_choice = input ("scegli ancora >>---> ")

dice_face = int(player_choice [2])
dice_number = int(player_choice [0])
print (player_choice)
print (dice_number)
print (dice_face)
