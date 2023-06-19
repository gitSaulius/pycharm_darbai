# Sukurkite klasę "Mokinys", turinčią atributus "vardas", "pavarde" ir "pazymiai".
# Parašykite metodą, kuris pridės naują pažymį prie mokinio pažymių sąrašo.
# Parašykite metodą, kuris suskaičiuos mokinio pažymių vidurkį.
# Sukurkite kelis objektus iš šios klasės su skirtingais pažymiais ir patikrinkite, ar vidurkis skaičiuojamas teisingai.

class Mokinys:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Pazymiai(Mokinys):
    def __init__(self, vardas, pavarde, pazymiai):
        super().__init__(vardas, pavarde)
        self.pazymiai = []

    def prideti_pazymi(self, pazymis):
        self.pazymiai.append(pazymis)
        print(f"Pazymis {pazymis} i dienyna irasytas")

    def skaiciuoti_vidurki(self):
        vidurkis = 0
        for pazymis in self.pazymiai:
            vidurkis = sum(self.pazymiai) / len(self.pazymiai)
            print(vidurkis)


moksleivis1 = Mokinys("Jonas", "Jonaitis")
moksleivis2 = Mokinys("Petras", "Petraitis")

pazymiai1 = [8, 6, 9, 5, 7, 10, 8, 7, 7, 9]
pazymiai2 = [5, 6, 8, 5, 7, 6, 9, 7, 6, 8]













