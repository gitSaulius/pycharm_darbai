# -------------------------------------------------------
# -----06.19-------

# 1.Parašykite programą, kuri atspausdina visus lyginius skaičius nuo 1 iki 10.
# destytojo
# sarasas = range(1, 11)
# for skaicius in range(2, 11, 2):
#     print(skaicius, end=" ")

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         print(skaicius)        ---------stulpeliu
#         print(skaicius, end=" ")   -----eilute


# 2.Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą.

# sarasas = [1, 3, 6, 5]
# suma = 0
# for skaicius in sarasas:
#     suma = sum(sarasas)
# print(suma)

# sarasas = [1, 3, 6, 5]
# suma = 0
# for skaicius in sarasas:
#     suma += skaicius
# print("Saraso skaiciu suma:", suma)


# 3.Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3,
# atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz";

# for skaicius in range (1, 21):
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         print("Fizz, Buzz")
#     elif skaicius % 3 == 0:
#         print("Fizz")
#     elif skaicius % 5 == 0:
#         print("Buzz")
#     else:
#         print(skaicius)


# 4.Sukurkite klasę "KnygosBiblioteka", turinčią atributą "knygos" (sąrašą) ir metodus "pridėti_knygą" ir "rodyti
# _knygas". Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas bibliotekoje
# esančias knygas.

# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#         print(f"Knyga {knyga} prideta sekmingai")
#
#     def rodyti_knygas(self):
#         if self.knygos:
#             print("Knygos:")
#             for knyga in self.knygos:
#                 print(knyga)
#         else:
#             print("Biblioteka tuscia")
#
# knyga = KnygosBiblioteka()
# knyga.prideti_knyga("Trys muskietininkai")
# knyga.prideti_knyga("Buratino nuotykiai")
# knyga.rodyti_knygas()


# 5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą, kuri suskaičiuoja ir atspausdina
# visų prekių kainų sumą.

# prekes = {
#     "obuoliai": 1.98,
#     "persikai": 3.29,
#     "agurkai": 3.50
# }
# suma = 0
# for kaina in prekes.values():
#     suma += kaina
#
# print(f"Visu prekiu kainu suma: {suma}")


# atspausdinti tik for pagalba trikampi

# eilutes = 6
# for i in range (1, eilutes +1):
#     print(" " * (eilutes - i), end="")
#     print("*" * (2 * i-1))
# print(" " * (eilutes - 1), end="")
# print("|")


