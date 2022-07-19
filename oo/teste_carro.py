from unittest import TestCase
from oo.carros import Motor, Direcao

motor = Motor()
direcao = Direcao()


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        self.assertEqual(0, motor.velocidade)

    def test_acelerar_motor(self):
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.velocidade = 200
        motor.acelerar()
        self.assertEqual(200, motor.velocidade)

    def test_frear_motor(self):
        motor.velocidade = 3
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def test_direcao_inicial(self):
        self.assertEqual('Norte', direcao.direcao)

    def test_girar_direita(self):
        direcao.girar_direita()
        self.assertEqual('Leste', direcao.direcao)

    def test_girar_esquerda(self):
        direcao.direcao = 'Norte'
        direcao.girar_esquerda()
        self.assertEqual('Oeste', direcao.direcao)
