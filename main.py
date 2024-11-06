import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
import time, sys

def main():
    pygame.init()
    pygame.display.set_caption("Asteroid")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    font = pygame.font.SysFont("Arial", 30)
    player = Player(x, y)
    AsteroidField()

    while True:
        screen.fill(000000)
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
             if asteroid.check_collision(player):
                pygame.display.flip()
                screen.fill(000000)
                print("Game Over!")
                text = font.render("GAME OVER", True, "red")
                text_rect = text.get_rect()
                text_rect.center = (x, y)
                screen.blit(text, text_rect)
                pygame.display.flip()
                time.sleep(1)
                sys.exit()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()