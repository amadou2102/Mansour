def taille():
    n=int(input("donne la taille du tableau: "))
    return n

def rempissage(T,n):

    for i in range(n):
        valeur = int(input(f"Entrez la valeur numéro {i + 1} : "))
        T.append(valeur)  # on ajoute la valeur à la liste
    return T

if __name__=="__main__":
    T=[]
    t=taille()
    r=rempissage(T,t)
