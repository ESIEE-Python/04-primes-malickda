"""
ce module test si un nombre est ptrmier ou pas
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    "la fonction vérifie si un nombre est premier"
    if p<=1:
        return False
    for i in range(2,int(sqrt(p))+1):
        if p%i==0:
            return False
    return True
#### Fonction principale


def main():
    """
    ce module teste la fonction sécondaire
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
