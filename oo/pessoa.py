class Pessoa:
    def __init__(self, *filho, nome=None, idade=None):
        self.filhos = list(filho)
        self.nome = nome
        self.idade = idade


    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    tiago = Pessoa(nome='Tiago')
    luciano = Pessoa(renzo, tiago, nome='Luciano', idade=33)
    print(Pessoa.comprimentar(luciano))
    print(id(luciano))
    print(luciano.comprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for f in luciano.filhos:
        print(f.nome)
    luciano.sobrenome = 'Ramalho'
    print(luciano.nome, *luciano.__dict__.keys(), sep=', ')
    print(renzo.nome, *renzo.__dict__.keys(), sep=', ')
    del luciano.sobrenome
    print(luciano.nome, *luciano.__dict__.keys(), sep=', ')
    print(renzo.nome, *renzo.__dict__.keys(), sep=', ')
