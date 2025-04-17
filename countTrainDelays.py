# Dieses Programm bezieht sich auf eine Prüfungsaufgabe (Aufgabe 1 - AP2 Winter 2024)
# der IHK. Es soll ein Algorithmus erstellt werden in Pseudo-Code (hab ich bereits gemacht)
# welcher in einem Array erfasste Zug-Abfahrtzeiten an mehreren Haltestellen auswertet
# und die Fahrtzeit zwischen zwei aufeinanderfolgenden Haltestellen ermittelt, und prüft ob 
# die tatsächliche Fahrtzeit über der geplanten Fahrtzeit liegt.
# Wenn dies zutrifft, dann soll in einem eindimensionalen Array für jeden Steckenabschnitt 
# zwischen den Haltestellen die Anzahl an Verspätungen hochgezählt werden, wenn die tatsächliche
# Fahrtzeit größer ist als die geplante Fahrtzeit PLUS 2 Minuten !

import random

    # Array 'zeiten' initialisieren
class Abfahrtszeit:

    datum = ""
    haltestellenNr = 0
    planAbfahrt = 0
    istAbfahrt = 0

    def __init__(self, datum, haltestellenNr, planAbfahrt, istAbfahrt):
        self.datum = datum
        self.haltestellenNr = haltestellenNr
        self.planAbfahrt = planAbfahrt
        self.istAbfahrt = istAbfahrt

def ermittle_verspaetungen(times):
    delays = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(len(times) - 1):
        if ((times[i+1].planAbfahrt - times[i].planAbfahrt) + 2 < (times[i+1].istAbfahrt - times[i].istAbfahrt)):
            delays[times[i].haltestellenNr] += 1

    return delays

zeiten = []
weekday = "Montag"
day = 1
month = 1
year = 2025

for i in range(60):
    pAbf = random.randint(0, 1000)
    iAbf = pAbf + random.randint(0, 30)
    haltSt = random.randint(0, 14)

    line = Abfahrtszeit("{}, {}.{}.{}".format(weekday, day, month, year), haltSt, pAbf, iAbf)
    zeiten.append(line)
    year = (year + 1) if (month == 12 and day == 31) else year
    weekday = "Dienstag" if weekday == "Montag" else "Mittwoch" if weekday == "Dienstag" else "Donnerstag" if weekday == "Mittwoch" else "Freitag" if weekday == "Donnerstag" else "Samstag" if weekday == "Freitag" else "Sonntag" if weekday == "Samstag" else "Montag"
    day = day + 1 if day < 31 else 1
    month = (month + 1) if day == 1 else month

#DEBUG AUSGABE:
    #Datum, gepl. Abfahrt, tatsächl. Abfahrt
for i in range(len(zeiten)):
    print("Datum: " + str(zeiten[i].datum))
    print("geplante Abfahrt: " + str(zeiten[i].planAbfahrt))
    print("tatsächl Abfahrt: " + str(zeiten[i].istAbfahrt))
    print("Haltestelle: " + str(zeiten[i].haltestellenNr))

    #Delays Ausgabe:
if (not ermittle_verspaetungen(zeiten)):
    print("Array ist leer")
else:
    print(ermittle_verspaetungen(zeiten))

input()