
"""
Objectif
Methode
Besoin
Connue
Entrees
Sorties
Resultat
Hypothese
"""
def saisie():
    prix_unitaire=int(input("saisir le Prix unitaire: "))
    quantite=int(input("saisir la Quantite: "))
    return prix_unitaire, quantite

"""
Objectif cette dontion permettant de calculer le prix unitaire et le quantite
Methode appel la fonction saisir ensuite usage d'une boucle For
Besoin: pu,qnt,pris_des_produits,nba
Connue nba
Entrees -
Sorties prix_des_produits
Resultat: _
Hypothese: PU>0  & qnt>0 & nbA appartient [0,10]
"""
def calcul_des_produits(nbA=10):
    prix_des_produits=0
    for i in range(nbA):
        print(f"donner l'article numero {i+1}")
        prix,quantite=saisie()
        prix_des_produits+=prix*quantite

    return prix_des_produits

"""
Objectif: permet de calculer la remise
Methode: utilisaton d'une expresson arithmetique associé à une structure alternative
Besoin: prix des produits, taux_remise, taux_remise2
Connue: taux_remise, taux_remise2
Entrees: pris_des_produits
Sorties: remise
Resultat: -
Hypothese: prix_produit>0
"""
def remise(prix_des_produits, taux_remise=0.025,taux_remise2=0.1):
    remise=0
    if (prix_des_produits >= 7000 and prix_des_produits <= 250000):
        remise=prix_des_produits * taux_remise
    else:
        if (prix_des_produits > 250000):
            remise=prix_des_produits * taux_remise2

    return remise

"""
Objectif
Methode
Besoin
Connue
Entrees
Sorties
Resultat
Hypothese
"""
def port(prix_des_produits, taux_de_port=0.02):
    port=0
    if(prix_des_produits >= 50000):
        port= prix_des_produits * taux_de_port
    return port

"""
Objectif 
Methode utilisation d'une expression arithmetique
Besoin: prix des produits, remise, port
Connue
Entrees
Sorties
Resultat
Hypothese
"""
def calcul_prix_total(prix_des_produits,port,remise):
    prix_total=0
    return prix_total + port - remise

"""
Objectif: calcul TVA
Methode: utilisation d'une expression arithmetique
Besoin: prix total et tva
Connue: tva
Entrees : prix total
Sorties : prix_tva
Resultat _
Hypothese prix_total>0
"""
def calcul_tva(prix_total,tva=0.18):
    return prix_total * tva

"""
Objectif calculer le prix à payer
Methode utilisation d'une expression arithmetique
Besoin prix total et prix tva
Connue
Entrees prix total et prix tva
Sorties : prix à payer
Resultat _
Hypothese
"""
def prix_a_payer(prix_total,prix_tva):
    return prix_total + prix_tva

""" programme principale"""
def programme_principal():
    prix_des_produits = calcul_des_produits()
    r = remise(prix_des_produits)
    p = port(prix_des_produits)
    prix_total = calcul_prix_total(prix_des_produits,p,r)
    tva = calcul_tva(prix_total)
    pap = prix_a_payer(prix_total,tva)
    print(f"Le prix à payer est de {pap}")

if __name__ == '__main__':
    programme_principal()