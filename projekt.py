class Eszkoz:
    def __init__(self, nev, ar, db):
        self.nev = nev
        self.ar = ar
        self.db = db


eszkozok = []
#5 eszkoz fajta van
for i in range(5):
    nev = input("Add meg az eszköz nevét: ")
    ar = int(input("Add meg az eszköz árát: "))
    db = int(input(f"Add meg a {nev} darabszámát: "))
    eszkozok.append(Eszkoz(nev,ar,db))


ossz = 0
for eszkoz in eszkozok:
    ossz += eszkoz.ar * eszkoz.db

print(f"{ossz}Ft ba fog kerülni a hálózat felépítése.")