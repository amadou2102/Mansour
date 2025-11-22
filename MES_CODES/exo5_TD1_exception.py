class ValeurInvalideException(Exception):
    pass
class SoldeInsufficientException(Exception):
    pass
class CompteBloqueException(Exception):
    pass
class CompteBancaire:
    def __init__(self, num, nom, solde, bloque = False):
        self.num = num
        self.nom = nom
        self.solde = solde
        self.bloque = bloque

    def Retrait(self,montant):
        if montant <= 0:
            raise ValeurInvalideException("Montant non valide")
        elif self.solde <= montant:
            raise SoldeInsufficientException("Solde insuffisant")
        elif self.bloque == True :
            raise CompteBloqueException("Compte bloque")

        else:
            self.solde -= montant

if __name__ == "__main__":
    C1 = CompteBancaire(2,"amadou",5000)
    try:
        C1.Retrait(1000)
    except Exception as e  :
        print("Erreur:", e)

