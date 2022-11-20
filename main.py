

# streichholzspiel
print("Beim Streichholzspiel liegen zu Beginn 13 Streichhölzer auf dem Tisch")
print("Zwei Spieler nehmen abwechselnd ein, zwei oder drei Streichhölzer weg.")
print("Die Person, die das letzte Streichholz nimmt, gewinnt. !!!\n")

# Spielbeginn
spiel_aktiv = True
anzahl_streich = 11
spieler_1 = str(input("Bitte geben Sie den Namen des 1. Spielers ein: "))
reihenfolge = spieler_1
spieler_2 = str(input("Bitte geben Sie den Namen des 2. Spielers ein: "))


# ich habe das Format des Spiels vorbereitet
def spiel_zeichnen():
    print("\n" + "====== " * anzahl_streich)
    for i in range(1, (anzahl_streich + 1)):
        print("|", format(i, "02d"), "|", end=" ")
    print("\n" + "====== " * anzahl_streich)


# ich habe den Bildschirm vorbereitet, der am Ende des Spiels erscheinen wird
def spiel_ende():
    gewinnen = ("Spiel ist aus. Spieler " + reihenfolge + " hat gewonnen.")
    lange = len(gewinnen) + 6
    print("=" * lange, end="\n")
    print("|| " + gewinnen + " ||")
    print("=" * lange, end="\n")


def spieler_anmelden():
    global spiel_aktiv
    while True:
        bewegung = input("Bitte geben Sie die Anzahl des Streichs ein, die Sie ziehen möchten: ")
        if bewegung == "Q" or bewegung == "q":
            spiel_aktiv = False
            return
        try:
            # damit es keine falsch eingegebenen Nummern akzeptiert
            bewegung = int(bewegung)
        except ValueError:
            print("Bitte geben Sie eine Zahl zwischen 1 und 3 ein oder drücken Sie Q/q zum Beenden")
        else:
            # sodass nur 1-3 Nummern ausgewählt werden können
            if bewegung >= 1 and bewegung <= 3:
                return bewegung
            else:
                print("Die gewählte Zahl muss zwischen 1 und 3 liegen. Drücken Sie zum Beenden Q/q")


# damit die Spieler abwechselnd spielen
def spieler_wechseln():
    global reihenfolge
    if reihenfolge == spieler_1:
        reihenfolge = spieler_2
    else:
        reihenfolge = spieler_1


def gewinn_kontrol():
    if anzahl_streich <= 0:
        gewonnen = 1
        return gewonnen
    else:
        spiel_zeichnen()


spiel_zeichnen()

while spiel_aktiv:
    print()
    print("Spieler: " + reihenfolge)
    bewegung = spieler_anmelden()
    if bewegung:
        anzahl_streich = anzahl_streich - bewegung
        gewonnen = gewinn_kontrol()
        if gewonnen:
            print()
            spiel_ende()
            spiel_aktiv = False
            break
        spieler_wechseln()
print()
