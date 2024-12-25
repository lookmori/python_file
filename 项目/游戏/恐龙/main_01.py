import pygame,random,os

pygame.init()

screen = pygame.display.set_mode((1200,300))

pygame.display.set_caption('恐龙游戏')
clock = pygame.time.Clock()
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

screen.fill('white')
kl_font = pygame.font.Font(None,25)
kl_text = kl_font.render("start",True,'red')
kl_text_rect = kl_text.get_rect(center = (WIDTH /2,40))


## 角色导入
bg_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/all.png')).convert_alpha()
grass = bg_img.subsurface(pygame.Rect(0,100,2440,30))
grass_rect = grass.get_rect(y= 250) #

# 循环标志
flag = True
# 移动标志
move_right = False
MOVE_SPEED = 10
## 飞行动物

bf_img_list = []
bf_index = 0
bf_img = None
bf_img_rect = None


for i in range(2):
    clip_img = pygame.Rect(265 + i*90,0,90,90)
    bf_img = bg_img.subsurface(clip_img)
    bf_img_list.append(bf_img)



# bf_img = bf_img_list[bf_index]
bf_img_rect = bf_img.get_rect(x = 600,y = 150)  


#恐龙大小 88*100
kl_img_list = []
kl_index = 0
for i in range(6):
    clip_img = pygame.Rect(1680 + i*88,0,88,100)
    kl_img_list.append(bg_img.subsurface(clip_img)) 


kl_index = 0
kl_img = kl_img_list[kl_index]
kl_img_rect =  kl_img.get_rect(y=160)


def kl_animotaion():
    global kl_index
    kl_index +=1
    if kl_index > 5:
        kl_index = 0

def fly_move():
  global bf_img_list,bf_img,bf_img_rect,bf_index
  bf_img_rect.x -= MOVE_SPEED
  if bf_img_rect.x < 0:
    bf_img_rect.x = 1200

  bf_index +=1
  if bf_index > 1:
    bf_index = 0
    

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


xrz_img = xrz_img_list[xrz_index]
xrz_img_rect = xrz_img.get_rect(y=190,x= 1000)
dxrz_img = dxrz_img_list[dxrz_index]
dxrz_img_rect = dxrz_img.get_rect(y=160,x = 950)



def xrz_move():
  global xrz_img_rect,xrz_index,dxrz_index,dxrz_img_rect
  xrz_img_rect.x -= MOVE_SPEED
  dxrz_img_rect.x -= MOVE_SPEED
  if xrz_img_rect.x <0:
    xrz_index = random.randint(0,4)
    xrz_img_rect.x = 1200
  if dxrz_img_rect.x <0:
    dxrz_index = random.randint(0,4)
    dxrz_img_rect.x = 1200

  
def collide_rect(body,collide):
  return body.colliderect(collide)

kl_timer = pygame.USEREVENT + 1
pygame.time.set_timer(kl_timer,50)

fl_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fl_timer,100)

xrz_timer = pygame.USEREVENT + 3
pygame.time.set_timer(xrz_timer,50)

speed_timer = pygame.USEREVENT + 4
pygame.time.set_timer(speed_timer,5000)

# 主循环
while flag:
  
  bf_img = bf_img_list[bf_index]
  kl_img = kl_img_list[kl_index]
  screen.fill('white')
  screen.blit(kl_text,kl_text_rect)

  screen.blit(grass,grass_rect)
  grass_rect.x -= MOVE_SPEED
  if grass_rect.x < -1200:
    grass_rect.x = 0

 
  

  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == kl_timer:
      kl_animotaion()
    if event.type == fl_timer:
      fly_move()
    if event.type == xrz_timer:
      xrz_move()
    if event.type == speed_timer:
      MOVE_SPEED += 2
    

    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_RIGHT:
        move_right = True
        
      if event.key == pygame.K_SPACE:
        kl_img_rect.y -= 100
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        kl_img_rect.y += 100
      if event.key == pygame.K_RIGHT:
        move_right = False
  if move_right and kl_img_rect.x < 1100:
     kl_img_rect.x += MOVE_SPEED


  screen.blit(xrz_img,xrz_img_rect)
  screen.blit(dxrz_img,dxrz_img_rect)
  screen.blit(bf_img,bf_img_rect)
  screen.blit(kl_img,kl_img_rect)
  if collide_rect(kl_img_rect,bf_img_rect) or collide_rect(kl_img_rect,dxrz_img_rect) or collide_rect(kl_img_rect,xrz_img_rect):
    MOVE_SPEED = 0
    kl_text = kl_font.render("fail",True,'red')
    kl_text_rect = kl_text.get_rect(center = (WIDTH /2,HEIGHT /2))
    screen.blit(kl_text,kl_text_rect)
    flag = False
  pygame.display.update()
  clock.tick(60)

