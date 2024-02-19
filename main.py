import pygame
import sys
from a_star import astar
from create_maze import create_maze
from draw_maze import draw_maze,setter_drawing
from events import find_event,setter_event
from copy import deepcopy

pygame.init()

class Game:
    def __init__(self):
        self.square_size=30
        self.gap=1
        self.maze_size=(25, 25)
        self.road_ratio=0.5
        self.main_maze=None
        self.maze=None
        self.start_node_pos=None
        self.end_node_pos=None
        self.selected_square=None
    
        self.font = pygame.font.SysFont(None, 24)
        self.button_width,self.button_height=120,50
        self.screen_plus=70
        self.window_width = (self.maze_size[1]) * (self.square_size + self.gap)
        self.window_height = (self.maze_size[0]) * (self.square_size + self.gap) +self.screen_plus
        self.button_start_rect = pygame.Rect(self.window_width // 2 - self.button_width // 2 - (self.window_width // 4), self.window_height - ((self.screen_plus-self.button_height)/2+self.button_height), self.button_width, self.button_height)
        self.button_clear_rect = pygame.Rect(self.window_width // 2 - self.button_width // 2 + (self.window_width // 4), self.window_height - ((self.screen_plus-self.button_height)/2+self.button_height), self.button_width, self.button_height)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("A* Simulation")
    
    def mix(self):
        self.main_maze.clear()
        self.main_maze=create_maze(self.maze_size,self.road_ratio)
        self.maze.clear()
        self.maze=deepcopy(self.main_maze)
        
    def find_path(self):
        if self.start_node_pos is not None and self.end_node_pos is not None:
            solved_maze=astar(self.maze,self.start_node_pos,self.end_node_pos)
            if solved_maze is None:
                print("Maze is Blocked")
            else:
                self.maze=solved_maze
        else:
            print("Please choose the correct start and end points !")

    def main(self):
        self.main_maze=create_maze(self.maze_size,self.road_ratio)
        self.maze=deepcopy(self.main_maze)
        running=True
        while running:
            for event in pygame.event.get():
                setter_event(self.maze,self.square_size,self.gap,self.button_start_rect,self.button_clear_rect)
                return_event=find_event(event)
                
                running=return_event[0]
                self.selected_square=return_event[1]
                self.start_node_pos=return_event[2]
                self.end_node_pos=return_event[3]
                clicked_start_button=return_event[4]
                clicked_clear_button=return_event[5]


                if clicked_start_button:
                    self.maze.clear()
                    self.maze=deepcopy(self.main_maze)
                    print(f"clicked start button, start={self.start_node_pos}, end={self.end_node_pos}")
                    self.find_path()

                elif clicked_clear_button:
                    self.mix()
                    self.start_node_pos,self.end_node_pos=None,None

            setter_drawing(self.screen,self.font,self.square_size,self.gap,self.maze_size,self.screen_plus,self.window_height,self.window_width,self.button_width,self.button_height,self.button_start_rect,self.button_clear_rect)           
            draw_maze(self.maze,self.start_node_pos,self.end_node_pos,self.selected_square)
            pygame.display.update()
        
        pygame.quit()
        sys.exit()                

game=Game()
game.main()