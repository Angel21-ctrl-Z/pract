import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file

from constants import*
#this area the values for the game.

from player import*


def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#setting up clock for FPS management
    clock = pygame.time.Clock()
   
#player spawn
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    


#display(game loop)
    while True:
        #quit input check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #player movement
        player.update(dt)
        #create black screen
        screen.fill("black")
        #spawn
        player.draw(screen)
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