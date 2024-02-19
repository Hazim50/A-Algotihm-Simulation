import pygame

running=True
maze,square_size,gap,selected_square,start_node_pos,end_node_pos,button_start_rect,button_clear_rect=(None for i in range(8))

def setter_event(_maze,_square_size,_gap,_button_start_rect,_button_clear_rect):
    global maze,square_size,gap,button_start_rect,button_clear_rect

    maze,square_size,gap,button_start_rect,button_clear_rect = _maze,_square_size,_gap,_button_start_rect,_button_clear_rect

def find_event(event):
    global running,selected_square,start_node_pos,end_node_pos,clicked_start_button,clicked_clear_button

    clicked_start_button,clicked_clear_button=False,False 

    if event.type==pygame.QUIT:
        running=False


    elif event.type==pygame.MOUSEMOTION:
        x,y=event.pos
        col = x // (square_size + gap)
        row = y // (square_size + gap)
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
            selected_square = (col, row)
        else:
            selected_square=None


    elif event.type==pygame.MOUSEBUTTONDOWN:
        x2,y2=event.pos
        button=event.button
        col = x2 // (square_size + gap)
        row = y2 // (square_size + gap)

        if button==1: 
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col]==0:
                start_node_pos = (row, col)
                print("start",start_node_pos)
        elif button==3:
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col]==0:
                end_node_pos = (row, col)
                print("end",end_node_pos)

        if button_start_rect[0] < x2 < button_start_rect[0] + button_start_rect[2] and button_start_rect[1] < y2 < button_start_rect[1] + button_start_rect[3]:
            clicked_start_button=True
        
        elif button_clear_rect[0] < x2 < button_clear_rect[0] + button_clear_rect[2] and button_clear_rect[1] < y2 < button_clear_rect[1] + button_clear_rect[3]:
            clicked_clear_button=True
            start_node_pos,end_node_pos=None,None
    return (running,selected_square,start_node_pos,end_node_pos,clicked_start_button,clicked_clear_button)