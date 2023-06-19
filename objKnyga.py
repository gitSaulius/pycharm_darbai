
# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         # parasyti metoda ar knyga turi >300 psl
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# Knyga1 = Knyga("Dziungles", "Kiplingas", 550)
# Knyga2 = Knyga("Ziedu valdovas", "Rasytoja", 250)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         # parasyti metoda kuris padidins atlyginima tam tikru procentu
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self):
#         print(f"informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1200)

# Darbuotojas1.padidinti_atlyginima(10)
# print(f"{Darbuotojas1.vardas}, {Darbuotojas1.pavarde} gavo nauja atlyginima: {Darbuotojas1.atlyginimas}")
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")

# Darbuotojas1.visa_informacija()

# Darbuotojas2.padidinti_atlyginima(10)
# print(f"{Darbuotojas2.vardas}, {Darbuotojas2.pavarde} gavo nauja atlyginima: {Darbuotojas2.atlyginimas}")


# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#     def atnaujinti_kaina(self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina {nauja_kaina}")
#
#         # pranesti pirkejui kad neturim tiek prekiu (kiek jis nori)
#     def sandelio_likutis(self, pardavimo_kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakanka prekiu: {self.pavadinimas}")
#
#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidintas kiekis {self.pavadinimas} {padidintas_likutis}")
#
# Preke1 = Preke("Pienas", 4, 10)
# Preke2 = Preke("Duona", 2, 5)
#
# Preke1.atnaujinti_kaina(3)
# Preke1.sandelio_likutis(10)
# Preke2.sandelio_likutis(8)
# Preke1.sandelio_papildymas(20)
# Preke2.sandelio_papildymas(12)
# print(Preke1.kiekis)
