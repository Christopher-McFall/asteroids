import pygame
from pygame import display
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from turtle import Screen




def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        display.flip()    















#KEEP AT BOTTOM OF FILE
if __name__ == "__main__":
    main()
