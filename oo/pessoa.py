class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, *filho, nome=None, idade=None): #atributo de objeto
        self.filhos = list(filho)
        self.nome = nome
        self.idade = idade


    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42


    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(renzo.__dict__)
    print(luciano.__dict__)
    del luciano.sobrenome
    luciano.olhos = 1
    print(renzo.__dict__)
    print(luciano.__dict__)
    Pessoa.olhos = 3
    #del luciano.olhos
    print(renzo.__dict__)
    print(luciano.__dict__)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos))
    del luciano.olhos
    print(luciano.olhos)
    print(id(luciano.olhos))
    print(Pessoa.__dict__.keys())
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
