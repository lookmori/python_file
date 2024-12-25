import pygame





pygame.init()

pygame.display.set_caption('贪吃蛇')
screen = pygame.display.set_mode((600,600))

def draw_bg(width,height,cellsize):
    bg_surface = pygame.Surface((width,height))
    bg_surface.fill((255,0,0))
    for x in range(0,width,cellsize):
        pygame.draw.line(bg_surface,(0,0,0),(x,0),(x,height))
    for y in range(0,height,cellsize):
        pygame.draw.line(bg_surface,(0,0,0),(0,y),(width,y))
    screen.blit(bg_surface,(0,0))

flag = True

while flag:
    draw_bg(600,600,30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()