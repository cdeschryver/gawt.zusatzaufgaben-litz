# Lösung Zusatzaufgabe 5.2
# aus Litz, Lothar: Wahrscheinlichkeitstheorie für Ingenieure

# Christian De Schryver, 2016
# This file is public domain.

from math import factorial

# A: kein Ausfall
PA = 0.9
PnotA = 1 - PA


# liefert n über k
def comb(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))


# ---------------------
#     Aufgabe 5.1 a)
# ---------------------

# kein Ausfall
PA0 = pow(PA, 10)

# ein Ausfall
# Hinweis: es gibt 10 Möglichkeiten, dass eine spezielle Einrichtung ausfällt!
PA1 = pow(PA, 9) * pow(PnotA, 1) * comb(10, 1)

# zwei Ausfälle
PA2 = pow(PA, 8) * pow(PnotA, 2) * comb(10, 2)

# gesuchte Wahrscheinlichkeit
Pa = PA0 + PA1 + PA2

print(" Lösung Aufgabenteil a): " + str(Pa))

# ---------------------
#     Aufgabe 5.1 b)
# ---------------------

Pb = pow(PnotA, 10)

print(" Lösung Aufgabenteil b): " + str(Pb))

print(comb(5,4))