# Dieses Programm bezieht sich auf eine Prüfungsaufgabe (Aufgabe 1 - AP2 Winter 2024)
# der IHK. Es soll ein Algorithmus erstellt werden in Pseudo-Code (hab ich bereits gemacht)
# welcher in einem Array erfasste Zug-Abfahrtzeiten an mehreren Haltestellen auswertet
# und die Fahrtzeit zwischen zwei aufeinanderfolgenden Haltestellen ermittelt, und prüft ob 
# die tatsächliche Fahrtzeit über der geplanten Fahrtzeit liegt.
# Wenn dies zutrifft, dann soll in einem eindimensionalen Array für jeden Steckenabschnitt 
# zwischen den Haltestellen die Anzahl an Verspätungen hochgezählt werden, wenn die tatsächliche
# Fahrtzeit größer ist als die geplante Fahrtzeit PLUS 2 Minuten !

import random

zeiten = []
weekday = "Montag"
day = 1
month = 1
year = 2025

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

def generateZeitenList(weekday, day, month, year):    
    for i in range(7):
        haltSt = 0
        for i in range(33):            
            pAbf = random.randint(0, 900)
            iAbf = pAbf + random.randint(0, 30)

            line = Abfahrtszeit("{}, {}.{}.{}".format(weekday, day, month, year), haltSt, pAbf, iAbf)
            zeiten.append(line)
            haltSt = haltSt + 1 if haltSt < 14 else 0
        year = (year + 1) if (month == 12 and day == 31) else year
        weekday = "Dienstag" if weekday == "Montag" else "Mittwoch" if weekday == "Dienstag" else "Donnerstag" if weekday == "Mittwoch" else "Freitag" if weekday == "Donnerstag" else "Samstag" if weekday == "Freitag" else "Sonntag" if weekday == "Samstag" else "Montag"
        day = day + 1 if day < 31 else 1
        month = (month + 1) if day == 1 else month

def ermittle_verspaetungen(zeiten):
    allDelays       = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    mondayDelays    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    tuesdayDelays   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    wednesdayDelays = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    thursdayDelays  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fridayDelays    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    saturdayDelays  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sundayDelays    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(len(zeiten) - 1):
        if ((zeiten[i+1].planAbfahrt - zeiten[i].planAbfahrt) + 2 < (zeiten[i+1].istAbfahrt - zeiten[i].istAbfahrt)):
            allDelays[zeiten[i].haltestellenNr] += 1

            if ("Montag"        in zeiten[i].datum):
                mondayDelays[zeiten[i].haltestellenNr] += 1
            if ("Dienstag"      in zeiten[i].datum):
                tuesdayDelays[zeiten[i].haltestellenNr] += 1
            if ("Mittwoch"      in zeiten[i].datum):
                wednesdayDelays[zeiten[i].haltestellenNr] += 1
            if ("Donnerstag"    in zeiten[i].datum):
                thursdayDelays[zeiten[i].haltestellenNr] += 1
            if ("Freitag"       in zeiten[i].datum):
                fridayDelays[zeiten[i].haltestellenNr] += 1
            if ("Samstag"       in zeiten[i].datum):
                saturdayDelays[zeiten[i].haltestellenNr] += 1
            if ("Sonntag"       in zeiten[i].datum):
                sundayDelays[zeiten[i].haltestellenNr] += 1
    
    delays = {
        "Verspätungen\t(von links, Streckenabschnitt 0 bis 14)": "\n",
        "Montags"     : mondayDelays, 
        "Dienstags"   : tuesdayDelays, 
        "Mittwochs"   : wednesdayDelays, 
        "Donnerstags" : thursdayDelays, 
        "Freitags"    : fridayDelays, 
        "Samstags"    : saturdayDelays, 
        "Sonntags"    : sundayDelays,
        "GESAMT"      : allDelays
    }
    return delays

def outputObjData():
            #DEBUG AUSGABE:
    #Datum, Haltestelle, gepl. Abfahrt, tatsächl. Abfahrt
    for i in range(len(zeiten)):
        print("Datum: " + str(zeiten[i].datum))
        print("Haltestelle: " + str(zeiten[i].haltestellenNr))
        print("geplante Abfahrt: " + str(zeiten[i].planAbfahrt))
        print("tatsächl Abfahrt: " + str(zeiten[i].istAbfahrt))
        print("")

def outputDelaysData():
        #Delays (Dictionary) Ausgabe:
    if (not ermittle_verspaetungen(zeiten)):
        print("Dictionary ist leer")
    else:
        for key, value in ermittle_verspaetungen(zeiten).items():
            print("\t\t\t{} :\t{}".format(key, value))

generateZeitenList(weekday, day, month, year)
outputObjData()
outputDelaysData()
input()