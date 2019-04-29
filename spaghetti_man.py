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

# SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
# BACKGROUND_COLOR = pygame.Color('black') #The background color of our window
# FPS = 60 #Frames per second



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

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 480, 80, 80)

        self.health = 10

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        
    
    def animate(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)

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
            self.rect.move_ip(0, 10)

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
            self.rect.move_ip(-10, 0)

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
            self.rect.move_ip(10, 0)

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
            center=(random.randint(920, 921), random.randint(0, 600))
        )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.image = pygame.image.load('pizza cat.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(920, 921), random.randint(0, 600))
        )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy3, self).__init__()

        self.images = []

        
        self.images.append(pygame.image.load('Zombie/Walk1.png'))
        self.images.append(pygame.image.load('Zombie/Walk1.png'))
        self.images.append(pygame.image.load('Zombie/Walk1.png'))
        self.images.append(pygame.image.load('Zombie/Walk2.png'))
        self.images.append(pygame.image.load('Zombie/Walk2.png'))
        self.images.append(pygame.image.load('Zombie/Walk2.png'))
        self.images.append(pygame.image.load('Zombie/Walk3.png'))
        self.images.append(pygame.image.load('Zombie/Walk3.png'))
        self.images.append(pygame.image.load('Zombie/Walk3.png'))
        self.images.append(pygame.image.load('Zombie/Walk4.png'))
        self.images.append(pygame.image.load('Zombie/Walk4.png'))
        self.images.append(pygame.image.load('Zombie/Walk4.png'))
        self.images.append(pygame.image.load('Zombie/Walk5.png'))
        self.images.append(pygame.image.load('Zombie/Walk5.png'))
        self.images.append(pygame.image.load('Zombie/Walk5.png'))
        self.images.append(pygame.image.load('Zombie/Walk6.png'))
        self.images.append(pygame.image.load('Zombie/Walk6.png'))
        self.images.append(pygame.image.load('Zombie/Walk6.png'))
        self.images.append(pygame.image.load('Zombie/Run1.png'))
        self.images.append(pygame.image.load('Zombie/Run1.png'))
        self.images.append(pygame.image.load('Zombie/Run1.png'))
        self.images.append(pygame.image.load('Zombie/Run2.png'))
        self.images.append(pygame.image.load('Zombie/Run2.png'))
        self.images.append(pygame.image.load('Zombie/Run2.png'))
        self.images.append(pygame.image.load('Zombie/Run3.png'))
        self.images.append(pygame.image.load('Zombie/Run3.png'))
        self.images.append(pygame.image.load('Zombie/Run3.png'))
        self.images.append(pygame.image.load('Zombie/Run4.png'))
        self.images.append(pygame.image.load('Zombie/Run4.png'))
        self.images.append(pygame.image.load('Zombie/Run4.png'))
        self.images.append(pygame.image.load('Zombie/Run5.png'))
        self.images.append(pygame.image.load('Zombie/Run5.png'))
        self.images.append(pygame.image.load('Zombie/Run5.png'))
        self.images.append(pygame.image.load('Zombie/Run6.png'))
        self.images.append(pygame.image.load('Zombie/Run6.png'))
        self.images.append(pygame.image.load('Zombie/Run6.png'))
        self.images.append(pygame.image.load('Zombie/Run7.png'))
        self.images.append(pygame.image.load('Zombie/Run7.png'))
        self.images.append(pygame.image.load('Zombie/Run7.png'))
        self.images.append(pygame.image.load('Zombie/Run8.png'))
        self.images.append(pygame.image.load('Zombie/Run8.png'))
        self.images.append(pygame.image.load('Zombie/Run8.png'))
        self.images.append(pygame.image.load('Zombie/Run9.png'))
        self.images.append(pygame.image.load('Zombie/Run9.png'))
        self.images.append(pygame.image.load('Zombie/Run9.png'))
        self.images.append(pygame.image.load('Zombie/Run10.png'))
        self.images.append(pygame.image.load('Zombie/Run10.png'))
        self.images.append(pygame.image.load('Zombie/Run10.png'))
        

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(930, 480, 80, 80)

        
        self.speed = random.randint(5,10)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]

        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(920, 921), random.randint(0, 0))
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
        self.rect.left = w
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
# sound = pygame.mixer.Sound('humps.wav')
screen = pygame.display.set_mode((w, h))

shoot_sound = pygame.mixer.Sound("pew.wav")
hit_sound = pygame.mixer.Sound("expl3.wav")
hit_kill = pygame.mixer.Sound("expl6.wav")
game_over = pygame.mixer.Sound("gameOver.wav")

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)
ADDCLOUD = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCLOUD, 1000)
ADDENEMY2 = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY2, 1000)
ADDENEMY3 = pygame.USEREVENT + 4
pygame.time.set_timer(ADDENEMY3, 1000)

all_sprites = Group()


layer = [Background(), Background1()]
all_sprites.add(layer[0], layer[1])
bullets = Group()
clouds = Group()
enemies = Group()
my_sprite = MySprite()
all_sprites.add(my_sprite)
all_sprites.add(bullets)
all_sprites.add(clouds)
all_sprites.add(enemies)


clock = pygame.time.Clock()
running = True
# =========================================================================================
while running:
    clock.tick(f)
    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # if the Esc key has been pressed set runnin to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                shoot(my_sprite)
                shoot_sound.play()
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
        elif event.type == ADDENEMY2:
            new_enemy2 = Enemy2()
            enemies.add(new_enemy2)
            all_sprites.add(new_enemy2)
        elif event.type == ADDENEMY3:
            new_enemy3 = Enemy3()
            enemies.add(new_enemy3)
            all_sprites.add(new_enemy3)

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
    
    if pygame.sprite.spritecollide(my_sprite, enemies, True, False):
        # enemies.remove()
        # game_over.play()
        # pygame.mixer.music.load('gameOver.wav')
        # pygame.mixer.music.set_volume(1)
        # pygame.mixer.music.play(loops=-1)
        hit_sound.play()       
        my_sprite.health -= 1
    # damage_hits = spritecollide(my_sprite, enemies, True, False)
    
    if my_sprite.health == 0:
    #     my_sprite.images = []
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__000.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__001.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__002.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__003.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__004.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__005.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__006.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__007.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__008.png'))
    #     my_sprite.images.append(pygame.image.load('templerun/Dead__009.png'))

    #     my_sprite.index = 0
    #     my_sprite.image = my_sprite.images[my_sprite.index]

    #     def update(my_sprite):
    #         my_sprite.index += 1

    #         if my_sprite.index >= len(my_sprite.images):
    #             my_sprite.index = 0
            
    #         my_sprite.image = my_sprite.images[my_sprite.index]
        my_sprite.kill()
        my_sprite.remove()


    hits = groupcollide(bullets, enemies, False, True)

    for hit_bullet in hits:
        bullets.remove(hit_bullet)
        hit_kill.play()


    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    screen.fill(Colors["black"]) 
    # screen.blit(background, background_rect) 
    all_sprites.draw(screen)

    pygame.display.flip()

    '''
    
'''