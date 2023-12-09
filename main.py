import pygame
from src.sample_controller import Controller

#import your controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()

if __name__ == '__main__':
    main()
