import pygame
import sys
from jugador import Jugador
from moviments import Moviments
from pilota import Pilota

class Juego:
    def __init__(self):
        pygame.init()
        self.finestraJoc = pygame.display.set_mode((800, 600))
        self.rellotge = pygame.time.Clock()
        self.gameOver = False
        self.jugador1 = Jugador(250)
        self.jugador2 = Jugador(250)
        self.movimientos_jugador = Moviments(self.jugador1, self.jugador2)
        self.pilota = Pilota()

    def pinta_objectes(self):
        self.finestraJoc.fill((0, 255, 0))
        pygame.draw.rect(self.finestraJoc, (255, 0, 0), pygame.Rect(50, self.jugador1.posY, 20, 100))
        pygame.draw.rect(self.finestraJoc, (0, 0, 255), pygame.Rect(730, self.jugador2.posY, 20, 100))
        self.pilota.dibuixar(self.finestraJoc)

    def moviments(self):
        keys = pygame.key.get_pressed()
        self.movimientos_jugador.procesar_entradas(keys)
        self.pilota.moure()
        self.comprovar_colisions()

    def comprovar_colisions(self):

        # Comprova colisions amb les parets verticals
        if self.pilota.posX <= 0 or self.pilota.posX >= 800:
            self.pilota.rebotar_paret_vertical()

        # Comprova colisions amb les parets horitzontals
        if self.pilota.posY <= 0 or self.pilota.posY >= 600:
            self.pilota.rebotar_paret_horitzontal()

        # Comprova colisions amb els jugadors
        jugador1_rect = pygame.Rect(50, self.jugador1.posY, 20, 100)
        jugador2_rect = pygame.Rect(730, self.jugador2.posY, 20, 100)
        pilota_rect = pygame.Rect(self.pilota.posX - 10, self.pilota.posY - 10, 20, 20)
        if pilota_rect.colliderect(jugador1_rect) or pilota_rect.colliderect(jugador2_rect):
            self.pilota.rebotar_paret_vertical()

    def bucle_principal(self):
        while not self.gameOver:
            self.rellotge.tick(30)
            pygame.display.update()
            self.pinta_objectes()
            self.moviments()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego = Juego()
    juego.bucle_principal()
