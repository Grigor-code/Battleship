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

font_size=int(block_size/1.5)
#шрифт
font = pygame.font.SysFont('notosans',font_size)

class ShipOnGrid:
    def _init_ (self):
        self.available_bloks = set((a,b)   for a in range (1,11) for b in range (1,11))
        self.ships_set = set()
        self.ships = self.populate_grid()
    def create_start_block(self, available_blocks):
        x_or_y= random.randint(0,1)
        str_rev= random.choice((-1,1))
        x,y= random.choice(tuple(available_blocks))
        return x,y, x_or_y, str_rev
    def create_ship(self,number_of_blocks, available_blocks):
        ship_coordinate=[]
        x,y,x_or_y,str_rev=self.create_start_block(available_blocks)
        for _ in range (number_of_blocks):
            ship_coordinate.append((x,y))
            if not x or y:
                str_rev,x=self.add_block_to_ship(x,str_rev,x_or_y,ship_coordinate)
            else:
                str_rev, y = self.add_block_to_ship(y, str_rev, x_or_y, ship_coordinate)
                if self.is_ship_valid(ship_coordinate):
                    return ship_coordinate
                return self.create_ship(number_of_blocks, available_blocks)


    def add_block_to_ship(self,coor, str_rev, x_or_y,ship_coordinate):
        if (coor <= 1 and str_rev == -1) or (coor>= 10 and str_rev == 1):
            str_rev *= -1
            return str_rev, ship_coordinate[0][x_or_y] + str_rev
        else:
            return str_rev,ship_coordinate[-1][x_or_y] + str_rev




    def is_ship_valid(self, new_ship):
        ship= set(new_ship)
        return ship.issubset(self.available_bloks)
    def add_new_ship_to_set(self,new_ship):
        for elem in new_ship:
            self.ships_set.add(elem)
    def update_available_bloks_for_creating_ships(self,new_ship):
        for elem in new_ship:
            for k in range(-1,2):
                for m in range(1,2):
                    if 0<(elem[0]+k)<11 and 0< (elem[1]+m)<11:
                        self.available_bloks.discard((elem[0]+k, elem[1]+m))
    def populate_grid(self):
        ships_coordinates_list=[]
        for number_of_bloks in range(4,0,-1):
            for _ in range(5-number_of_bloks):
                new_ship=self.create_ship(number_of_bloks,self.available_blocks)
                ships_coordinates_list.append(new_ship)
                self.add_new_ship_to_set(new_ship)
                self.update_available_bloks_for_creating_ships(new_ship)
        return ships_coordinates_list


computer=ShipOnGrid()
human=ShipOnGrid()

def draw_ships(ships_coordinates_list):
    for elem in ships_coordinates_list:
        ship= sorted(elem)
        x_start=ship[0][0]
        y_start= ship[0][1]
        #вертикалные
        if len(ship)>1 and ship[0][0]==ship[1][0]:
            ship_width=block_size
            ship_height=block_size* len(ship)
        #hor
        else:
            ship_width= block_size* len(ship)
            ship_height=block_size
        x=block_size*(x_start-1)+left_margin
        y=block_size*(y_start-1)+upper_margin
        if ships_coordinates_list==human.ships:
            x+=15*block_size
        pygame.draw.rect(screen,Black,((x,y),(ship_width,ship_height)),width=block_size//10)
def draw_grid():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for y in range(11):
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
    draw_grid()
    draw_ships(computer.ships)
    draw_ships(human.ships)
    pygame.display.update()


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True




main()
pygame.quit()