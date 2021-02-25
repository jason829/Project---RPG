import pygame  
import sys
import time
import random
import math
mainClock = pygame.time.Clock() 
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Game')
screen = pygame.display.set_mode((1280, 720),0,32)
font = pygame.font.SysFont(None, 60)

backgroundImage = pygame.image.load('background.png')
backgroundImage2 = pygame.image.load('Grass_Sample.png')

playerModel = pygame.image.load('player.png')
playerModelLeft = pygame.image.load('player_left.png')
playerModelRight = pygame.image.load('player_right.png')
playerModelDown = pygame.image.load('player_down.png')
playerAttack = pygame.image.load('player_attack.png')
playerAttack2 = pygame.image.load('player_attack_left.png')
playerAttack3 = pygame.image.load('player_attack_Right.png')
playerAttack4 = pygame.image.load('player_attack_down.png')
enemyModelUp = pygame.image.load('enemy.png')
enemyModelRight = pygame.image.load('enemy_right.png')
enemyModelDown = pygame.image.load('enemy_down.png')
enemyModelLeft = pygame.image.load('enemy_left.png')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 5, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 



def main_menu():
    click = False
    while True:
        screen.blit(pygame.transform.scale(backgroundImage, (1280, 720)),(0,0))
        draw_text('My Game', font, (255, 255, 255), screen, 25, 25)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(140, 100, 225, 50)
        button_2 = pygame.Rect(140, 200, 225, 50)
        button_3 = pygame.Rect(140, 300, 225, 50)
        button_4 = pygame.Rect(140, 400, 225, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                newGame()
        if button_2.collidepoint((mx, my)):
            if click:
                loadGame()
        if button_3.collidepoint((mx, my)):
            if click:
                options()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        pygame.draw.rect(screen, (0, 0, 0), button_4)
        draw_text('New Game', font, (255,255,255), screen, 145, 105)
        draw_text('Load Game', font, (255,255,255), screen, 145, 205)
        draw_text('Options', font, (255,255,255), screen, 145, 305)
        draw_text('Quit', font, (255,255,255), screen, 145, 405)

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def newGame():
    running = True
    click = False
    while running:
        screen.fill((0,0,0))
        section = pygame.Rect(100, 100, 500, 600)
        pygame.draw.rect(screen, (169,169,169), section)
        screen.blit(pygame.transform.scale(backgroundImage, (1280, 720)),(0,0))
        section = pygame.Rect(100, 100, 1100, 500)
        pygame.draw.rect(screen, (169,169,169), section)
        mx, my = pygame.mouse.get_pos()
        draw_text('Game', font, (255, 255, 255), screen, 10, 10)

        
        button_1 = pygame.Rect(25, 650, 125, 50)
        button_2 = pygame.Rect(100, 150, 225, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                running = False
        if button_2.collidepoint((mx, my)):
            if click:
                playable()
                break
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        draw_text('Back', font, (255,255,255), screen, 30, 655)
        draw_text('File 1', font, (255,255,255), screen, 105, 105)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        pygame.display.update()
        mainClock.tick(60)
 
def loadGame():
    running = True
    click = False
    while running:
        screen.fill((0,0,0))
        screen.blit(pygame.transform.scale(backgroundImage, (1280, 720)),(0,0))
        section = pygame.Rect(100, 100, 1100, 500)
        pygame.draw.rect(screen, (169,169,169), section)
        draw_text('Pick Save File', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(25, 650, 125, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                running = False
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        draw_text('Back', font, (255,255,255), screen, 30, 655)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    click = False
    while running:
        screen.fill((0,0,0))
        screen.blit(pygame.transform.scale(backgroundImage, (1280, 720)),(0,0)) 
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(25, 650, 125, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                running = False
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        draw_text('Back', font, (255,255,255), screen, 30, 655)
        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 
        
        pygame.display.update()
        mainClock.tick(60)

def playable():
    running = True
    click = False
    while running:
        area = pygame.display.set_mode((1280, 720))
        moving(area)
        
   
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
                   
def moving(area):
    click = False
    man = player(500, 500, 100, 100)
    zombie = enemy(300, 500, 64, 64, 1100, 600)
    running = True
    while running:
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        pygame.time.delay(50)
        keys = pygame.key.get_pressed()
        man.hitbox = (man.x + 11, man.y + 10, 70, 70)
        pygame.draw.rect(area, (255,0,0), man.hitbox,2)
        zombie.hitbox = (zombie.x + 11, zombie.y + 10, 70, 70)
        pygame.draw.rect(area, (255,0,0), zombie.hitbox,2)

        

        if zombie.velX > 0:
            if zombie.x < zombie.path[1] + zombie.velX:
                zombie.x += zombie.velX
                screen.blit(pygame.transform.scale(enemyModelRight, (75, 75)),(zombie.x,zombie.y))
            else: 
                zombie.velX = zombie.velX * -1
                zombie.x += zombie.velX
                screen.blit(pygame.transform.scale(enemyModelLeft, (75, 75)),(zombie.x,zombie.y))

        else: 
            if zombie.x > zombie.path[0] - zombie.velX:
                zombie.x += zombie.velX
                screen.blit(pygame.transform.scale(enemyModelLeft, (75, 75)),(zombie.x,zombie.y))
            else:
                zombie.velX = zombie.velX * -1
                zombie.x += zombie.velX
                screen.blit(pygame.transform.scale(enemyModelRight, (75, 75)),(zombie.x,zombie.y))

        if zombie.velY > 0:
            if zombie.y < zombie.path2[1] + zombie.velY:
                zombie.y += zombie.velY
                screen.blit(pygame.transform.scale(enemyModelUp, (75, 75)),(zombie.x,zombie.y))
            else:
                zombie.velY = zombie.velY * -1
                zombie.y += zombie.velY
                screen.blit(pygame.transform.scale(enemyModelDown, (75, 75)),(zombie.x,zombie.y))
        else:
            if zombie.y > zombie.path[0] - zombie.velY:
                zombie.y += zombie.velX * -1
                screen.blit(pygame.transform.scale(enemyModelDown, (75, 75)),(zombie.x,zombie.y))
            else:
                zombie.velY = zombie.velY * -1
                zombie.y += zombie.velY
                screen.blit(pygame.transform.scale(enemyModelUp, (75, 75)),(zombie.x,zombie.y))
         
            
            
        
        if keys[pygame.K_a] and man.x > man.speed:
            man.x-=man.speed
            screen.blit(pygame.transform.scale(playerModelLeft, (100,100)), (man.x,man.y))
            man.left = True
            man.right = False
            man.up = False
            man.down = False
            man.still = False
            man.attacking = False
                
        elif keys[pygame.K_d] and man.x < 1280 - man.speed - man.width:
            man.x+=man.speed
            screen.blit(pygame.transform.scale(playerModelRight, (100,100)), (man.x,man.y))
            man.right = True
            man.left = False
            man.up = False
            man.down = False
            man.still = False
            man.attacking = False

            
        elif keys[pygame.K_w] and man.y > man.speed:
            man.y-=man.speed
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            man.up = True
            man.left = False
            man.right = False
            man.down = False
            man.still = False
            man.attacking = False
            
        elif keys[pygame.K_s] and man.y < 720 - man.height - man.speed:
            man.y+=man.speed
            screen.blit(pygame.transform.scale(playerModelDown, (100,100)), (man.x,man.y))
            man.down = True
            man.left = False
            man.up = False
            man.right = False
            man.still = False
            man.attacking = False

        elif man.still == True:
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            man.down = False
            man.left = False
            man.up = False
            man.right = False
            man.attacking = False
            if keys[pygame.K_SPACE]:
                man.attacking = True
                screen.blit(pygame.transform.scale(playerAttack, (100,100)), (man.x,man.y))
        
        if man.left == True:
            screen.blit(pygame.transform.scale(playerModelLeft, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                man.attacking = True
                screen.blit(pygame.transform.scale(playerAttack2, (100,100)), (man.x,man.y))
            else:
                man.attacking = False
        elif man.right == True:
            screen.blit(pygame.transform.scale(playerModelRight, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                man.attacking = True
                screen.blit(pygame.transform.scale(playerAttack3, (100,100)), (man.x,man.y))
            else:
                man.attacking = False
        elif man.up == True:
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                man.attacking = True
                screen.blit(pygame.transform.scale(playerAttack, (100,100)), (man.x,man.y))
            else:
                man.attacking = False
        elif man.down == True:
            screen.blit(pygame.transform.scale(playerModelDown, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                man.attacking = True
                screen.blit(pygame.transform.scale(playerAttack4, (100,100)), (man.x,man.y))
            else:
                man.attacking = False

        if man.attacking == True:
            if man.hitbox[1] - man.y<= zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.y >= zombie.hitbox[1]:
                if man.hitbox[0] + man.x >= zombie.hitbox[0] and man.hitbox[0] - man.x <= zombie.hitbox[0] + zombie.hitbox[2]:
                    print('ok')

        if keys[pygame.K_i]:
            running = False
            menuInGame()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        mainClock.tick(60)


        
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 8
        self.hitbox = (self.x + 11, self.y + 10, 70, 70)
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.attacking = False
        self.still = True
    
        
class enemy(object):
    def __init__(self, x, y, width, height, endX, endY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 11, self.y + 10, 70, 70)
        self.path = [x, endX]
        self.path2 = [y, endY]
        self.velX = 0
        self.velY = 0

def menuInGame():
    click = False
    running = True
    while running:
        area = pygame.display.set_mode((1280, 720))
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        draw_text('Menu', font, (255, 255, 255), screen, 25, 25)
        mx, my = pygame.mouse.get_pos()
        
        
        button_1 = pygame.Rect(140, 100, 225, 50)
        button_2 = pygame.Rect(140, 200, 225, 50)
        button_3 = pygame.Rect(140, 300, 225, 50)
        button_4 = pygame.Rect(140, 400, 225, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                print("1")
                running = False
                inventory()
        if button_2.collidepoint((mx, my)):
            if click:
                print("2")
                running = False
                skills()
        if button_3.collidepoint((mx, my)):
            if click:
                options()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        pygame.draw.rect(screen, (0, 0, 0), button_4)
        draw_text('Inventory', font, (255,255,255), screen, 145, 105)
        draw_text('Skills', font, (255,255,255), screen, 145, 205)
        draw_text('Options', font, (255,255,255), screen, 145, 305)
        draw_text('Quit Game', font, (255,255,255), screen, 145, 405)
        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    playable()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)
    
def inventory():
    click = False
    running = True
    while running:
        area = pygame.display.set_mode((1280, 720))
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        draw_text('Inventory', font, (255, 255, 255), screen, 25, 25)
        mx, my = pygame.mouse.get_pos()

        section = pygame.Rect(100, 100, 1100, 500)
        pygame.draw.rect(screen, (169,169,169), section)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    menuInGame()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60) 

def skills():
    click = False
    running = True
    while running:
        area = pygame.display.set_mode((1280, 720))
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        draw_text('Skills', font, (255, 255, 255), screen, 25, 25)
        mx, my = pygame.mouse.get_pos()

        section = pygame.Rect(100, 100, 1100, 500)
        pygame.draw.rect(screen, (169,169,169), section)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    menuInGame()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)

main_menu()
