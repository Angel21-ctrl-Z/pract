import sys
import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file

from constants import*
#this area the values for the game.

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from gun import Gun

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#setting up clock for FPS management
    clock = pygame.time.Clock()

#group set
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Gun.containers = (updatable, drawable, shots)
    
    
#player spawn

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
#asteriods spawn
    
    asteroid_field = AsteroidField()

    dt = 0
    
#display(game loop)
    score = 0
    font = pygame.font.SysFont(None, 48)

    while True:
        #quit input check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Start menu
        if not hasattr(main, "started"):
            title = font.render("Asteroids", True, (255, 255, 255))
            prompt = pygame.font.SysFont(None, 32).render("Press space to start", True, (200, 200, 200))
            screen.fill("black")
            screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, SCREEN_HEIGHT // 3))
            screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        waiting = False
                clock.tick(60)
            main.started = True
            score = 0  # Reset score when starting

        #movement
        for obj in updatable:
            obj.update(dt)
        #collision
        for asteriod in asteroids:
            if asteriod.collision(player):
                print("Game Over")
                del main.started
                end_game = font.render("Game Over!", True, (255, 0, 0))
                screen.blit(end_game, ((SCREEN_WIDTH - end_game.get_width()) // 2, SCREEN_HEIGHT // 3))
                score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, (255, 255, 255))
                screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                # Reset game state
                player.kill()
                for a in asteroids:
                    a.kill()
                for s in shots:
                    s.kill()
                asteroid_field = AsteroidField()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                break

            for shot in shots:
                if asteriod.collision(shot):
                    asteriod.split()
                    shot.kill()
                    score += 10  # Increase score for each asteroid hit

        #create black screen
        screen.fill("black")
        #spawn
        for obj in drawable:
            obj.draw(screen)
        # Draw score
        score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        #update screen
        pygame.display.flip()
        #adjusting frames for better run
        dt = clock.tick(60) / 1000
        
        

#test runs
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()