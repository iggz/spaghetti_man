import pygame
import random, time
from pygame.locals import *



SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 30 #Frames per second

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('templerun/Run__000.png'))
        self.images.append(pygame.image.load('templerun/Run__001.png'))
        self.images.append(pygame.image.load('templerun/Run__002.png'))
        self.images.append(pygame.image.load('templerun/Run__003.png'))
        self.images.append(pygame.image.load('templerun/Run__004.png'))
        self.images.append(pygame.image.load('templerun/Run__005.png'))
        self.images.append(pygame.image.load('templerun/Run__006.png'))
        self.images.append(pygame.image.load('templerun/Run__007.png'))
        self.images.append(pygame.image.load('templerun/Run__008.png'))
        self.images.append(pygame.image.load('templerun/Run__009.png'))

        self.images.append(pygame.image.load('templerun/Jump__000.png'))
        self.images.append(pygame.image.load('templerun/Jump__001.png'))
        self.images.append(pygame.image.load('templerun/Jump__002.png'))
        self.images.append(pygame.image.load('templerun/Jump__003.png'))
        self.images.append(pygame.image.load('templerun/Jump__004.png'))
        self.images.append(pygame.image.load('templerun/Jump__005.png'))
        self.images.append(pygame.image.load('templerun/Jump__006.png'))
        self.images.append(pygame.image.load('templerun/Jump__007.png'))
        self.images.append(pygame.image.load('templerun/Jump__008.png'))
        self.images.append(pygame.image.load('templerun/Jump__009.png'))

        self.images.append(pygame.image.load('templerun/Slide__000.png'))
        self.images.append(pygame.image.load('templerun/Slide__001.png'))
        self.images.append(pygame.image.load('templerun/Slide__002.png'))
        self.images.append(pygame.image.load('templerun/Slide__003.png'))
        self.images.append(pygame.image.load('templerun/Slide__004.png'))
        self.images.append(pygame.image.load('templerun/Slide__005.png'))
        self.images.append(pygame.image.load('templerun/Slide__006.png'))
        self.images.append(pygame.image.load('templerun/Slide__007.png'))
        self.images.append(pygame.image.load('templerun/Slide__008.png'))
        self.images.append(pygame.image.load('templerun/Slide__009.png'))

        self.images.append(pygame.image.load('templerun/Idle__000.png'))
        self.images.append(pygame.image.load('templerun/Idle__001.png'))
        self.images.append(pygame.image.load('templerun/Idle__002.png'))
        self.images.append(pygame.image.load('templerun/Idle__003.png'))
        self.images.append(pygame.image.load('templerun/Idle__004.png'))
        self.images.append(pygame.image.load('templerun/Idle__005.png'))
        self.images.append(pygame.image.load('templerun/Idle__006.png'))
        self.images.append(pygame.image.load('templerun/Idle__007.png'))
        self.images.append(pygame.image.load('templerun/Idle__008.png'))
        self.images.append(pygame.image.load('templerun/Idle__009.png'))

        self.images.append(pygame.image.load('templerun/Dead__000.png'))
        self.images.append(pygame.image.load('templerun/Dead__001.png'))
        self.images.append(pygame.image.load('templerun/Dead__002.png'))
        self.images.append(pygame.image.load('templerun/Dead__003.png'))
        self.images.append(pygame.image.load('templerun/Dead__004.png'))
        self.images.append(pygame.image.load('templerun/Dead__005.png'))
        self.images.append(pygame.image.load('templerun/Dead__006.png'))
        self.images.append(pygame.image.load('templerun/Dead__007.png'))
        self.images.append(pygame.image.load('templerun/Dead__008.png'))
        self.images.append(pygame.image.load('templerun/Dead__009.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(0, 530, 80, 80)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
    
    def move(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 400:
            self.rect.top = 400
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # if the Esc key has been pressed set runnin to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        pressed_keys = pygame.key.get_pressed()
        my_sprite.move(pressed_keys)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    main()