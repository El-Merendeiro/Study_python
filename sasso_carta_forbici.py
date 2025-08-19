print ("Benvenuto al classicco gioco, ")
print ("SASSO, CARTA, FORBICI")

knowledge = input ("Conosci gia le le regole?[Si/No]▷▶ ")

if knowledge == "Si" or knowledge == "si":
  print ("ok allora iniziamo subito")

elif knowledge == "No" or knowledge == "no":
  print ("ok nessun problema le regole sono semplicissime")
  print ("entrambi scegliamo una delle 3 opzioni: Sasso, Carta o Forbici")
  print ("La Carta batte il Sasso")
  print ("Il Sasso batte le Forbici")
  print ("Le Forbici battono la Carta")

print ("scegli al mio tre")
import time
for t in range (3,0,-1):
        print (t,end='\r', flush=True)
        time.sleep(1.5)

valore_player = input ("cosa scegli?▷▶ ")
