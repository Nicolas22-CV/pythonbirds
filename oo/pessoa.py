class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    

if __name__ == '__main__':
    nicolas = Pessoa(nome = 'Nicolas')
    alex = Pessoa(nicolas, nome = 'Alex')
    print(Pessoa.cumprimentar(alex))
    print(id(alex))
    print(alex.cumprimentar())
    print(alex.nome)
    print(alex.idade)
    for filhos in alex.filhos:
        print(filhos.nome)