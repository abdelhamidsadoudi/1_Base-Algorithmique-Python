# Exercice 9 - vérifier si un mot est un palindrome
mot = input("Entrez un mot : ")

# On va écrire qui permet de comparer le mot à sa version inversée
if mot == mot[::-1]:
    print(f"{mot} est un palindrome.")
else:
    print(f"{mot} n'est pas un palindrome.")
