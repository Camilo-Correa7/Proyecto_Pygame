import pygame
import random
WIDTH = 0
HEIGHT = 0
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Evade al enemigo")

#Color
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10