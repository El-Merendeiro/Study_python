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

score_player = 0
score_bot = 0

while valore_player == valore_bot:
  print (f"anche io ho scelto {scelta_player}")
  print ("pareggio riproviamo")
  scelta_player = input ("proviamo ancora▷▶ ")
  valore_bot = random.choice(opzioni)

if valore_bot == 1:
  print ("io ho scelto sasso")
elif valore_bot == 2:
  print ("io ho scelto carta")
elif valore_bot == 3:
  print ("io ho scelto forbice")

def gioca():
#bot=sasso/player=forbici
  if valore_bot == 1 and valore_player == 3:
    print ("sasso batte forbici")
    score_bot += 1
#bot=sasso/player=carta
  elif valore_bot == 1 and valore_player == 2:
    print ("carta batte sasso")
    score_player += 1
#bot=carta/player=sasso
  elif valore_bot == 2 and valore_player == 1:
    print ("carta batte sasso")
    score_bot += 1
#bot=carta/player=forbici
  elif valore_bot == 2 and valore_player == 3:
    print ("forbice batte carta")
    score_player += 1
#bot=forbici/player=sasso
  elif valore_bot == 3 and valore_player == 1:
    print ("sasso batte forbici")
    score_player += 1
#bot=forbici/player=carta
  elif valore_bot == 3 and valore_player == 2:
    print ("forbice batte carta")
    score_bot += 1

while score_player < 3 or score_bot < 3:
  gioca ()
  print (f"siamo io a {score_bot} e tu a {scoreplayer} continuiamo")

if player_score == 3:
  print (f"complimenti hai vinto {score_player} a {score_bot}")
  print ("voglio la rivincita")
else:
  print (f"questa partita l'ho vinta io {score_bot} a {score_player}")
  print ("posso darti la rivincita quando vuoi")
