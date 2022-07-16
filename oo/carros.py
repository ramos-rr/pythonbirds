"""
Criar classe Carro com 2 atributos compostos por outras duas classes: MOTOR E DIREÇÃO

1. MOTOR -> Controlar a velocidade, com atributo de dado:
a. Velocidade
b. Acelerar (aumento de uma unidade)
c. Frear (diminuição de 2 unidades)

2. Direção -> Controlar a direção, com os seguintes atributos:
a. Valor de direção (valores possíveis: NORTE, SUL, LESTE, OESTE
b. Girar a direita (Sentido horário)
c. Girar a esquerda (Sentido antihorário)
  N
O   L
  S
    Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Testando direção
    >>> direcao = Direcao()
    >>> direcao.direcao
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.direcao
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.direcao
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.direcao
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.direcao
    'Norte'
    >>> direcao.girar_esquerda()
    >>> direcao.direcao
    'Oeste'
    >>> direcao.girar_esquerda()
    >>> direcao.direcao
    'Sul'
    >>> direcao.girar_esquerda()
    >>> direcao.direcao
    'Leste'
    >>> direcao.girar_esquerda()
    >>> direcao.direcao
    'Norte'

    # Do carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""


class Motor:
    def __init__(self, veloc=0):
        self.velocidade = veloc

    def acelerar(self):
        self.velocidade += 1
        self.velocidade = min(200, self.velocidade)

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


orientacao = ['Norte', 'Nordeste', 'Leste', 'Sudeste', 'Sul', 'Sudoeste', 'Oeste', 'Noroeste']


class Direcao:
    def __init__(self, dir=orientacao[0]):
        self.direcao = dir.capitalize()

    def girar_direita(self):
        pos = orientacao.index(self.direcao)
        if pos == 3:
            self.direcao = orientacao[0]
        else:
            self.direcao = orientacao[pos+1]

    def girar_esquerda(self):
        pos = orientacao.index(self.direcao)
        if pos == 0:
            self.direcao = orientacao[-1]
        else:
            self.direcao = orientacao[pos-1]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.direcao

    def girar_direita(self):
        return self.direcao.girar_direita()

    def girar_esquerda(self):
        return self.direcao.girar_esquerda()
