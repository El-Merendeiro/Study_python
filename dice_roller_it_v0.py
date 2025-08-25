#questo sara' un dice roller per qualsiasi gioco da di ruolo o da tavola

print ("\n\nBenvenuto in \033[1;41;37mRolly\033[0m\n")
print ("Scegli il numero di dadi e le facce. Esempio: \033[47;30m3d6\033[0m tre dadi da sei facce")
print ("Per le opzioni digita: \033[47;30mhelp\033[0m")
print ("Per uscire digita: \033[47;30mexit\033[0m\n\n")

player_choice = input ("dado ")
dice_face = int(player_choice [2])
dice_number = int(player_choice [0])
print (dice_number)
print (dice_face)
