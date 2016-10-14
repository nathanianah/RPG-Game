import pygame
from character import *
from h import *


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

    #Setting sprite lists
    char = Character()
    bullets = []

    #Making sprite groups
    bulletList = pygame.sprite.Group()
    spriteList = pygame.sprite.Group()
    spriteList.add(char)
    
    (deltaX, deltaY) = (0, 0)
    jumps = max_jumps
    jumping = False

    #Game Loop
    while gameContinue:
        for event in pygame.event.get():
            #Setting Key Map
            if event.type == pygame.QUIT:
                gameContinue = False
            elif event.type == pygame.KEYDOWN:
                keys[event.key] = True
            elif event.type == pygame.KEYUP:
                keys[event.key] = False

        #Interpreting Keypresses
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
        if pygame.K_SPACE in keys and keys[pygame.K_SPACE]:
            (rectX, rectY) = char.rect.center
            bullet = Bullet(rectX, rectY, 1)
            bullets += [bullet]
            bulletList.add(bullet)

        #Update character movement
        deltaY += 5

        char.rect.x += deltaX
        char.rect.y += deltaY

        char.rect.x = max(0, min(char.rect.x, window_width - char.rect.width))
        char.rect.y = max(0, min(char.rect.y, window_height - 50 - char.rect.height))

        #Update bullet movement
        for bullet in bullets:
            bullet.rect.x += 5 if bullet.direction > 0 else -5

        #Render
        gameDisplay.fill(white)
        gameDisplay.fill(black, [0, 550, 800, 25])
        if char.rect.y >= (window_height - 50 - char.rect.height):
            jumps = max_jumps
            messageToScreen(gameDisplay, "Jumps reset", red)
        spriteList.draw(gameDisplay)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

def messageToScreen(gameDisplay, msg, color):
    message = font.render(msg, True, color)
    gameDisplay.blit(message, [window_width / 2, window_height / 2])

main()
