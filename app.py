import pygame
import os 

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 100)
surface =pygame.display.set_mode((1000,700))
pygame.display.set_caption("Sudoku game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False