import pygame,os
class Plane(pygame.sprite.Sprite):
    def __init__(self, screen,*groups):
        super().__init__(*groups)
        self.img =  pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/飞机.png'))
        self.img = pygame.transform.rotate(self.img,180)
        self.img_rect = self.img.get_rect()
        self.lefe = 100
    
    def move(self,key,screen):
        if key[pygame.K_UP]:
            self.img_rect.y -=5
        if key[pygame.K_DOWN]:
            self.img_rect.y +=5
        if key[pygame.K_LEFT]:
            self.img_rect.x -=5
        if key[pygame.K_RIGHT]:
            self.img_rect.x +=5
        screen.blit(self.img,self.img_rect)
