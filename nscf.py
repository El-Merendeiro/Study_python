import time, random
scelte = ["Sasso","sasso","Carta","carta","Forbice","forbice","Forbici","forbici"]
print ("Benvenuto al classicco gioco, ")
print ("SASSO, CARTA, FORBICI")
time.sleep(1)

knowledge = input ("Conosci gia le le regole?[Si/No]▷▶ ")

if knowledge == "Si" or knowledge == "si":
  print ("ok allora iniziamo subito")
  time.sleep(1)
elif knowledge == "No" or knowledge == "no":
  print ("ok nessun problema le regole sono semplicissime")
  print ("entrambi scegliamo una delle 3 opzioni: Sasso, Carta o Forbici")
  time.sleep(0.5)
  print ("La Carta batte il Sasso")
  print ("Il Sasso batte le Forbici")
  print ("Le Forbici battono la Carta")
  time.sleep(1)

opzioni = [1,2,3]
valore_bot = random.choice(opzioni)

print ("scegli al mio tre")
import time
for t in range (3,0,-1):
        print (t,end='\r', flush=True)
        time.sleep(1.5)
scelta_player = input ("cosa scegli?▷▶ ")

while scelta_player not in scelte:
  print ("la scelta non e valida")
  print ("devi scegliere tra: Sasso, Carta o Forbici")
  scelta_player = input ("prova di nuovo▷▶ ")
else:
  print (f"hai scelto {scelta_player}")

if scelta_player == "sasso" or scelta == "Sasso" or scelta == "SASSO":
  valore_player = 1
elif scelta_player == "Carta" or scelta == "carta" or scelta == "CARTA":
  valore_player = 2
elif scelta_player == "Forbice" or scelta == "forbice" or scelta == "Forbici" or scelta == "forbici":
  valore_player = 3

while valore_player == valore_bot:
  print (f"anche io ho scelto {scelta_player}")
  print ("pareggio riproviamo")
  scelta_player = input ("proviamo ancora▷▶ ")
  valore_bot = random.choice(opzioni)
else:
  print ("fine")
