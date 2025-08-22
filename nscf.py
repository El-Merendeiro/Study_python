import time, random
scelte = ["Sasso","sasso","Carta","carta","Forbice","forbice","Forbici","forbici"]

scelta_player = input ("cosascegli?")

while scelta_player not in scelte:
  print ("la scelta non e valida")
  scelta_player = input ("scegli ancora")
else:
  print (f"hai scelto {scelta_player}")


