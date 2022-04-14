class Eszkoz:
    def __init__(self, nev, ar, db):
        self.nev = nev
        self.ar = ar
        self.db = db


eszkozok = []
while True:
    print("Nyomj ENTER-t a kilépéshez")
    nev = input("Add meg az eszköz nevét: ")
    if not nev:
        break
    ar = input(f"Add meg a {nev} árát: ")
    if not ar:
        break
    db = input(f"Add meg a {nev}-k darabszámát: ")
    if not db:
        break
    eszkozok.append(Eszkoz(nev,int(ar),int(db)))

ossz = 0
for eszkoz in eszkozok:
    ossz += eszkoz.ar * eszkoz.db

f = open('koltsegek.txt', 'w')
for eszkoz in eszkozok:
    f.write(f'{eszkoz.nev} \n ára: {eszkoz.ar} \n darabszáma: {eszkoz.db} \n összköltsége: {eszkoz.db * eszkoz.ar} \n')
f.write(f"{ossz}Ft ba fog kerülni a teljes hálózat felépítése.")
f.close()

