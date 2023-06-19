"""
multi-komentavimas
"""
# spausdinimas
# print(vardas)
#
# vardas = "Modestas"
# amzius = 25
#
# arVartotojasAktyvus = False
# produktoKaina = 3.99
# print(type(produktoKaina))
#
# miestai =["Vilniuje", "Kaunas", "Klaipeda"]
#
# miestai[1] = "Siauliai"
# miestai.append("Panevezys")
# miestai.insert(1, "Anyksciai")
# miestai.pop()
# istrina paskutini elementa is saraso
# istrina nurodyta vieta
# del miestai[2]
#
# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))
#
# if amzius == 18:
#     print("Pilnametis")
#
# elif amzius >= 24:
#     print("Daugiau nei 18")
# else:
#     print("Nepilnametis")
#
# skaiciuSarasas = [1, 3, 53, 123, 1245, 12312]
#
# print(len(miestai))
#
# if len(skaiciuSarasas) >0:
#     print("Skaiciu sarasas pilnas")
# else:
#     print("Skaiciu sarasas tuscias")
#
# zodis = "Kaunas"
#
#  if zodis in miestai:
#     print("Zodis " + zodis + " egzistuoja sarase")
#
# else:
#     print("Zodis nerastas")
#
# skaicius = int(input("Iveskite skaiciu: "))
#
# if skaicius > 0:
#     print("Skaicius yra teigiamas")
# elif skaicius <0:
#     print("Skaicius yra neigiamas")
# else:
#     print("Skaicius yra nulis")

"""
Priskirimo operatoriai
= Priskirimas
+= Prideda ir priskiria
-= Atima ir priskiria
*=
/=
%=
Matematiniai operatoriai
+
-
*
/
% trupmena
** kelimas laipsniu
// sveikoji dalyba
Palyginimo operatoriai
== lygu
!= nelygu
>
<
>=
<=
Loginiai operatoriai
and
or
not
Narystes operatoriai
in
not in
Tapatumo operatoriai
is
is not
"""

# Uzduotys

# 1. Patikrinkite, ar studentas išlaikė egzaminą;

# mano
# vardas = "Studentas"
# egzaminas = 7
# if egzaminas >= 5:
#     print("Studentas egzamina islaike")
# else:
#     print("Neislaike")

# Deivido
# ivertinimas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# islaikymoRiba = 5
# ivertinimas = int(input("Iveskite ivertinima: "))
# if ivertinimas >= islaikymoRiba:
#     print("Egzaminas islaikytas")
# else:
#     print("Egzaminas neislaikytas")


# 2. Patikrinkite, ar skaičius yra lyginis;

# Skaicius = 120

# galima iterpti ir tokia eilute:  ivertinimas = int(input("Iveskite ivertinima: "))

# if Skaicius % 2 == 0:
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis skaicius")


# 3. Patikrinkite, ar sąraše yra bent du skaičiai

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# if len(sarasas) >= 2:
#     print("yra 2 skaiciai")
# else:
#     print("nera 2 skaiciu")

# Teorija
# ciklas
# for index in range(1, 11):
#     print(index)

# vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]
#
#      key       value
# for vardas in vardai:
#     print(vardas)

# atrinkti ir sudeti skaicius i sarasa pagal nurodyta salyga:
# skaiciai = [10, 20, 30, 40, 50, 23]
# atrinkti = []
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius)
# print("Atrinkti skaiciai: ", atrinkti)


# atrinkti unikalias reiksmes is saraso:
# skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44, 11, 21]
# unikalios_reiksmes = []
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:
#         unikalios_reiksmes.append(skaicius)
# print("Unikalios reiksmes: ", unikalios_reiksmes)


# Teorija. Funkcijos

# def suma(a, b):
#     return a + b
# rezultatas = suma(2, 5)
# print("Suma: ", rezultatas)


# def pasisveikinimas(vardas="Anonimas"):
#     print("Labas,", vardas)
# pasisveikinimas("Modestas")


# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
# sarasas1 = [1, 2, 3]
# sarasas2 = [4, 5, 6]
# rezultatas = sujungti_sarasus(sarasas1, sarasas2)
# print("Sujungtas sarasas: ", rezultatas)

# Uzduotys

# 1.Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina,
# ar skaičius yra lyginis. Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False.

# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print(ar_lyginis(9))

# 2. Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;

# def didziausias_skaicius(sarasas):
#     didziausias = sarasas [0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# skaiciusarasas = [5, 8, 2, 6, 9, 15, 20, 11]
# rezultatas = didziausias_skaicius (skaiciusarasas)
# print(rezultatas)

# 3. Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą,
# kuriame yra tik unikalios reikšmės iš pradinio sąrašo.

# def unikalios_reiksmes(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_sarasas:
#             tuscias_sarasas.append(reiksme)
#     return tuscias_sarasas
# naujas_sarasas = [5, 6, 9, 1, 5, 7, 10, 6, 8, 10]
# print(unikalios_reiksmes(naujas_sarasas))

"""
N.D.
1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai. 
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.

2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo. 
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.

3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.
"""

# 1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.

# pradinis_sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma_nelyginiu = []
# for nelyginis_skaicius in pradinis_sarasas:
#     if nelyginis_skaicius % 2 != 0:
#         suma_nelyginiu.append(nelyginis_skaicius)
#         SUM = sum(suma_nelyginiu)
# print(SUM)

# def suma_nelyginiu(sarasas):
#     suma = 0
#     for nelyginis_skaicius in sarasas:
#         if nelyginis_skaicius % 2 != 0:
#             suma += nelyginis_skaicius
#     return suma
# pradinis_sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = suma_nelyginiu(pradinis_sarasas)
# print(rezultatas)






# 2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.

# pradinis_sarasas = [5, 9, 22, 38, 70, 10, 40, 77]
# def didziausias_skaicius(sarasas):
#      didziausias = sarasas [0]
#      for skaicius in sarasas:
#          if skaicius > didziausias:
#              didziausias = skaicius
#      return didziausias
# rezultatas = didziausias_skaicius (pradinis_sarasas)
# print(rezultatas)


# 3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.

# skaicius = int(input("Iveskite skaiciu: "))
# if skaicius == 1:
#     print(skaicius, "nera pirminis skaicius")
# elif skaicius > 1:
#     for i in range(2, skaicius):
#         if (skaicius % i) == 0:
#             print(skaicius, "nera pirminis skaicius")
#             print(i, "*", skaicius // i, "=", skaicius)
#             break
#     else:
#         print(skaicius, "yra pirminis skaicius")
# else:
#     print(skaicius, "nera pirminis skaicius")

# 2 variantas
# def pirminis_skaicius (skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range (2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# skaicius = 100
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius} yra pirminis skaicius")
# else:
#     print(f"skaicius {skaicius} yra ne pirminis skaicius")


#-------06.13---------

# ----paprasti pavyzdukai su while
# skaicius = 1
# while skaicius <= 5:
#     print(skaicius)
#     skaicius += 1

# ----paprasyti vartotojo ivesti skaiciu ir atspausdinti visus lyginius skaicius nuo ivesto skaiciaus
# skaicius = int(input("Iveskite skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1


# sarasas1 = [1, 2, 3]
# sarasas2 = [4, 5, 6]
# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
# rezultatas = sujungti_sarasus(sarasas1, sarasas2)
# print("Sujungtas sarasas: ", rezultatas)

# # perkelti vykdymo mygtuka prie rasomos eilutes

# if __name__ == '__main__':
#     sujungti_sarasus(sarasas1, sarasas2)


#----- 06.14

# Dictionary

# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 27,
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
# zmogus["lytis"] = "Vyras"
# # pridedame nauja elementa i savo zodyna
# print(f"As esu zmogus['lytis']")
#
# # keiciame reiksmes
#
# zmogus["amzius"] = 20
#
# print("Atsiprasau man yra:", zmogus['amzius'])

# triname reiksmes

