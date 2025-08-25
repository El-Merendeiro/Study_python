import random, time

opzioni = {"sasso": 1, "carta": 2, "forbici": 3}
risultati = {
    (1, 1): "Pareggio", (2, 2): "Pareggio", (3, 3): "Pareggio",
    (1, 3): "Hai perso", (1, 2): "Hai vinto", (2, 1): "Hai perso",
    (2, 3): "Hai vinto", (3, 1): "Hai vinto", (3, 2): "Hai perso"
}

def gioca():
    scelta = input("Cosa scegli?▷▶ ").lower()
    if scelta not in opzioni:
        print("Scelta non valida.")
        return
    valore_player = opzioni[scelta]
    valore_bot = random.choice(list(opzioni.values()))
    risultato = risultati.get((valore_bot, valore_player))
    print(f"Ho scelto {list(opzioni.keys())[list(opzioni.values()).index(valore_bot)]}. {risultato}!")
    if risultato == "Pareggio": gioca()

print("Benvenuto al classicco gioco, SASSO, CARTA, FORBICI")
if input("Conosci le regole?[Si/No]▷▶ ").lower() == "no":
    print("La Carta batte il Sasso\nIl Sasso batte le Forbici\nLe Forbici battono la Carta")

print("Scegli al mio tre")
for t in range(3, 0, -1):
    print(t, end='\r', flush=True)
    time.sleep(1.5)

gioca()
