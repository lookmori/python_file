import pygame,sys
import os
from random import *

pygame.init()


screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('恐龙')
flag = True

screen.fill('white')
bg_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/all.png')).convert_alpha()

# 蝙蝠
# 蝙蝠大小 90*90
bf_img_list = []
bf_index = 0
bf_img_rect = bg_img.get_rect(center = (200,200))
for i in range(2):
    clip_img = pygame.Rect(260 + i*90,0,90,90)
    bf_img_list.append(bg_img.subsurface(clip_img))


# 仙人掌
# 仙人掌大小 35*70
xrz_img_list = []
xrz_index = 0
for i in range(6):
    clip_img = pygame.Rect(445 + i*35,0,35,70)
    xrz_img_list.append(bg_img.subsurface(clip_img))

# 大仙人掌
# 大仙人掌 大小 50*90
dxrz_img_list = []
dxrz_index = 0
for i in range(6):
    clip_img = pygame.Rect(650 + i*50,0,50,95)
    dxrz_img_list.append(bg_img.subsurface(clip_img))

# 恐龙

#恐龙大小 88*100
kl_img_list = []
kl_index = 0
for i in range(6):
    clip_img = pygame.Rect(1680 + i*88,0,88,100)
    kl_img_list.append(bg_img.subsurface(clip_img)) 






# 事件触发
kl_timer = pygame.USEREVENT + 1
pygame.time.set_timer(kl_timer,500)

bf_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bf_timer,300)

dxrz_timer = pygame.USEREVENT + 3
pygame.time.set_timer(dxrz_timer,4500)



xrz_timer = pygame.USEREVENT + 4
pygame.time.set_timer(xrz_timer,1500)


# 小仙人掌动起来
def xrz_animotaion():
    
    global xrz_index,xrz_img_list,xrz_img_rect
    xrz_index = randint(0,5)
    xrz_img_rect = xrz_img_list[xrz_index]


# 大仙人掌动起来
def dxrz_animotaion():
    global dxrz_index,dxrz_img_list,dxrz_img_rect
    dxrz_index = randint(0,5)
    dxrz_img_rect = dxrz_img_list[dxrz_index]
# 恐龙动起来
def kl_animotaion():
    global kl_index,kl_img_list,kl_img_rect,kl_img
    kl_img = kl_img_list[kl_index]
    kl_img_rect = kl_img.get_rect()
    kl_index +=1
    pygame.time.delay(200)
    if kl_index > 5:
        kl_index = 0

# 蝙蝠动起来
def bf_animotaion():
    global bf_index,bf_img_list,bf_img_rect
    bf_img_rect = bf_img_list[bf_index]
    if bf_index == 0:
        bf_index = 1
    else:
        bf_index = 0


while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == kl_timer:
            kl_animotaion()
            screen.blit(kl_img,kl_img_rect)
        if event.type == bf_timer:
            bf_animotaion()
            screen.blit(bf_img_rect,(100,150,90,90))
        if event.type == xrz_timer:
            xrz_animotaion()
            screen.blit(xrz_img_rect,(250,150,34,70))

        if event.type == dxrz_timer:
            dxrz_animotaion()
            screen.blit(dxrz_img_rect,(350,150,50,100))   

            
 
        key_down = pygame.key.get_pressed() 

        if  event.type == pygame.KEYDOWN:
            if key_down[pygame.K_SPACE]: 
                kl_img_rect.y += 20
            screen.blit(kl_img,kl_img_rect)
        if event.type == pygame.KEYUP:
            kl_img_rect.y = 0
            screen.blit(kl_img,kl_img_rect)


    pygame.display.update()
    clock.tick(60)
    
    

    


