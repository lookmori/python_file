import pygame,sys
import os

pygame.init()


screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('恐龙')
flag = True

screen.fill('white')
bg_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/all.png'))
kl_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/all.png'))

clip_img = pygame.Rect(20,0,145,100)
kl_img_rect = kl_img.subsurface(clip_img)



# 飞机和敌机



while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            
    key_down = pygame.key.get_pressed() 
    screen.blit(kl_img_rect,(0,0,100,100))

    
    pygame.display.update()


