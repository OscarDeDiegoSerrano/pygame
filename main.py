import sys
import pygame

pygame.init()

finestraJoc = pygame.display.set_mode((800, 600))  # Canviem les dimensions de la finestra
rellotge = pygame.time.Clock()

gameOver = False

# Definim els atributs per a cada jugador
jugador1_posY = 250
jugador2_posY = 250
jugador_velocitat = 5

def PintaObjectes():
    finestraJoc.fill((0, 255, 0))

    # Pintem els jugadors
    jugador1 = pygame.Rect(50, jugador1_posY, 20, 100)  # (posX, posY, ample, alçada)
    jugador2 = pygame.Rect(730, jugador2_posY, 20, 100)  # (posX, posY, ample, alçada) - Canviem la posició per ajustar-la a la finestra més gran
    pygame.draw.rect(finestraJoc, (255, 0, 0), jugador1)  # Color vermell per al jugador 1
    pygame.draw.rect(finestraJoc, (0, 0, 255), jugador2)  # Color blau per al jugador 2

def Moviments():

    global jugador1_posY, jugador2_posY
    keys = pygame.key.get_pressed()

    # Moviment jugador 1
    if keys[pygame.K_w]:  # Tecle "W"
        jugador1_posY -= jugador_velocitat
        jugador1_posY = max(jugador1_posY, 0)  # Limitar moviment cap amunt

    if keys[pygame.K_s]:  # Tecle "S"
        jugador1_posY += jugador_velocitat
        jugador1_posY = min(jugador1_posY, 500)  # Limitar moviment cap avall

    # Moviment jugador 2
    if keys[pygame.K_UP]:  # Fletxa cap amunt
        jugador2_posY -= jugador_velocitat
        jugador2_posY = max(jugador2_posY, 0)  # Limitar moviment cap amunt
    if keys[pygame.K_DOWN]:  # Fletxa cap avall
        jugador2_posY += jugador_velocitat
        jugador2_posY = min(jugador2_posY, 500)  # Limitar moviment cap avall

while not gameOver:
    rellotge.tick(30)
    pygame.display.update()
    PintaObjectes()
    Moviments()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

pygame.quit()
sys.exit()
