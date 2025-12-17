list = ["Bernard", "Gérard", "Gontran", "Jacqueline", "Intrus", "Nadia", "Jack"]
for item in list:
    if item == "Intrus":
        print ("Intrus trouvé!")
        break


liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]
sum = 0
for value in liste_somme:
    sum += value
print(sum)


factoriel = 1
for i in range (1,11):
    factoriel *= i
print(factoriel)


response = ""
while response != "oui":
    response = input("Tapez oui ou non: ").lower()
    if response != "oui" and response != "non":
        print("Message invalide")


ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]

for index, value in enumerate(ma_liste):
    print(f"L'élement à l'index {index} est {value}")


main_list = [23, 1, 27, 28, 3, 4, 763, 12, 90]
new_list = []
for nb in main_list:
    if nb % 5 == 0:
        nb = nb * 2
        new_list.append(nb)
    else:
        nb = nb // 3
        new_list.append(nb)
print(new_list)


palindrome = ["kayak", "coloc", "malayalam", "pop", "erre"]
resultat = all([mot == mot[::-1] for mot in palindrome])
print(resultat)


liste = [1, 3, 7, [4, 6, [5, 2]]]

flat = [
    item
    for sub in liste
    for item in (sub if not isinstance(sub, list) else 
                 [i for j in sub for i in (j if not isinstance(j, list) else j)])
]
flat = sorted(flat)
print(flat) 

