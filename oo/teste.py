class Corpo:

    def __init__(self, olhos = None, boca = None, nariz = None, orelhas = None):
        self.olhos = olhos
        self.boca = boca
        self.nariz = nariz
        self.orelhas = orelhas

if __name__ == '__main__':
    corpo = Corpo(olhos = 2, boca = 1, nariz = 1, orelhas = 2)
    print(corpo.olhos)
    print(corpo.boca)
    print(corpo.nariz)
    print(corpo.orelhas)