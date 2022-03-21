import pygame
from settings import *
from player import Player
from map import *
from map import world_map
from ray_casting import ray_casting


import math

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.movement()
        sc.fill(BLACK)

        ray_casting(sc, player.pos, player.angle)



        # pygame.draw.circle(sc, GREEN, player.pos, 12)
        # pygame.draw.line(sc, RED, (int(player.x), int(player.y)), (player.x + WIDTH * math.cos(player.angle),
        #                                        player.y + WIDTH * math.sin(player.angle)))



        # for x, y in world_map:
        #     pygame.draw.rect(sc, DARKGREY, (x, y, TILE, TILE), 2)


        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
