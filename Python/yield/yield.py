def generate_numbers():
    yield 1
    yield 2
    yield 3

gen = generate_numbers()

# Utilisation avec une boucle for
for number in gen:
    print(number)  # Affiche 1, puis 2, puis 3

# Utilisation avec next()
gen = generate_numbers()
print(next(gen))  # Affiche 1
print(next(gen))  # Affiche 2
print(next(gen))  # Affiche 3
# print(next(gen))  # Provoque une erreur StopIteration car il n'y a plus de valeurs à générer