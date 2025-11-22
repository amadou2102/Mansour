from numbers import Complex


class Complexe:
    def __init__(self, reel,imaginaire):
        self.reel = reel
        self.imaginaire = imaginaire

    def __add__(self, other):
        sum_reel = self.reel + other.reel
        sum_imaginaire = self.imaginaire + other.imaginaire
        return Complexe(sum_reel, sum_imaginaire)

    def __mul__(self, other):
        p_reel = (self.reel * other.reel) - (self.imaginaire * other.imaginaire)
        p_imaginaire = (self.reel * other.imaginaire) + (self.imaginaire * other.reel)
        return Complexe(p_reel, p_imaginaire)

    def conjugue(self):
        return Complexe(self.reel, self.imaginaire)

    def __abs__(self):
        return (self.reel**2 + self.imaginaire**2) ** 0.5

    def __truediv__(self, other):
        denom = (other.reel**2) + (other.imaginaire**2)
        d_reel = (self.reel * other.reel) + (self.imaginaire * other.imaginaire) / denom
        d_imag = (other.reel * self.imaginaire) - (self.reel * other.imaginaire) / denom
        return Complexe(d_reel, d_imag)

    def __str__(self):
        return f"{self.reel} {self.imaginaire}"
if __name__ == "__main__":
    C1 = Complexe(2, -3)
    C2 = Complexe(3,9)
    C3 = C1 + C2
    C4 = C1 * C2
    C5 = C2 * C3
    print(C1)
    print(C2)
    print(C3)
    print(C4)
    print(C5)