# del zmogus["miestas]

# print(zmogus['miestas'])

# iteruojame per visus zodyno elementus

# for key, value in zmogus.items():
#     print(key, ":", value)


# Tuple

# Tuple elementu reiksmes keisti negalima po to kai buvo sukurtos
# koordinates = (10,50)
# print(koordinates[1])
#
# koordinates1 = (54,42,12)
#
# sujungtos_koordinates = koordinates + koordinates1
# print(sujungtos_koordinates)



#------ 06.16
#  metodo perrasymas

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal make a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#
#     def make_sound(self):
#         print("The dog barks")
#
# dog = Dog("Bob", 5)
# dog.make_sound()
# print(f"My dog name is {dog.name}" + " and age is " + str(dog.age))


# paveldejimas
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#
#     def star_engine(self):
#         print("Engine started")
#
#     def stop_engine(self):
#         print("Engine stopped!")
#
# class Car(Vehicle):
#
#     def drive(self):
#         print("Car is driving!")
#
#
# car = Car("Toyota")
#
# car.start_engine()
# car.drive()
# car.stop_engine()

# ---------------------------------------------------------------------
#  sukurti zmogu, tevine klase, isvardinam savybes, jas aprasome
#
# class Zmogus:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # kuriam metodus, funkcijas rodyti informacija
#     def display_info(self):
#         print(f"Zmogaus vardas yra {self.name}")
#         print(f"Zmogaus amzius yra {self.age}")
#
# # sukuriam vaikine klase (inheritance). isvardiname kokiu savybiu norime, o tada kokias savybes paveldi is tevines (super)
# class Darbuotojas(Zmogus):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#     # ----super panaudoja tevines klases metoda, aprasom papildomas savybes
#     def display_info(self):
#         super().display_info()
#         print(f"Darbuotojo atlyginimas yra {self.salary}")
#
# zmogus = Zmogus("Antanukas", 12)                 sukuriam tevines klases objekta
# darbuotojas = Darbuotojas("Jonukas", 25, 2000)   sukuriam vaikines klases objekta
#
# zmogus.display_info()
# print()
# darbuotojas.display_info()


# ---sukurti pirkiniu krepselio funkcionaluma (turim produkta ir krepseli)
#
# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#
#     def display_info(self):
#         print(f"Produkto pavadinimas yra {self.title}")
#         print(f"Produkto kaina {self.price} $")
#
#
# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#     def calculate_discounted_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#     def display_info(self):
#         super().display_info()
#         print(f"Nuolaida {self.discount_percentage} %")
#         print(f"Galutine kaina {self.calculate_discounted_price()} $")
#
#
# class ShoppingCart(Product):
#     def __init__(self):
#         super().__init__(title=None, price=None)
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Produktas {product.title} i krepseli pridetas")
#
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f"Produktas {product.title} pasalintas is krepselio")
#         else:
#             print(f"Produktas {product.title} nerastas")
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:
#             total_price += product.price
#         return total_price
#
#
# prod3 = Product("Pienas", 2)
# prod1 = DiscountedProduct("Obuoliai", 3, 15)
# prod2 = Product("Sviestas", 3)
# shoppingcart = ShoppingCart()
# shoppingcart.add_product(prod3)
# shoppingcart.add_product(prod1)
# shoppingcart.add_product(prod2)
# print()
# for product in shoppingcart.products:
#     product.display_info()
#     print()
#
# total_price = shoppingcart.calculate_total_price()
# print(f"Bendra kaina {total_price} $")
# print()
#
# shoppingcart.remove_product(prod3)
#
# total_price = shoppingcart.calculate_total_price()
# print(f"Nauja bendra kaina {total_price} $")
# print()
#----------------------------------------------------------------

# --- Get-Set'ai------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Amzius negali buti neigiamas")
#
# person = Person("Jonas", -25)
#
# print("name", person.get_name())
# print("age", person.get_age())
#
# person.set_name("Petras")
# person.set_age(27)
#
# print("newname", person.get_name())
# print("newage", person.get_age())

