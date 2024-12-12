# Exercice 7 - ici on va compter les voyelles dans n'importe qu'elle phrase

def compter_voyelles(phrase):
# On définis d'abord les voyelles
    voyelles = "aeiouAEIOU"
# On utilise la fonction sum simplifier le comptage
    compteur = sum(1 for lettre in phrase if lettre in voyelles)
    return compteur

phrase = input("Entrez une phrase : ")
nombre_voyelles = compter_voyelles(phrase)
print(f"Le nombre de voyelles est {nombre_voyelles}.")