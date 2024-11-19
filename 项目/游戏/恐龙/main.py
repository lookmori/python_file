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
grass = bg_img.subsurface(pygame.Rect(0,100,2440,30))
grass_rect = grass.get_rect(center = (400,300))

def drawGrass():
    global grass_rect,grass
    grass_rect.x -= 10
    if grass_rect.x > 8000 :
        grass_rect.x = 0
# 蝙蝠
# 蝙蝠大小 90*90
bf_img_list = []
bf_index = 0
bf_img_rect = bg_img.get_rect(center = (200,200))
for i in range(2):
    clip_img = pygame.Rect(260 + i*90,0,90,90)
    bf_img_list.append(bg_img.subsurface(clip_img))


#    LDPI: {
#             CACTUS_LARGE: { x: 332, y: 2 },
#             CACTUS_SMALL: { x: 228, y: 2 },
#             CLOUD: { x: 86, y: 2 },
#             HORIZON: { x: 2, y: 54 },
#             MOON: { x: 484, y: 2 },
#             PTERODACTYL: { x: 134, y: 2 },
#             RESTART: { x: 2, y: 2 },
#             TEXT_SPRITE: { x: 655, y: 2 },
#             TREX: { x: 848, y: 2 },
#             STAR: { x: 645, y: 2 }
#         },
#         HDPI: {
#             CACTUS_LARGE: { x: 652, y: 2 },
#             CACTUS_SMALL: { x: 446, y: 2 },
#             CLOUD: { x: 166, y: 2 },
#             HORIZON: { x: 2, y: 104 },
#             MOON: { x: 954, y: 2 },
#             PTERODACTYL: { x: 260, y: 2 },
#             RESTART: { x: 2, y: 2 },
#             TEXT_SPRITE: { x: 1294, y: 2 },
#             TREX: { x: 1678, y: 2 },
#             STAR: { x: 1276, y: 2 }
#         }

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
pygame.time.set_timer(dxrz_timer,100)



xrz_timer = pygame.USEREVENT + 4
pygame.time.set_timer(xrz_timer,1500)


# 小仙人掌动起来
def xrz_animotaion():
    
    global xrz_index,xrz_img_list,xrz_img_rect
    xrz_index = randint(0,5)
    xrz_img_rect = xrz_img_list[xrz_index]


# 大仙人掌动起来
def dxrz_animotaion():
    global dxrz_index,dxrz_img_list,dxrz_img_rect,dxrz_img
    dxrz_index = randint(0,5)
    dxrz_img = dxrz_img_list[dxrz_index]
    dxrz_img_rect = dxrz_img.get_rect()
    dxrz_img_rect.x +=10
    screen.blit(dxrz_img,dxrz_img_rect)
# 恐龙动起来
def kl_animotaion():
    global kl_index,kl_img_list,kl_img_rect,kl_img
    kl_img = kl_img_list[kl_index]
    kl_img_rect = kl_img.get_rect()
    kl_index +=1
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
    clock.tick(60)
    screen.fill('white')
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

        
 
        # key_down = pygame.key.get_pressed() 

        # if  event.type == pygame.KEYDOWN:
        #     if key_down[pygame.K_SPACE]: 
        #         kl_img_rect.y += 20
        #     screen.blit(kl_img,kl_img_rect)
        # if event.type == pygame.KEYUP:
        #     kl_img_rect.y = 0
        #     screen.blit(kl_img,kl_img_rect)

    
    #drawGrass()
    grass_rect.x -= 3
    if grass_rect.x > 800 :
        grass_rect.x = 0
    screen.blit(grass,grass_rect)
    print(grass_rect)
    pygame.display.update()
    
    
    
    

    


