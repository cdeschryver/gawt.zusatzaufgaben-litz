# Lösung Zusatzaufgabe 6.1
# aus Litz, Lothar: Wahrscheinlichkeitstheorie für Ingenieure

# Christian De Schryver, 2016
# This file is public domain.

from math import factorial

# A: Bauelement ist defekt
PA = 0.01
PnotA = 1 - PA


# liefert n über k
def comb(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))


# liefert Binomialverteilung als Summe aller k
def binomial(p, n, k):
	sum = 0
	for i in k:
		sum = sum + comb(n, i) * pow(p, i) * pow((1 - p), n - i)
	return sum


# -----------------------
#     Aufgabenteil  a)
# -----------------------

# 1-20 Ausfälle

# Achtung: range(1,21) erzeugt Liste bis 20! [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(list(range(1,21)))
Pa = binomial(PA, 20, range(1, 21))

# alternativ: 1-kein Ausfall
PaAlternativ = 1 - pow(PnotA, 20)

print(" Lösung Aufgabenteil a): " + str(Pa))
print("       Alternativlösung: " + str(PaAlternativ))
print()

# -----------------------
#     Aufgabenteil b)
# -----------------------

nb = 0
Pb = 0
while (Pb <= 0.5):
	nb = nb + 1
	Pb = binomial(PA, nb, range(1, nb + 1))

print(" Lösung Aufgabenteil b): " + str(nb))
print()

# -----------------------
#     Aufgabenteil c)
# -----------------------

# kein Bernoulliexperiment!
Pc = 3 / 20 * 2 / 19 * 1 / 18

print(" Lösung Aufgabenteil c): " + str(Pc))
print()

# -----------------------
#     Aufgabenteil d)
# -----------------------

Pd = pow(PnotA, 10)

print(" Lösung Aufgabenteil d): " + str(Pd))
print()

# -----------------------
#     Aufgabenteil e)
# -----------------------

PeDefektDurch2UndMehrTeile = binomial(PA, 10, range(2, 11))

# bedingte Wahrscheinlichkeit mit der Bedingung "PC ist defekt"
Pe = PeDefektDurch2UndMehrTeile / (1.0 - Pd)

print(" Lösung Aufgabenteil e): " + str(Pe))
print(PeDefektDurch2UndMehrTeile)
print()

# -----------------------
#     Aufgabenteil f)
# -----------------------

Pf = binomial(1 - Pd, 30, range(0, 2))

print(" Lösung Aufgabenteil f): " + str(Pf))
print()
