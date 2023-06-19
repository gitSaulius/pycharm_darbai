# Parašykite programą, studentų valdymo sistemą ir leistų vartotojui įvesti komandas, kad galėtų manipuliuoti studentų
# duomenimis.
# 1.Pridėti naują studentą
# 2.Pašalinti studentą
# 3.Gauti informaciją apie studentą pagal studento ID
# 4.Rodyti visus studentus
# 5.Baigti programą
# Vartotojas įveda pasirinkimo numerį, o programa atlieka atitinkamą veiksmą naudodama studentų valdymo sistemą.

class Universitetas:
    def __init__(self):
        self.studentai = []
    def naujas_irasas(self, vardas, pavarde, studento_id, fakultetas, specialybe):
        irasas = {
            "vardas": vardas,
            "pavarde": pavarde,
            "studento id": studento_id,
            "fakultetas": fakultetas,
            "specialybe": specialybe
            }
        self.studentai.append(irasas)
        print("Naujas irasas sekmingai sukurtas")

    def pasalinti_irasa(self, studento_id):
        for irasas in self.studentai:
            if irasas["studento id"] == studento_id:
                self.studentai.remove(irasas)
                print("Irasas buvo sekmingai pasalintas")
                break
            else:
                print("Toks irasas nesurastas! Bandykite dar karta.")
                return

    def parodyti_info(self, studento_id):
        for irasas in self.studentai:
            if irasas["studento id"] == studento_id:
                print(f"{vardas} {pavarde}, studento id: {studento_id}, fakultetas: {fakultetas}, specialybe: {specialybe}")
                break
            else:
                print("Toks irasas nesurastas! Bandykite dar karta.")
                return

    def rodyti_visus_irasus(self):
        for irasas in range(0, len(self.studentai)):
            print(f"{vardas} {pavarde}, studento id: {studento_id}, fakultetas: {fakultetas}, specialybe: {specialybe}")
        if not self.studentai:
            print("Irasu nerasta")
            return


vcsu=Universitetas()

while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sukurti nauja studento irasa")
    print("2. Pasalinti studento irasa")
    print("3. Patikrinti studento informacija pagal studento id")
    print("4. Parodyti visus studentus")
    print("0. Baigti programa")
    pasirinkimas = input("Iveskite pasirinkimo numeri_> ")


    if pasirinkimas == "1":
        vardas = input("Iveskite varda_> ")
        pavarde = input("Iveskite pavarde_> ")
        studento_id = int(input("Iveskite studento ID numeri_> "))
        fakultetas = input("Iveskite fakulteto pavadinima_> ")
        specialybe = input("Iveskite studiju specialybe_> ")
        vcsu.naujas_irasas(vardas, pavarde, studento_id, fakultetas, specialybe)

    elif pasirinkimas == "2":
        studento_id = int(input("Iveskite studento ID numeri_> "))
        vcsu.pasalinti_irasa(studento_id)

    elif pasirinkimas =="3":
        studento_id = int(input("Iveskite studento ID numeri_> "))
        vcsu.parodyti_info(studento_id)

    elif pasirinkimas == "4":
        print("Universiteto studentai: ")
        vcsu.rodyti_visus_irasus()

    elif pasirinkimas == "0":
        break

