import sys

import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
import player
from player import Player
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot



def main():
    # initialize pygame and create a window
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # create sprite groups and add the player to them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # while loop for the game
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in asteroids:
            if sprite.collides_with(my_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids.copy():
            for shot in shots.copy():
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


        















#KEEP AT BOTTOM OF FILE
if __name__ == "__main__":
    main()
