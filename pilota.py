import pygame
import random

class Pilota:
    def __init__(self):
        self.posX = 400
        self.posY = 300
        self.velocitatX = random.choice([-10, 10])
        self.velocitatY = random.choice([-10, 10])
        self.diametre = 15

    def moure(self):
        self.posX += self.velocitatX
        self.posY += self.velocitatY

    def rebotar_paret_vertical(self):
        self.velocitatX *= -1

    def rebotar_paret_horitzontal(self):
        self.velocitatY *= -1

    def resetejar_posicio(self):
        self.posX = 400
        self.posY = 300
        self.velocitatX = random.choice([-5, 5])
        self.velocitatY = random.choice([-5, 5])

    def dibuixar(self, finestraJoc):
        pygame.draw.circle(finestraJoc, (255, 255, 255), (self.posX, self.posY), self.diametre)
