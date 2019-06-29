import pygame
import sys
import traceback
import myplane
import enemy
from pygame.locals import *
from random import *
pygame.init()
pygame.mixer.init()

bg_size = width,height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('期末作业————————飞机大战')

background = pygame.image.load('images/background.png').convert()

#载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2 = enemy.SmallEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3 = enemy.SmallEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)
def main():
    pygame.mixer_music.play(-1)
    #生成我方飞机
    me = myplane.MyPlane(bg_size)
    #生成敌方飞机，大。中。小共三类
    enemies = pygame.sprite.Group()

    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)

    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)

    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)

    clock = pygame.time.Clock()
    #用于切换图片
    switch_image = True
    #用于延迟
    delay = 100
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #检测用户键盘操作
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()


        screen.blit(background,(0,0))
        #绘制敌方大型飞机
        for each in big_enemies:
            each.move()
            if switch_image:
                screen.bilt(each.image1,each.rect)
            else:
                screen.bilt(each.image2, each.rect)
        # 绘制敌方中型飞机
        for each in mid_enemies:
            each.move()
            screen.bilt(each.image, each.rect)
        # 绘制敌方中型飞机
        for each in small_enemies:
            each.move()
            screen.bilt(each.image, each.rect)
        #当大型飞机出现时，播放音效
        if each.rect.bottom > -50:
            enemy3_fly_sound.play()

        #绘制我的飞机

        if switch_image:
            screen.blit(me.image1,me.rect)
        else:
            screen.blit(me.image2,me.rect)
        #切换图片，60帧，一秒切换12次
        if not (delay % 5):
            switch_image = not switch_image

        delay -=1
        if not delay:
            delay = 100
            
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()