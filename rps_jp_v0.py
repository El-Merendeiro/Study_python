import time, random
scelte = ["グー","ぐー","パー","ぱー","チョキ","ちょき"]
print("たのしいゲームへようこそ！")
print("グー・パー・チョキ！")
time.sleep(1)

knowledge = input("ルールをしってる？[はい/いいえ]▷▶ ")

if knowledge == "はい" or knowledge == "ハイ":
    print("わかった！じゃあはじめよう！")
    time.sleep(1)
elif knowledge == "いいえ" or knowledge == "イイエ":
    print("だいじょうぶ！ルールはかんたんだよ！")
    print("ふたりとも３つのなかからえらぶよ：グー・パー・チョキ")
    time.sleep(0.5)
    print("パーはグーにかつ")
    print("グーはチョキにかつ")
    print("チョキはパーにかつ")
    time.sleep(1)

opzioni = [1, 2, 3]
valore_bot = random.choice(opzioni)
score_player = 0
score_bot = 0

def game():
    print("３でえらんでね！")
    for t in range(3, 0, -1):
        print(t, end='\r', flush=True)
        time.sleep(1.5)

    scelta_player = input("なにをえらぶ？▷▶ ")

    while scelta_player not in scelte:
        print("そのえらびかたはだめだよ")
        print("グー・パー・チョキからえらんでね")
        scelta_player = input("もういちど▷▶ ")
    else:
        print(f"きみは {scelta_player} にしたね")

    if scelta_player in ["グー", "ぐー"]:
        valore_player = 1
    elif scelta_player in ["パー", "ぱー"]:
        valore_player = 2
    elif scelta_player in ["チョキ", "ちょき"]:
        valore_player = 3

    global opzioni
    global valore_bot
    while valore_player == valore_bot:
        print(f"ぼくも {scelta_player} にしたよ")
        print("あいこ！もういちど！")
        scelta_player = input("もういちど▷▶ ")
        valore_bot = random.choice(opzioni)

    if valore_bot == 1:
        print("ぼくはグーにしたよ")
    elif valore_bot == 2:
        print("ぼくはパーにしたよ")
    elif valore_bot == 3:
        print("ぼくはチョキにしたよ")

    global score_player
    global score_bot
# bot=グー / player=チョキ
    if valore_bot == 1 and valore_player == 3:
        print("グーはチョキにかつ")
        valore_bot = random.choice(opzioni)
        score_bot += 1
# bot=グー / player=パー
    elif valore_bot == 1 and valore_player == 2:
        print("パーはグーにかつ")
        valore_bot = random.choice(opzioni)
        score_player += 1
# bot=パー / player=グー
    elif valore_bot == 2 and valore_player == 1:
        print("パーはグーにかつ")
        valore_bot = random.choice(opzioni)
        score_bot += 1
# bot=パー / player=チョキ
    elif valore_bot == 2 and valore_player == 3:
        print("チョキはパーにかつ")
        valore_bot = random.choice(opzioni)
        score_player += 1
# bot=チョキ / player=グー
    elif valore_bot == 3 and valore_player == 1:
        print("グーはチョキにかつ")
        valore_bot = random.choice(opzioni)
        score_player += 1
# bot=チョキ / player=パー
    elif valore_bot == 3 and valore_player == 2:
        print("チョキはパーにかつ")
        valore_bot = random.choice(opzioni)
        score_bot += 1

while score_player < 3 and score_bot < 3:
    game()
    if score_player < 3 and score_bot < 3:
      print(f"ぼく {score_bot} たい きみ {score_player} ！つづけよう！")

if score_player == 3:
    print(f"おめでとう！きみのかち！ {score_player} たい {score_bot}")
    print("ぼくはリベンジしたいな！")
else:
    print(f"ぼくのかち！ {score_bot} たい {score_player}")
    print("またやろうね！")
