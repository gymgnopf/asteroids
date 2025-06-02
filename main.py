import pygame
from constants import *
import player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)

    clock = pygame.time.Clock()
    dt = 0

    pl = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (22, 0, 0))

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(pl):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()  
