#!/usr/bin/env python

# import my_haus
from my_haus import Moeble
from my_haus import Zimmer
from my_haus import Haus

haus = Haus()

# def test_neu_zimmer():


print("")
print("Willkommen nach unsere erste OO prog")
print("")

zimmer_name = raw_input("Bitte schreiben name erste zimmer: ")
print "Zimmer name: ", zimmer_name

zimmer = Zimmer()
zimmer.set_name(zimmer_name)
haus.add_zimmer(zimmer)

zimmer_neu = raw_input("Wollen Sie neue Zimmer eingeben: (J/N) ")

while (zimmer_neu == 'J' or zimmer_neu == 'j'):
        print("Eingabe neue Zimmer")
        zimmer_name = raw_input("Bitte schreiben name andere zimmer: ")
        print "Zimmer name: ", zimmer_name

        zimmer = Zimmer()
        zimmer.set_name(zimmer_name)
        haus.add_zimmer(zimmer)

        zimmer_neu = raw_input("Wollen Sie neue Zimmer eingeben: (J/N) ")

for zimmer in haus.zimmers:
    moeble_neu = raw_input("Moeble fuer zimmer %s eingeben?: (J/N) " % zimmer.name )

    while (moeble_neu == 'J' or moeble_neu == 'j'):
        print("Eingabe neue Moeble")
        moeble = Moeble()
        moeble_name = raw_input("Bitte schreiben die moeble name: ")
        moeble.set_name(moeble_name)

        moeble_preis = raw_input("Bitte schreiben die moeble preis: ")
        moeble.preis = float(moeble_preis)

        zimmer.add_moeble(moeble)

        moeble_neu = raw_input("Neue moeble fuer zimmer %s eingeben?: (J/N) " % zimmer.name )
print("")
total_haus = 0
for zimmer in haus.zimmers:

    zimmer_total = zimmer.get_zimmer_kosten()
    print("Zimmer %s hast total kosten von %f" % (zimmer.name, zimmer_total))

    total_haus = total_haus + zimmer_total

print("")
print("Total kosten haus: %f" % total_haus)
