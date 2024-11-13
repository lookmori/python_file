from time import sleep
import pygame,os,random
from fire import Fire
class Empty(pygame.sprite.Sprite):
    def __init__(self, screen,*groups):
        super().__init__(*groups)
        self.img =  pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)),'images/敌人.png'))
        self.img_rect = self.img.get_rect()
        self.lefe = 100
        random_X = random.randint(30,700)
        self.img_rect.center = (random_X,0)
        self.fireList = []
        

    

    def move(self,screen):
        random_Y = random.randint(0,10)
        self.img_rect.y += random_Y
        # fire = Fire(self)
        # fire.move(screen)
        sleep(0.03)
        screen.blit(self.img,self.img_rect)
