#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

f = open('slova.txt')
slova = []

for radek in f:
    radek = radek.strip().split(' ')
    radek = [ slovo for slovo in radek
              if len(slovo) <= 8 and
                 len(slovo) >= 3 and
                 slovo[-1] not in "ýáíéůě"
            ]

    if radek:
        slova.append(radek)

f.close()

minule_slovo = None
pouzite = set()

while True:
    clovek = input('Zadej slovo: ')
    existuje = False

    if clovek in pouzite:
        print('Tohle slovo už bylo. Zkus jiné.')
        continue

    for radek in slova:
        for slovo in radek:
            if slovo == clovek:
                existuje = True
                pouzite.update(radek)

    if not existuje:
        print('Tohle slovo neznám, zkus jiné.')
        continue

    if minule_slovo:
        if clovek[0] != minule_slovo[-1]:
            print('Tohle slovo nenavazuje. Zkus jiné.')
            continue

    minule_slovo = clovek

    print('Pěkné slovo. Teď já.')

    pocitac = None

    for radek in slova:
        if radek[0][0] == minule_slovo[-1]:
            if radek[0] not in pouzite:
                pocitac = radek[0]
                pouzite.update(radek)
                break

    if not pocitac:
        print('Nevím jak navázat. Prohrál jsem. :-(')
        break

    print('Moje slovo:', pocitac)
    minule_slovo = pocitac


# vim:set sw=4 ts=4 et:
