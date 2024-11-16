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
grass_rect = grass.get_rect(center = (400,250))


## 飞行动物

bf_img_list = []
bf_index = 0
bf_img = None
bf_img_rect = None
for i in range(2):
    clip_img = pygame.Rect(260 + i*90,0,90,90)
    bf_img = bg_img.subsurface(clip_img)
    bf_img_list.append(bg_img)



def fly_move():
  global bf_img_list,bf_img,bf_img_rect,bf_index
  bf_img_rect = bf_img_list[bf_index].get_rect(x=600,y=100)  
  # bf_img_rect.x -= 5
  # if bf_img_rect.x < 0:
  #   bf_img_rect.x = 1200
  # if bf_index == 1:
  #   bf_index =0
  # else:
  #   bf_index = 1
    




flag = True
while flag:
  
  screen.blit(kl_text,kl_text_rect)
  screen.blit(grass,grass_rect)
  fly_move()
  print(bf_img_rect.x)
  screen.blit(bf_img,bf_img_rect)


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()


  pygame.display.update()
  clock.tick(60)

