class Jugador:
    def __init__(self, pos_inicial):
        self.posY = pos_inicial
        self.velocidad = 10

    def mover_arriba(self):
        self.posY -= self.velocidad
        self.posY = max(self.posY, 0)

    def mover_abajo(self):
        self.posY += self.velocidad
        self.posY = min(self.posY, 500)
