import pygame,os
class Fire(pygame.sprite.Sprite):
  def __init__(self,empty):
    super().__init__()
    self.img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/子弹弹药.png'))
    self.img = pygame.transform.scale(self.img,(32,32))
    self.img_rect = empty.img_rect
  
  def move(self,screen):
    self.img_rect.y += 10
    screen.blit(self.img,self.img_rect)