import pygame
import random


White = (255,255,255)
Black =(0,0,0)

block_size=30
left_margin=40
upper_margin=50

size =(left_margin+30*block_size, upper_margin+15*block_size)

pygame.init()

screen= pygame.display.set_mode(size)
pygame.display.set_caption("Морской бой")

font_size=int(block_size//1.5)
#шрифт
font = pygame.font.SysFont('notosans',font_size)

def main():
    game_over=False
    screen.fill(White)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
        pygame.display.update()



main()
pygame.quit()