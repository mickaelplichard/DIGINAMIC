x = 42
print(id(x))


a: int = 66
b = a
print(id(a), id(b), sep="\n")


message1, message2 = "Première chaînes de caractères", "Deuxième chaînes de caractères"
message2, message1 = message1, message2
print(message1, message2, sep="\n")
