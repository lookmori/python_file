import pygame,sys
import os

pygame.init()


screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('飞机大战')
flag = True

screen.fill('white')
bg_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/all.png'))

bg_rect = bg_img.get_rect()
bg_rect.center = (400,300) 


# 飞机和敌机



while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            
    key_down = pygame.key.get_pressed() 
    screen.blit(bg_img,bg_rect)

    
    pygame.display.update()


