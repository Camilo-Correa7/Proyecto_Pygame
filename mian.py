import pygame
import random

pygame.init()

width, height = 800, 600
escena = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evade al enemigo")
black = (0, 0, 0)
purpura = (128, 0, 128)
green = (0, 255, 0)


jugador_size = 50
jugador_pos = [width // 2, height - 2 * jugador_size]
jugador_speed = 25


enemigo_size = 50
enemigo_pos = [random.randint(0, width - enemigo_size), 0]
enemigo_speed = 5


clock = pygame.time.Clock()
puntaje = 0
game_over = False

#Funciones juego
def dibujar_jugador(position):
    pygame.draw.rect(escena, green, (position[0], position[1], jugador_size, jugador_size))


def dibujar_enemigo(position):
    pygame.draw.rect(escena, purpura, (position[0], position[1], enemigo_size, enemigo_size))


def det_colision(jugador_pos, enemigo_pos):
    px, py = jugador_pos
    ex, ey = enemigo_pos
    if (ex < px < ex + enemigo_size or ex < px + jugador_size < ex + enemigo_size) and \
       (ey < py < ey + enemigo_size or ey < py + jugador_size < ey + enemigo_size):
        return True
    return False

#Bucle
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            x, y = jugador_pos
            if event.key == pygame.K_LEFT and x > 0:
                jugador_pos[0] -= jugador_speed
            if event.key == pygame.K_RIGHT and x < width - jugador_size:
                jugador_pos[0] += jugador_speed
    #Fondo
    escena.fill(black)
    dibujar_jugador(jugador_pos)
    dibujar_enemigo(enemigo_pos)

    
    enemigo_pos[1] += enemigo_speed
    if enemigo_pos[1] >= height:
        enemigo_pos = [random.randint(0, width - enemigo_size), 0]
        puntaje += 1
        enemigo_speed += 1 

   
    if det_colision(jugador_pos, enemigo_pos):
        game_over = True

    
    pygame.display.update()
    clock.tick(30)

# Finaliza Pygame
pygame.quit()
print(f"Tu puntaje final es: {puntaje}")
