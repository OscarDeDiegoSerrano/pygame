import pygame


class Moviments:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def procesar_entradas(self, keys):
        if keys[pygame.K_w]:
            self.jugador1.mover_arriba()
        if keys[pygame.K_s]:
            self.jugador1.mover_abajo()
        if keys[pygame.K_UP]:
            self.jugador2.mover_arriba()
        if keys[pygame.K_DOWN]:
            self.jugador2.mover_abajo()
