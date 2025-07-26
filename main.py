import pygame
import constants as c
from player import Player

def main():
    pygame.init()
    # set screen
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    # FPS things
    clock = pygame.time.Clock()
    dt = 0
    # Player
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    # game loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
