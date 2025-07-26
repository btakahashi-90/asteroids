import pygame
import sys
import constants as c
from player import Player, Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    # set screen
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    # Groups setup
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # FPS things
    clock = pygame.time.Clock()
    dt = 0
    # Player
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    # Asteroid Field
    field = AsteroidField()
    # game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(0)
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
