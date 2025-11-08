def valeurs():
    n = int(input("donne le nombre 1: "))
    m = int(input("donne le nombre 2: "))
    return n, m

def somme(n,m):
    somme = 0
    somme=n+m
    return somme

if __name__=="__main__":
    nombre=valeurs()
    s=somme(nombre[0],nombre[1])
    print(s)