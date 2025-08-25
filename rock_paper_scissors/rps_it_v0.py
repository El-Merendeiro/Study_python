import time, random
print ("Benvenuto al classicco gioco, ")
print ("SASSO, CARTA, FORBICI")
time.sleep(2)

knowledge = input ("Conosci gia le le regole?[Si/No]▷▶ ")

if knowledge == "Si" or knowledge == "si":
  print ("ok allora iniziamo subito")
  time.sleep(1)
elif knowledge == "No" or knowledge == "no":
  print ("ok nessun problema le regole sono semplicissime")
  print ("entrambi scegliamo una delle 3 opzioni: Sasso, Carta o Forbici")
  print ("La Carta batte il Sasso")
  print ("Il Sasso batte le Forbici")
  print ("Le Forbici battono la Carta")
  time.sleep(1)
print ("scegli al mio tre")
import time
for t in range (3,0,-1):
        print (t,end='\r', flush=True)
        time.sleep(1.5)
scelta = input ("cosa scegli?▷▶ ")

if scelta == "sasso" or scelta == "Sasso" or scelta == "SASSO":
  valore_player = 1
elif scelta == "Carta" or scelta == "carta" or scelta == "CARTA":
  valore_player = 2
elif scelta == "Forbice" or scelta == "forbice" or scelta == "Forbici" or scelta == "forbici":
  valore_player = 3
else:
  print ("la tua scelta non era valida il gioco finisce qui")

import random
opzioni = [1,2,3]
valore_bot = random.choice(opzioni)

#pareggio sasso
if valore_bot == 1 and valore_player ==1:
  print ("anch'io ho scelto sasso")
  print ("facciamo un ultimo tentativo")
  print ("scegli al mio tre")
  import time
  for t in range (3,0,-1):
          print (t,end='\r', flush=True)
          time.sleep(1.5)

  scelta = input ("cosa scegli?▷▶ ")

  if scelta == "sasso" or scelta == "Sasso" or scelta == "SASSO":
    valore_player = 1 
  elif scelta == "Carta" or scelta == "carta" or scelta == "CARTA":
    valore_player = 2
  elif scelta == "Forbice" or scelta == "forbice" or scelta == "Forbici" or scelta == "forbici":
    valore_player = 3
  else:
    print ("la tua scelta non era valida il gioco finisce qui")
  valore_bot = random.choice(opzioni)
  if valore_bot == player:
    print ("abbiamo scelto di nuovo la stessa opzione il gioco finisce qui")

#pareggio carta
if valore_bot == 2 and valore_player == 2:
  print ("anch'io ho scelto carta")
  print ("facciamo un ultimo tentativo")
  print ("scegli al mio tre")
  import time
  for t in range (3,0,-1):
          print (t,end='\r', flush=True)
          time.sleep(1.5)

  scelta = input ("cosa scegli?▷▶ ")

  if scelta == "sasso" or scelta == "Sasso" or scelta == "SASSO":
    valore_player = 1
  elif scelta == "Carta" or scelta == "carta" or scelta == "CARTA":
    valore_player = 2
  elif scelta == "Forbice" or scelta == "forbice" or scelta == "Forbici" or scelta == "forbici":
    valore_player = 3
  else:
    print ("la tua scelta non era valida il gioco finisce qui")
  valore_bot = random.choice(opzioni)
  if valore_bot == valore_player:
    print ("abbiamo scelto di nuovo la stessa opzione il gioco finisce qui")

#pareggio forbice
if valore_bot == 3 and valore_player == 3:
  print ("anch'io ho scelto forbice")
  print ("facciamo un ultimo tentativo")
  print ("scegli al mio tre")
  import time
  for t in range (3,0,-1):
          print (t,end='\r', flush=True)
          time.sleep(1.5)

  scelta = input ("cosa scegli?▷▶ ")

  if scelta == "sasso" or scelta == "Sasso" or scelta == "SASSO":
    valore_player = 1
  elif scelta == "Carta" or scelta == "carta" or scelta == "CARTA":
    valore_player = 2
  elif scelta == "Forbice" or scelta == "forbice" or scelta == "Forbici" or scelta == "forbici":
    valore_player = 3
  else:
    print ("la tua scelta non era valida il gioco finisce qui")
  valore_bot = random.choice(opzioni)
  if valore_bot == valore_player:
    print ("abbiamo scelto di nuovo la stessa opzione il gioco finisce qui")

#bot=sasso/player=forbici
if valore_bot != valore_player and valore_bot == 1 and valore_player == 3:
  print ("che sfortuna hai perso, io ho scelto sasso")
  print ("sasso batte forbici")
  print ("sara per la prossima partita")
#bot=sasso/player=carta
elif valore_bot != valore_player and valore_bot == 1 and valore_player == 2:
  print ("complimenti hai vinto!!, io ho scelto sasso")
  print ("carta batte sasso")
  print ("voglio la rivincita subito!!")
#bot=carta/player=sasso
elif valore_bot != valore_player and valore_bot == 2 and valore_player == 1:
  print ("che sfortuna hai perso, io ho scelto carta")
  print ("carta batte sasso")
  print ("sara per la prossima partita")
#bot=carta/player=forbici
elif valore_bot != valore_player and valore_bot == 2 and valore_player == 3:
  print ("complimenti hai vinto!!, io ho scelto carta")
  print ("forbice batte carta")
  print ("voglio la rivincita subito!!")
#bot=forbici/player=sasso
elif valore_bot != valore_player and valore_bot == 3 and valore_player == 1:
  print ("complimenti hai vinto!!, io ho scelto forbici")
  print ("sasso batte forbici")
  print ("voglio la rivincita subito!!")
#bot=forbici/player=carta
elif valore_bot != valore_player and valore_bot == 3 and valore_player == 2:
  print ("che sfortuna hai perso, io ho scelto forbici")
  print ("forbice batte carta")
  print ("sara per la prossima partita")


