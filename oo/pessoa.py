class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, *filho, nome=None, idade=None): #atributo de objeto
        self.filhos = list(filho)
        self.nome = nome
        self.idade = idade


    def comprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42


    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def comprimentar(self):
        comprimetar_de_classe = super().comprimentar()
        return f'{comprimetar_de_classe}. Aperto de Mão!'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    tiago = Homem(nome='Tiago')
    luciano = Homem(renzo, tiago, nome='Luciano', idade=33)
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
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(issubclass(Homem, Pessoa))
    print(issubclass(Pessoa, Homem))
    print(renzo.olhos)
    print(renzo.comprimentar())
    print(luciano.comprimentar())
