# Exercice 6 - trouver le plus grand nombre parmi les 3 nombres qu'on va insérer
nombres = []
for i in range(3):
    nombre = float(input(f"Entrez le {i + 1}e nombre : "))
    nombres.append(nombre)

plus_grand = max(nombres)
print(f"Le plus grand nombre est {plus_grand}.")
