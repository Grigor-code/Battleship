import pygame
import random


White = (255,255,255)
Black =(0,0,0)

block_size=40
left_margin=100
upper_margin=100

size =(left_margin+30*block_size, upper_margin+15*block_size)

pygame.init()

screen= pygame.display.set_mode(size)
pygame.display.set_caption("Морской бой")

font_size=int(block_size//1.5)
#шрифт
font = pygame.font.SysFont('notosans',font_size)

def draw_grid():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for y in range(11):
        for x in range(11):
            pygame.draw.line(screen, Black, (left_margin,upper_margin + y* block_size), (left_margin+10*block_size,upper_margin+y*block_size), 1)
            pygame.draw.line(screen,Black,(left_margin+y*block_size,upper_margin),(left_margin+y*block_size,upper_margin+10*block_size),1)

            pygame.draw.line(screen, Black, (left_margin+15*block_size, upper_margin + y * block_size),
                             (left_margin + 25 * block_size, upper_margin + y * block_size), 1)
            pygame.draw.line(screen, Black, (left_margin + y * block_size +15*block_size, upper_margin),
                             (left_margin + y * block_size+15*block_size, upper_margin + 10 * block_size), 1)
        if y< 10:
            num_vert=font.render(str(y+1),True,Black)
            letters_horz=font.render(letters[y],True,Black)

            num_vert_width = num_vert.get_width()
            num_vert_heigth=num_vert.get_height()
            letters_horz_width=letters_horz.get_width()

            screen.blit(num_vert,(left_margin- (block_size//2+num_vert_width//2), upper_margin +y*block_size+(block_size//2-num_vert_heigth//2)))

            screen.blit(letters_horz, (left_margin+y*block_size+(block_size//2-letters_horz_width//2),upper_margin+10.2*block_size))

            screen.blit(num_vert, (left_margin - (block_size // 2 + num_vert_width // 2)+15*block_size,
                                   upper_margin + y * block_size + (block_size // 2 - num_vert_heigth // 2)))

            screen.blit(letters_horz, (
            left_margin + y * block_size + (block_size // 2 - letters_horz_width // 2)+15*block_size, upper_margin + 10.2 * block_size))


def main():
    game_over=False
    screen.fill(White)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
        draw_grid()
        pygame.display.update()



main()
pygame.quit()