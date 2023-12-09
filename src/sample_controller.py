import pygame
import random

class Controller:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 768

        # Colors
        self.BLACK = (0, 0, 0)
        self.RECTANGLE_COLOR = (0, 0, 255)
        self.SWAP_COLOR = (255, 0, 0)
        self.TEXT_COLOR = (255, 255, 255)
        self.button_pressed_color = (203, 195, 227)

        # Initialize Pygame display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Bubble Sorting")

        # Font for displaying text
        self.font = pygame.font.Font(None, 24)

        # Clock to control the frame rate
        self.clock = pygame.time.Clock()

        # Initialize button colors
        self.init_button_colors()

        # Time tracking attribute
        self.start_time = 0

        # Running and menu_active as instance variables
        self.running = True
        self.menu_active = True

    def init_button_colors(self):
        # Button colors for menu
        self.button_color10 = (255, 0, 255)
        self.button_color20 = (255, 0, 255)
        self.button_color30 = (255, 0, 255)
        self.button_color50 = (255, 0, 255)
        self.button_color100 = (255, 0, 255)
        self.button_color150 = (255, 0, 255)
        self.button_color500 = (255, 0, 255)
        self.button_color600 = (255, 0, 255)
        self.button_color700 = (255, 0, 255)

    def mainloop(self):
        # Main loop

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.menu_active:
                    self.handle_menu_clicks()

            if self.menu_active:
                # Draw the menu screen
                self.draw_menu()
            else:
                # Draw the sorting screen
                self.handle_sorting_screen()

        # Quit Pygame
        pygame.quit()

    def handle_menu_clicks(self):
        # Handle menu button clicks
        mouse_pos = pygame.mouse.get_pos()

        # Check number of rectangles buttons
        if self.button_10_rect.collidepoint(mouse_pos):
            self.button_color10 = self.button_pressed_color
            self.num_rectangles = 10
        elif self.button_20_rect.collidepoint(mouse_pos):
            self.button_color20 = self.button_pressed_color
            self.num_rectangles = 20
        elif self.button_30_rect.collidepoint(mouse_pos):
            self.button_color30 = self.button_pressed_color
            self.num_rectangles = 30

        # Check minimum height buttons
        elif self.button_50_min.collidepoint(mouse_pos):
            self.button_color50 = self.button_pressed_color
            self.rectangle_height_min = 50
        elif self.button_100_min.collidepoint(mouse_pos):
            self.button_color100 = self.button_pressed_color
            self.rectangle_height_min = 100
        elif self.button_150_min.collidepoint(mouse_pos):
            self.button_color150 = self.button_pressed_color
            self.rectangle_height_min = 150

        # Check maximum height buttons
        elif self.button_500_max.collidepoint(mouse_pos):
            self.rectangle_height_max = 500
            self.button_color500 = self.button_pressed_color
            self.menu_active = False
            self.start_time = pygame.time.get_ticks()  
        elif self.button_600_max.collidepoint(mouse_pos):
            self.rectangle_height_max = 600
            self.button_color600 = self.button_pressed_color
            self.menu_active = False
            self.start_time = pygame.time.get_ticks()  
        elif self.button_700_max.collidepoint(mouse_pos):
            self.rectangle_height_max = 700
            self.button_color700 = self.button_pressed_color
            self.menu_active = False
            self.start_time = pygame.time.get_ticks()  

    def draw_menu(self):
        # Draw the menu screen
        self.screen.fill(self.BLACK)

        # Font for menu buttons
        button_font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 72)

        # Draw instruction texts
        title_text = title_font.render("Bubble Sorting", True, self.TEXT_COLOR)
        instruction_text = button_font.render("Instructions: click buttons from left to right, only select 1 option from each column.", True, self.TEXT_COLOR)

        # Draw menu buttons for number of rectangles
        self.button_10_rect = pygame.draw.rect(self.screen, self.button_color10, (100, 200, 200, 50))
        self.button_20_rect = pygame.draw.rect(self.screen, self.button_color20, (100, 300, 200, 50))
        self.button_30_rect = pygame.draw.rect(self.screen, self.button_color30, (100, 400, 200, 50))

        text_10 = button_font.render("10 Elements", True, self.TEXT_COLOR)
        text_20 = button_font.render("20 Elements", True, self.TEXT_COLOR)
        text_30 = button_font.render("30 Elements", True, self.TEXT_COLOR)

        self.screen.blit(text_10, (100 + 20, 200 + 10))
        self.screen.blit(text_20, (100 + 20, 300 + 10))
        self.screen.blit(text_30, (100 + 20, 400 + 10))
        self.screen.blit(title_text, (300, 0))
        self.screen.blit(instruction_text, (25, 100))

        # Draw menu buttons for minimum height
        self.button_50_min = pygame.draw.rect(self.screen, self.button_color50, (400, 200, 200, 50))
        self.button_100_min = pygame.draw.rect(self.screen, self.button_color100, (400, 300, 200, 50))
        self.button_150_min = pygame.draw.rect(self.screen, self.button_color150, (400, 400, 200, 50))

        text_50_min = button_font.render("50 Min Height", True, self.TEXT_COLOR)
        text_100_min = button_font.render("100 Min Height", True, self.TEXT_COLOR)
        text_150_min = button_font.render("150 Min Height", True, self.TEXT_COLOR)

        self.screen.blit(text_50_min, (400 + 20, 200 + 10))
        self.screen.blit(text_100_min, (400 + 20, 300 + 10))
        self.screen.blit(text_150_min, (400 + 20, 400 + 10))

        # Draw menu buttons for maximum height
        self.button_500_max = pygame.draw.rect(self.screen, self.button_color500, (700, 200, 200, 50))
        self.button_600_max = pygame.draw.rect(self.screen, self.button_color600, (700, 300, 200, 50))
        self.button_700_max = pygame.draw.rect(self.screen, self.button_color700, (700, 400, 200, 50))

        text_500_max = button_font.render("500 Max Height", True, self.TEXT_COLOR)
        text_600_max = button_font.render("600 Max Height", True, self.TEXT_COLOR)
        text_700_max = button_font.render("700 Max Height", True, self.TEXT_COLOR)

        self.screen.blit(text_500_max, (700 + 20, 200 + 10))
        self.screen.blit(text_600_max, (700 + 20, 300 + 10))
        self.screen.blit(text_700_max, (700 + 20, 400 + 10))

        pygame.display.flip()

    def handle_sorting_screen(self):
        # Draw the sorting screen
        self.RECTANGLE_WIDTH = (self.SCREEN_WIDTH * 0.75) / self.num_rectangles

        # Function to generate random heights for rectangles
        def generate_random_heights(num_rectangles):
            return [random.randint(self.rectangle_height_min, self.rectangle_height_max) for _ in range(num_rectangles)]

        rectangle_heights = generate_random_heights(self.num_rectangles)
        total_time = self.bubble_sort(rectangle_heights)
        fptr = open("time.txt", 'w')
        fptr.write(f"Time it took: {total_time:.2f} seconds")
        fptr.close()
        self.running = False  # Stop the program after one iteration

    def bubble_sort(self, heights):
        start_time = pygame.time.get_ticks() / 1000
        n = len(heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j] > heights[j+1]:
                    # Swap heights
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    # Update display
                    self.update_display(j, j+1, heights)
        end_time = pygame.time.get_ticks() / 1000
        time_taken = end_time - start_time
        return time_taken  # Return the total time taken

    def update_display(self, i, j, heights):
        self.screen.fill(self.BLACK)
        for idx in range(len(heights)):
            x_position = idx * (self.SCREEN_WIDTH // len(heights))
            y_position = self.SCREEN_HEIGHT - heights[idx]

            if idx == i or idx == j:
                # Highlight the rectangles being swapped
                pygame.draw.rect(self.screen, self.SWAP_COLOR, (x_position, y_position, self.RECTANGLE_WIDTH, heights[idx]))
            else:
                pygame.draw.rect(self.screen, self.RECTANGLE_COLOR, (x_position, y_position, self.RECTANGLE_WIDTH, heights[idx]))

            text = self.font.render(str(heights[idx]), True, self.TEXT_COLOR)
            text_rect = text.get_rect(center=(x_position + self.RECTANGLE_WIDTH // 2, self.SCREEN_HEIGHT - 10))
            self.screen.blit(text, text_rect)

        current_time = pygame.time.get_ticks()/1000 - self.start_time/1000
        timer_text = self.font.render(f"{current_time:.3f} seconds", True, self.TEXT_COLOR)
        timer_rect = timer_text.get_rect(topleft=(self.SCREEN_WIDTH - 150, 10))
        self.screen.blit(timer_text, timer_rect)
        pygame.display.flip()
        self.clock.tick(3)  # Control the frame rate (3 frames per second)

# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Constants
# SCREEN_WIDTH = 1024
# SCREEN_HEIGHT = 768



# # Colors
# BLACK = (0, 0, 0)
# RECTANGLE_COLOR = (0, 0, 255)
# SWAP_COLOR = (255, 0, 0)
# TEXT_COLOR = (255, 255, 255)

# button_color10 = (255, 0, 255)
# button_color20 = (255, 0, 255)
# button_color30 = (255, 0, 255)

# button_color50 = (255, 0, 255)
# button_color100 = (255, 0, 255)
# button_color150 = (255, 0, 255)

# button_color500 = (255, 0, 255)
# button_color600 = (255, 0, 255)
# button_color700 = (255, 0, 255)

# button_pressed_color = (203, 195, 227)



# # Bubble Sort algorithm
# def bubble_sort(heights):
#     start_time = pygame.time.get_ticks() / 1000
#     n = len(heights)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if heights[j] > heights[j+1]:
#                 # Swap heights
#                 heights[j], heights[j+1] = heights[j+1], heights[j]
#                 # Update display
#                 update_display(j, j+1, heights)
#     end_time = pygame.time.get_ticks() / 1000
#     time_taken = end_time - start_time
#     return time_taken  # Return the total time taken

# # Function to update the display
# def update_display(i, j, heights):
#     screen.fill(BLACK)
#     for idx in range(len(heights)):
#         x_position = idx * (SCREEN_WIDTH // len(heights))
#         y_position = SCREEN_HEIGHT - heights[idx]

#         if idx == i or idx == j:
#             # Highlight the rectangles being swapped
#             pygame.draw.rect(screen, SWAP_COLOR, (x_position, y_position, RECTANGLE_WIDTH, heights[idx]))
#         else:
#             pygame.draw.rect(screen, RECTANGLE_COLOR, (x_position, y_position, RECTANGLE_WIDTH, heights[idx]))

#         text = font.render(str(heights[idx]), True, TEXT_COLOR)
#         text_rect = text.get_rect(center=(x_position + RECTANGLE_WIDTH // 2, SCREEN_HEIGHT - 10))
#         screen.blit(text, text_rect)
#     current_time = pygame.time.get_ticks()/1000 - start_time/1000
#     timer_text = font.render(f"{current_time:.3f} seconds", True, TEXT_COLOR)
#     timer_rect = timer_text.get_rect(topleft=(SCREEN_WIDTH - 150, 10))
#     screen.blit(timer_text, timer_rect)
#     pygame.display.flip()
#     clock.tick(3)  # Control the frame rate (3 frames per second)
    

# # Function to create menu buttons
# def draw_menu():
#     screen.fill(BLACK)

#     # Font for menu buttons
#     button_font = pygame.font.Font(None, 36)
#     title_font = pygame.font.Font(None, 72)

#     # Draw instruction texts
#     title_text = title_font.render("Bubble Sorting", True, TEXT_COLOR)
#     instruction_text = button_font.render("Instructions: click buttons from left to right, only select 1 option from each column.", True, TEXT_COLOR)

#     # Draw menu buttons for number of rectangles
#     button_10_rect = pygame.draw.rect(screen, button_color10, (100, 200, 200, 50))
#     button_20_rect = pygame.draw.rect(screen, button_color20, (100, 300, 200, 50))
#     button_30_rect = pygame.draw.rect(screen, button_color30, (100, 400, 200, 50))

#     # Draw text on menu buttons for number of rectangles
#     text_10 = button_font.render("10 Elements", True, TEXT_COLOR)
#     text_20 = button_font.render("20 Elements", True, TEXT_COLOR)
#     text_30 = button_font.render("30 Elements", True, TEXT_COLOR)

#     screen.blit(text_10, (100 + 20, 200 + 10))
#     screen.blit(text_20, (100 + 20, 300 + 10))
#     screen.blit(text_30, (100 + 20, 400 + 10))
#     screen.blit(title_text, (300, 0))
#     screen.blit(instruction_text, (25, 100))

#     # Draw menu buttons for minimum height
#     button_50_min = pygame.draw.rect(screen, button_color50, (400, 200, 200, 50))
#     button_100_min = pygame.draw.rect(screen,button_color100, (400, 300, 200, 50))
#     button_150_min = pygame.draw.rect(screen,button_color150, (400, 400, 200, 50))

#     # Draw text on menu buttons for minimum height
#     text_50_min = button_font.render("50 Min Height", True, TEXT_COLOR)
#     text_100_min = button_font.render("100 Min Height", True, TEXT_COLOR)
#     text_150_min = button_font.render("150 Min Height", True, TEXT_COLOR)

#     screen.blit(text_50_min, (400 + 20, 200 + 10))
#     screen.blit(text_100_min, (400 + 20, 300 + 10))
#     screen.blit(text_150_min, (400 + 20, 400 + 10))

#     # Draw menu buttons for maximum height
#     button_500_max = pygame.draw.rect(screen, button_color500, (700, 200, 200, 50))
#     button_600_max = pygame.draw.rect(screen, button_color600, (700, 300, 200, 50))
#     button_700_max = pygame.draw.rect(screen, button_color700, (700, 400, 200, 50))

#     # Draw text on menu buttons for maximum height
#     text_500_max = button_font.render("500 Max Height", True, TEXT_COLOR)
#     text_600_max = button_font.render("600 Max Height", True, TEXT_COLOR)
#     text_700_max = button_font.render("700 Max Height", True, TEXT_COLOR)

#     screen.blit(text_500_max, (700 + 20, 200 + 10))
#     screen.blit(text_600_max, (700 + 20, 300 + 10))
#     screen.blit(text_700_max, (700 + 20, 400 + 10))

#     pygame.display.flip()

# # Create the screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Sorting Rectangles")

# # Font for displaying text
# font = pygame.font.Font(None, 24)

# # Clock to control the frame rate
# clock = pygame.time.Clock()

# # Main loop
# running = True
# menu_active = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and menu_active:
#             mouse_pos = pygame.mouse.get_pos()

#             # Check number of rectangles buttons
#             if button_10_rect.collidepoint(mouse_pos):
#                 button_color10 = (203, 195, 227)
#                 num_rectangles = 10
#             elif button_20_rect.collidepoint(mouse_pos):
#                 button_color20 = (203, 195, 227)
#                 num_rectangles = 20
#             elif button_30_rect.collidepoint(mouse_pos):
#                 button_color30 = (203, 195, 227)
#                 num_rectangles = 30

#             # Check minimum height buttons
#             elif button_50_min.collidepoint(mouse_pos):
#                 button_color50 = (203, 195, 227)
#                 rectangle_height_min = 50       
#             elif button_100_min.collidepoint(mouse_pos):
#                 button_color100 = (203, 195, 227)
#                 rectangle_height_min = 100
#             elif button_150_min.collidepoint(mouse_pos):
#                 button_color150 = (203, 195, 227)
#                 rectangle_height_min = 150

#             # Check maximum height buttons
#             elif button_500_max.collidepoint(mouse_pos):
#                 rectangle_height_max = 500
#                 button_color500 = (203, 195, 227)
#                 menu_active = False
#                 start_time = pygame.time.get_ticks()
#             elif button_600_max.collidepoint(mouse_pos):
#                 rectangle_height_max = 600
#                 button_color600 = (203, 195, 227)
#                 menu_active = False
#                 start_time = pygame.time.get_ticks()
#             elif button_700_max.collidepoint(mouse_pos):
#                 rectangle_height_max = 700
#                 button_color700 = (203, 195, 227)
#                 menu_active = False
#                 start_time = pygame.time.get_ticks()
#     if menu_active:
#         # Draw the menu screen
#         draw_menu()
#         button_10_rect = pygame.Rect(100, 200, 200, 50)
#         button_20_rect = pygame.Rect(100, 300, 200, 50)
#         button_30_rect = pygame.Rect(100, 400, 200, 50)
#         button_50_min = pygame.Rect(400, 200, 200, 50)
#         button_100_min = pygame.Rect(400, 300, 200, 50)
#         button_150_min = pygame.Rect(400, 400, 200, 50)
#         button_500_max = pygame.Rect(700, 200, 200, 50)
#         button_600_max = pygame.Rect(700, 300, 200, 50)
#         button_700_max = pygame.Rect(700, 400, 200, 50)
#     else:
#         # Draw the sorting screen
#         RECTANGLE_WIDTH = (SCREEN_WIDTH * 0.75) / num_rectangles

#         # Function to generate random heights for rectangles
#         def generate_random_heights(num_rectangles):
#             return [random.randint(rectangle_height_min, rectangle_height_max) for _ in range(num_rectangles)]
#         rectangle_heights = generate_random_heights(num_rectangles)
#         total_time = bubble_sort(rectangle_heights)
#         fptr = open("time.txt", 'w')
#         fptr.write(f"Time it took: {total_time:.2f} seconds")
#         fptr.close()
#         running = False  # Stop the program after one iteration

# # Quit Pygame
# pygame.quit()