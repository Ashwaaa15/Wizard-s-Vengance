import pygame
import random
import sys
pygame.init()

screen_width=1000
screen_height=500

score = 0
player_lives=4
font = pygame.font.Font(None,36)


backgroudn_image=pygame.image.load("assets/background.png")
backgroudn_image=pygame.transform.scale(backgroudn_image,(screen_width,screen_height))
bg_x=0
speed_increase_rate=0

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Realm quest")
enemies=[]

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img=pygame.image.load("assets/player1.png")
        self.img=pygame.transform.scale(self.img,(100,100))
        self.rect=self.img.get_rect()
        self.rect.center=(x,y)
        self.run_animation_count=0
        self.img_list=["assets/player1.png","assets/player2.png","assets/player3.png","assets/player4.png"]
        self.is_jump=False
        self.jump_count=15
    def draw(self):
        self.rect.center=(self.x,self.y)
        screen.blit(self.img,self.rect)
    def run_animation_player(self):
        if(not self.is_jump):
            self.img=pygame.image.load(self.img_list[int(self.run_animation_count)])
            self.img=pygame.transform.scale(self.img,(100,100))
            self.run_animation_count+=0.5
            self.run_animation_count=self.run_animation_count%4
    def jump(self):
        if(self.jump_count>-15):
            n=1
            if(self.jump_count<0):
                n=-1
            self.y-=((self.jump_count**2)/10)*n
            self.jump_count-=1
        else:
            self.is_jump=False  
            self.jump_count=15
            self.y=386       

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img=pygame.image.load("assets/enemy1.png")
        self.img=pygame.transform.scale(self.img,(75,75))
        self.rect=self.img.get_rect()
        self.rect.center=(x,y)
        self.run_animation_count=0
        self.img_list=["assets/enemy1.png","assets/enemy2.png","assets/enemy3.png"]
    def draw(self):
        self.rect.center=(self.x,self.y)
        screen.blit(self.img,self.rect)
    def run_animation_enemy(self):
        self.img=pygame.image.load(self.img_list[int(self.run_animation_count)])
        self.img=pygame.transform.scale(self.img,(75,75))
        self.run_animation_count+=0.5
        self.run_animation_count=self.run_animation_count%3

player=Character(100,386)
running = True
clock = pygame.time.Clock()

last_enemy_spawn_time=pygame.time.get_ticks()


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.is_jump=True
    bg_x-=(10+speed_increase_rate)
    speed_increase_rate+=0.005
    if bg_x<=-screen_width:
        bg_x=0
    screen.blit(backgroudn_image,(bg_x,0))
    screen.blit(backgroudn_image,(screen_width+bg_x,0))

    current_time=pygame.time.get_ticks()
    if current_time-last_enemy_spawn_time>=3000:
        if random.randint(0,100)<3:
            enemy_x=screen_width+900
            enemy_y=396
            enemy=Enemy(enemy_x,enemy_y)
            enemies.append(enemy)
            last_enemy_spawn_time=current_time

    for enemy in enemies:
        enemy.x-=(15+speed_increase_rate)
        enemy.draw()
        enemy.run_animation_enemy()        
        
    if(player.is_jump):
        player.jump()
    player.draw()   
    player.run_animation_player()
    pygame.display.update()
    clock.tick(30)

pygame.quit()