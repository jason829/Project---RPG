import pygame  
import sys
import time
import random
import os
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
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 5, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False


def main_menu():
    while True:
 
        screen.fill((0,0,0))
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
    while running:
        area = pygame.display.set_mode((1280, 720))
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        playerMovement()
   
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
                   
def playerMovement():
    man = player(500, 500, 100, 100)
    running = True
    while running:
        screen.blit(pygame.transform.scale(backgroundImage2, (1280, 720)),(0,0))
        pygame.time.delay(50)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and man.x > man.speed:
            man.x-=man.speed
            screen.blit(pygame.transform.scale(playerModelLeft, (100,100)), (man.x,man.y))
            man.left = True
            man.right = False
            man.up = False
            man.down = False
            man.still = False
                
        elif keys[pygame.K_d] and man.x < 1280 - man.speed - man.width:
            man.x+=man.speed
            screen.blit(pygame.transform.scale(playerModelRight, (100,100)), (man.x,man.y))
            man.right = True
            man.left = False
            man.up = False
            man.down = False
            man.still = False
            
        elif keys[pygame.K_w] and man.y > man.speed:
            man.y-=man.speed
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            man.up = True
            man.left = False
            man.right = False
            man.down = False
            man.still = False
            
        elif keys[pygame.K_s] and man.y < 720 - man.height - man.speed:
            man.y+=man.speed
            screen.blit(pygame.transform.scale(playerModelDown, (100,100)), (man.x,man.y))
            man.down = True
            man.left = False
            man.up = False
            man.right = False
            man.still = False

        elif man.still == True:
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                screen.blit(pygame.transform.scale(playerAttack, (100,100)), (man.x,man.y))
        
        if man.left == True:
            screen.blit(pygame.transform.scale(playerModelLeft, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                screen.blit(pygame.transform.scale(playerAttack2, (100,100)), (man.x,man.y))
        elif man.right == True:
            screen.blit(pygame.transform.scale(playerModelRight, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                screen.blit(pygame.transform.scale(playerAttack3, (100,100)), (man.x,man.y))
        elif man.up == True:
            screen.blit(pygame.transform.scale(playerModel, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                screen.blit(pygame.transform.scale(playerAttack, (100,100)), (man.x,man.y))
        elif man.down == True:
            screen.blit(pygame.transform.scale(playerModelDown, (100,100)), (man.x,man.y))
            if keys[pygame.K_SPACE]:
                screen.blit(pygame.transform.scale(playerAttack4, (100,100)), (man.x,man.y))
            

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
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.still = True
    
        
        

        


main_menu()
