import pygame
import sys

# Inizializza pygame
pygame.init()

# Dimensioni finestra
larghezza, altezza = 600, 400
schermo = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Mini Gioco")

# Colori
ROSSO = (255, 0, 0)
NERO = (0, 0, 0)

# Player
player = pygame.Rect(50, 50, 40, 40)
velocita = 5

# Loop principale
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Input da tastiera
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_LEFT]:
        player.x -= velocita
    if tasti[pygame.K_RIGHT]:
        player.x += velocita
    if tasti[pygame.K_UP]:
        player.y -= velocita
    if tasti[pygame.K_DOWN]:
        player.y += velocita

    # Disegna schermo
    schermo.fill(NERO)
    pygame.draw.rect(schermo, ROSSO, player)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
