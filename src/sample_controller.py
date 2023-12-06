
# class Controller:
  
#   def __init__(self):
#     #setup pygame data
    
#   def mainloop(self):
#     #select state loop
    
  
#   ### below are some sample loop states ###

#   def menuloop(self):
    
#       #event loop

#       #update data

#       #redraw
      
#   def gameloop(self):
#       #event loop

#       #update data

#       #redraw
    
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
NUM_RECTANGLES = int(input("number of rectangles?: "))
RECTANGLE_HEIGHT_MIN = int(input("minimum height?: "))
RECTANGLE_HEIGHT_MAX = int(input("maximum height?: "))
RECTANGLE_WIDTH = (SCREEN_WIDTH*0.75)/NUM_RECTANGLES



# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RECTANGLE_COLOR = (0, 0, 255)
SWAP_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Function to generate random heights for rectangles
def generate_random_heights(num_rectangles):
    return [random.randint(RECTANGLE_HEIGHT_MIN, RECTANGLE_HEIGHT_MAX) for _ in range(num_rectangles)]

# Bubble Sort algorithm
def bubble_sort(heights):
    n = len(heights)
    for i in range(n):
        for j in range(0, n-i-1):
            if heights[j] > heights[j+1]:
                # Swap heights
                heights[j], heights[j+1] = heights[j+1], heights[j]
                # Update display
                update_display(j, j+1, heights)

# Function to update the display
def update_display(i, j, heights):
    screen.fill(BLACK)
    for idx in range(NUM_RECTANGLES):
        x_position = idx * (SCREEN_WIDTH // NUM_RECTANGLES)
        y_position = SCREEN_HEIGHT - heights[idx]

        if idx == i or idx == j:
            # Highlight the rectangles being swapped
            pygame.draw.rect(screen, SWAP_COLOR, (x_position, y_position, RECTANGLE_WIDTH, heights[idx]))
        else:
            pygame.draw.rect(screen, RECTANGLE_COLOR, (x_position, y_position, RECTANGLE_WIDTH, heights[idx]))

        text = font.render(str(heights[idx]), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(x_position + RECTANGLE_WIDTH // 2, SCREEN_HEIGHT - 10))
        screen.blit(text, text_rect)
    elapsed_time = pygame.time.get_ticks()/1000
    timer_text = timer_font.render(f"{elapsed_time} seconds", True, TEXT_COLOR)
    timer_rect = timer_text.get_rect(topleft=(SCREEN_WIDTH - 150, 10))
    screen.blit(timer_text, timer_rect)

    pygame.display.flip()
    pygame.time.delay(500)  # Delay to make the sorting steps visible

# Create a list of random heights for rectangles
rectangle_heights = generate_random_heights(NUM_RECTANGLES)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Rectangles")

# Font for displaying text
font = pygame.font.Font(None, 24)
timer_font = pygame.font.Font(None, 24)
# Clock to control the frame rate
clock = pygame.time.Clock()

# Main loop
running = True
sorting = False  # Flag to indicate whether the sorting is active

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Start sorting when the space bar is pressed
            sorting = True

    if sorting:
        # Run the Bubble Sort algorithm
        bubble_sort(rectangle_heights)
        sorting = False  # Stop sorting after one iteration

    # Quit the loop after the sorting is done
    if not any(heights != sorted(heights) for heights in [rectangle_heights]):
        running = False


# Quit Pygame
pygame.quit()


