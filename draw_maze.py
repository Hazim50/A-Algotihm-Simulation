import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (225, 153, 35)

pygame.init()

screen,font,square_size,gap,maze_size,screen_plus,window_height,window_width,button_width,button_height,button_start_rect,button_clear_rect=(None for i in range(12))

def setter_drawing(_screen,_font,_square_size,_gap,_maze_size,_screen_plus,_window_height,_window_width,_button_width,_button_height,_button_start_rect,_button_clear_rect):
    global screen,font,square_size,gap,maze_size,screen_plus,window_height,window_width,button_width,button_height,button_start_rect,button_clear_rect
    screen,font,square_size,gap,maze_size,screen_plus,window_height,window_width,button_width,button_height,button_start_rect,button_clear_rect=_screen,_font,_square_size,_gap,_maze_size,_screen_plus,_window_height,_window_width,_button_width,_button_height,_button_start_rect,_button_clear_rect

def draw_maze(maze,start_node,end_node,selected_square):
    for row in range(len(maze)):
        for col in range(len(maze[0])):

            if maze[row][col]==1:
                pygame.draw.rect(screen,BLACK,(col*(square_size+gap),row*(square_size+gap),square_size,square_size))
            elif maze[row][col]==5:
                pygame.draw.rect(screen,BLUE,(col*(square_size+gap),row*(square_size+gap),square_size,square_size))
            else:
                renk=RED if (col, row) == selected_square else WHITE
                pygame.draw.rect(screen,renk,(col*(square_size+gap),row*(square_size+gap),square_size,square_size))
                if start_node!=end_node:
                    if start_node is not None:
                        pygame.draw.rect(screen,GREEN,(start_node[1] * (square_size + gap), start_node[0] * (square_size + gap),square_size,square_size))
                    if end_node is not None:
                        pygame.draw.rect(screen,PURPLE,(end_node[1] * (square_size + gap), end_node[0] * (square_size + gap),square_size,square_size))
                else:
                    if start_node is not None:
                        pygame.draw.rect(screen,ORANGE,(start_node[1] * (square_size + gap), start_node[0] * (square_size + gap),square_size,square_size)) 
    pygame.draw.rect(screen,YELLOW,(0,(row+1)*(square_size+gap),window_width,screen_plus))
    draw_button()

def draw_button():
    pygame.draw.rect(screen, GREEN, button_start_rect)
    text1 = font.render("Start", True, WHITE)
    text_rect = text1.get_rect(center=button_start_rect.center)
    screen.blit(text1, text_rect)

    pygame.draw.rect(screen, GREEN, button_clear_rect)
    text2=font.render("Mix", True, WHITE)
    text2_rect=text2.get_rect(center=button_clear_rect.center)
    screen.blit(text2, text2_rect)