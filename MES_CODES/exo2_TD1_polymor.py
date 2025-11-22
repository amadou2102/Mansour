class Marchandise:
    def __init__(self,nom,poids):
        self.nom = nom
        self.__poids = poids

    def getPoids(self):
        return self.__poids

class Cargo:
    def __init__(self,distance,limit):
        self.distance = distance
        self.limit = limit
        self.marchandises=[]

    def poidsTotal(self):
        sp=0
        for m in self.marchandises:
            sp+=m.getPoids()

        return sp

    def ajouter(self,marchandise):
        if self.poidsTotal() + marchandise.getPoids()>self.limit:
            self.marchandises.append(Marchandise())
        else:
            print("la limit est atteinte")

    def getCout(self):
        return self.distance*self.poidsTotal()

class Maritime(Cargo):
    def __init__(self,distance):
        super().__init__(distance,30000)

    def getCout(self):
        return 10 * self.distance * self.poidsTotal()

class Routiere(Cargo):
    def __init__(self,distance):
        super().__init__(distance,38000)

    def getCout(self):
        return 4 * self.distance * self.poidsTotal()

class Aerienne(Cargo):
    def __init__(self,distance):
        super().__init__(distance,80000)
    def getCout(self):
        return self.distance * self.poidsTotal()

if __name__ == "__main__":
    marchandise1=Marchandise("ordi",1500)
    maritime1=Maritime(1200)
    maritime1.ajouter(marchandise1)