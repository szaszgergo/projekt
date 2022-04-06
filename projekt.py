class Eszkoz:
    def __init__(self, nev, ar, db):
        self.nev = nev
        self.ar = ar
        self.db = db


eszkozok = []
#5 eszkoz fajta van
while True:
    print("Nyomj ENTER-t a kilépéshez")
    nev = input("Add meg az eszköz nevét: ")
    if nev == "":
        break
    ar = int(input(f"Add meg a {nev} árát: "))
    db = int(input(f"Add meg a {nev}-k darabszámát: "))
    eszkozok.append(Eszkoz(nev,ar,db))


ossz = 0
for eszkoz in eszkozok:
    ossz += eszkoz.ar * eszkoz.db

print(f"{ossz}Ft ba fog kerülni a hálózat felépítése.")
