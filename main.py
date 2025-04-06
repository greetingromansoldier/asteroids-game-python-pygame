import pygame
import sys
from constants import *
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import *

def main ():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroidfield = AsteroidField()

    # the "game loop"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            collision_status = player.check_collision(obj)
            if collision_status == True:
                print("Game over!")
                sys.exit()



        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
