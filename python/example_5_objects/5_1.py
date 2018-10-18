#!/usr/bin/env python

### DEBUGGER
import pdb

class Moeble():

    def __init__(self):
        self.name = None
        self.func = None

    def set_name(self, moeble_name):
        self.name = moeble_name

    def set_funktionalitaet(self, name_func):
        self.func = name_func

class Zimmer():

    def __init__(self):
        self.name = None
        self.moebles = []

    def set_name(self, name_zimmer):
        self.name = name_zimmer

    def add_moeble(self, moeble_obj):
        self.moebles.append(moeble_obj)

    def get_zimmer_moebles_names(self):
        print("")
        for moeble in self.moebles:
            print("moebles name: %s" % moeble.name)
        print("")

class Haus():

    def __init__(self):
        self.plz = None
        self.zimmers = []

    def set_plz(self, haus_plz):
        self.plz = haus_plz

    def add_zimmer(self, zimmer):
        self.zimmers.append(zimmer)

    def get_moebles_names(self):
        for zimmer in self.zimmers:
            zimmer.get_zimmer_moebles_names()

    def get_moebles_names_2(self):
        for zimmer in self.zimmers:
            for moeble in zimmer.moebles:
                print("moebles name: %s" % moeble.name)



has = Haus()

zii = Zimmer()
moo = Moeble()
mooo = Moeble()
moo.set_name("Tisch")
mooo.set_name("Stuelle")
zii.add_moeble(moo)
zii.add_moeble(mooo)

ziii = Zimmer()
maa = Moeble()
maaa = Moeble()
maa.set_name("Sofa")
maaa.set_name("Fehrsehen")
ziii.add_moeble(maa)
ziii.add_moeble(maaa)

has.add_zimmer(zii)
has.add_zimmer(ziii)

# has.get_moebles_names()
# print("####################")
# has.get_moebles_names_2()
