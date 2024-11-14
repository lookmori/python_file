import pygame,os
class Fire(pygame.sprite.Sprite):
  def __init__(self,screen,empty,rotate=180):
    super().__init__()
    self.img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/子弹弹药.png'))
    self.img = pygame.transform.rotate(pygame.transform.scale(self.img,(32,32)),rotate)
    self.img_rect = self.img.get_rect()
    self.img_rect.midbottom = empty.midbottom
    screen.blit(self.img,self.img_rect)
  
  def move(self,screen):
    self.img_rect.y += 5
    if self.img_rect.y > screen.get_height():
      self.img_rect.y = 0
    screen.blit(self.img,self.img_rect)