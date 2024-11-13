import pygame,sys
import os

from plane import Plane
from empty import Empty

pygame.init()
# screen = pygame.display.set_mode((1024,1358))
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('飞机大战')
flag = True

bg_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/风景.png'))

bg_rect = bg_img.get_rect()
bg_rect.center = (400,300) 


# 飞机和敌机
plane = Plane(screen)
empty = Empty(screen)



while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        key_down = pygame.key.get_pressed()
        
    screen.blit(bg_img,bg_rect)
    plane.move(key_down,screen)
    empty.move(screen)
    pygame.display.update()


