import pygame
from pygame.sprite import Group, groupcollide, spritecollide, collide_circle, Sprite
import random, time
from pygame.locals import *
import os

from Bullet import Bullet

from Attributes import Attributes, Colors
w = Attributes["width"]
h = Attributes["height"]
f = Attributes["fps"]

SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
# BACKGROUND_COLOR = pygame.Color('black') #The background color of our window
FPS = 15 #Frames per second



class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []

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

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 530, 80, 80)

        self.rect.centery = h / 2

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        
    
    def animate(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)

            self.images = []
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
            
            self.index = 0
            self.image = self.images[self.index]
            # self.rect = pygame.Rect(0, 530, 80, 80)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

            self.images = []
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
            
            self.index = 0
            self.image = self.images[self.index]
            # self.rect = pygame.Rect(0, 530, 0, 0)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

            self.images = []
            self.images.append(pygame.image.load('templerun/Run__009.png'))
            self.images.append(pygame.image.load('templerun/Run__008.png'))
            self.images.append(pygame.image.load('templerun/Run__007.png'))
            self.images.append(pygame.image.load('templerun/Run__006.png'))
            self.images.append(pygame.image.load('templerun/Run__005.png'))
            self.images.append(pygame.image.load('templerun/Run__004.png'))
            self.images.append(pygame.image.load('templerun/Run__003.png'))
            self.images.append(pygame.image.load('templerun/Run__002.png'))
            self.images.append(pygame.image.load('templerun/Run__001.png'))
            self.images.append(pygame.image.load('templerun/Run__000.png'))
            
            self.index = 0
            self.image = self.images[self.index]
            # self.rect = pygame.Rect(0, 530, 80, 80)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

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
            
            self.index = 0
            self.image = self.images[self.index]
            # self.rect = pygame.Rect(0, 530, 80, 80)

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
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 570:
            self.rect.bottom = 570

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('missile_left.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(820, 900), random.randint(0, 0))
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

class Background(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        
        self.image = pygame.image.load("Background.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.speedx = 10
        
    def update(self):
        
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.left= w

class Background1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        
        self.image = pygame.image.load("Background.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.speedx = 10
        
    def update(self):
        
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.left= w

def shoot(my_sprite):
    bullet = Bullet(my_sprite.rect.right, my_sprite.rect.centery)
    all_sprites.add(bullet)
    bullets.add(bullet)
    shoot_sound.play()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SIZE)

shoot_sound = pygame.mixer.Sound("pew.wav")
hit_sound = pygame.mixer.Sound("expl3.wav")
hit_kill = pygame.mixer.Sound("expl6.wav")
game_over = pygame.mixer.Sound("gameOver.wav")

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)
ADDCLOUD = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCLOUD, 1000)

all_sprites = Group()


bullets = Group()
clouds = Group()
layer = [Background(), Background1()]
all_sprites.add(layer[0], layer[1])
my_sprite = MySprite()
all_sprites.add(my_sprite)
all_sprites.add(bullets)
all_sprites.add(clouds)
enemies = Group()


clock = pygame.time.Clock()
running = True
# =========================================================================================
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # if the Esc key has been pressed set runnin to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                shoot(my_sprite)
                shoot_sound.play
        if event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)

    all_sprites.update()
    # screen.fill(BACKGROUND_COLOR)
    pressed_keys = pygame.key.get_pressed()
    my_sprite.move(pressed_keys)
    my_sprite.animate(pressed_keys)
    all_sprites.draw(screen)
    enemies.update()
    bullets.update()
    clouds.update()
    
    pygame.display.update()
    clock.tick(15)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollide(my_sprite, enemies, True, False):
        # enemies.remove()
        # game_over.play()
        # pygame.mixer.music.load('gameOver.wav')
        # pygame.mixer.music.set_volume(1)
        # pygame.mixer.music.play(loops=-1)
        hit_sound.play()        

    hits = groupcollide(bullets, enemies, False, True)

    for hit_bullet in hits:
        bullets.remove(hit_bullet)
        hit_kill.play()




    '''
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
'''