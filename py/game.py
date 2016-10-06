import pygame

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
green = (0, 255, 255)
fps = 60
window_width = 800
window_height = 600

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 25)

def main():

    #setting up pygame, window
    pygame.init()
    gameDisplay = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("RPG-Game")

    #Gameloop variables
    gameContinue = True
    keys = dict()
    
    x = 300
    y = 300
    deltaX = 0
    deltaY = 0
    width = 10
    height = 10
    speed = 250
    jumps = 1
    jumping = False

    #Game Loop
    while gameContinue:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameContinue = False
            elif event.type == pygame.KEYDOWN:
                keys[event.key] = True
            elif event.type == pygame.KEYUP:
                keys[event.key] = False

        if pygame.K_UP in keys and keys[pygame.K_UP]:
            if jumps > 0 and not jumping:
                jumping = True
                jumps -= 1
                deltaY = -50
        elif pygame.K_UP in keys and not keys[pygame.K_UP]:
            jumping = False
        if pygame.K_DOWN in keys and keys[pygame.K_DOWN]:
            #y += (speed) / fps
            pass
        if pygame.K_LEFT in keys and keys[pygame.K_LEFT]:
            deltaX = -speed / fps
            #x -= (speed) / fps
        elif pygame.K_RIGHT in keys and keys[pygame.K_RIGHT]:
            deltaX = speed / fps
            #x += (speed) / fps
        else:
            deltaX = 0
        
        deltaY += 5

        x += deltaX
        y += deltaY

        x = max(0, min(x, window_width - width))
        y = max(0, min(y, window_height - 50 - height))

        gameDisplay.fill(white)
        gameDisplay.fill(black, [0, 550, 800, 25])
        gameDisplay.fill(blue, [x, y, width, height])
        if y >= (window_height - 50 - height):
            jumps = 2
            messageToScreen(gameDisplay, "Jumps reset", red)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

def messageToScreen(gameDisplay, msg, color):
    message = font.render(msg, True, color)
    gameDisplay.blit(message, [window_width / 2, window_height / 2])

main()
