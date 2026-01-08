import sys
from asteroid import Asteroid
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,LINE_WIDTH
from logger import log_state,log_event
import pygame
from asteroidfield import AsteroidField

from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteriod in asteroids:
            if asteriod.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        player.update(dt)
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        player.draw(screen)
        
        for draw in drawable:
            draw.draw(screen)
        # drawable.draw(screen)
        # print(f"dt: {dt}")bootdev run 658641f2-586b-48eb-bfb0-e7612cdd5dfd


if __name__ == "__main__":
    main()
