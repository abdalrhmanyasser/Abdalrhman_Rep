import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((200, 200))

seguisy80 = pygame.freetype.SysFont("segoeuisymbol", 100)
emoji, rect = seguisy80.render('🛑', "RED")
rect.center = window.get_rect().center

run = True
while run:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("lightgray")
    window.blit(emoji, rect)
    pygame.display.flip()

pygame.quit()