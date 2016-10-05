import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magneta = (255, 0, 255)
green = (0, 255, 255)

def main():
    #define colors


    pygame.init()
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("RPG-Game")

    #Game Loop
    gameContinue = True
    while gameContinue:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameContinue = False

        gameDisplay.fill(white)
        pygame.display.update()

    pygame.quit()
    quit()

main()
