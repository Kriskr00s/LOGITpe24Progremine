perepikkus = []
hetk = 1.0
while (hetk != 0.0):
    hetk = float(input("Sisesta perekonnaliikmete pikkus meetrides, kui rohkem ei ole liikmeid siis sisest 0 või 0.0"))
    if hetk != 0.0:
        perepikkus.append(hetk)
print(perepikkus)
jagaja = len(perepikkus)
jagatav = 0.0
tsüklimuutuja = 0
while tsüklimuutuja < jagaja:
    jagatav+= perepikkus[tsüklimuutuja]
    tsüklimuutuja += 1
keskminepikkus = jagatav / jagaja
print(keskminepikkus)