import pygame
import random
import os

kunkun_pict=pygame.image.load(os.path.join('pict','kunkun.png')).convert()
gj_pict=pygame.image.load(os.path.join('pict','gj.jpg')).convert()
kaida_pict=pygame.image.load(os.path.join('pict','kaida.png')).convert()
dazhao_pict=pygame.image.load(os.path.join('pict','dazhao.png')).convert()
diren_pict=pygame.image.load(os.path.join('pict','diren.jpg')).convert()
zidan_pict=pygame.image.load(os.path.join('pict','zidan.jpg')).convert()

shoot_sound=pygame.mixer.Sound(os.path.join('sound','ji.mp3'))
start1_sound=pygame.mixer.Sound(os.path.join('sound','heiheihei.mp3'))
start2_sound=pygame.mixer.Sound(os.path.join('sound','lailea.mp3'))
dazhao_sound=pygame.mixer.Sound(os.path.join('sound','zhendetaixunle.mp3'))
jieshu_sound=pygame.mixer.Sound(os.path.join('sound','niganmahahayou.mp3'))


宽=600
长=800


class player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #定义大小
        self.image =pygame.transform.scale(kunkun_pict,(35,50))
        #位置
        self.rect=self.image.get_rect()
        self.rect.center=(宽/2,长-100)
        self.speed=5
        #血量
        self.health=100
    def update(self):
        key_use=pygame.key.get_pressed()
        if key_use[pygame.K_d]:
            self.rect.x+=self.speed
        if key_use[pygame.K_a]:
            self.rect.x-=self.speed
        if key_use[pygame.K_s]:
            self.rect.y+=self.speed
        if key_use[pygame.K_w]:
            self.rect.y-=self.speed
        if self.rect.right>宽:
            self.rect.right=宽
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.bottom>长:
            self.rect.bottom=长
        if self.rect.top<长/4:
            self.rect.top=长/4
    def shoot1(self):
        bu1=bullet1(self.rect.centerx,self.rect.centery)
        all_sprites.add(bu1)
        bull1.add(bu1)
        shoot_sound.play()
    def shoot2(self):
        bu2=bullet2(self.rect.centerx-25,self.rect.centery)
        all_sprites.add(bu2)
        bull2.add(bu2)
        dazhao_sound.play()


class enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #定义大小
        self.wi=40
        self.hi=50
        self.image =pygame.transform.scale(diren_pict,(self.wi,self.hi))
        #位置
        self.rect = self.image.get_rect()
        self.rect.x=random.randint(-100,宽+100)
        self.rect.y=random.randint(-100,-20)
        self.speedy=random.randint(3,4)
        self.speedx=random.randint(-1,1)
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>长 or self.rect.left<0 or self.rect.right>宽:
            self.rect.x = random.randint(-100, 宽 + 100)
            self.rect.y = random.randint(-100, -20)
            self.rect.y += self.speedy
            self.rect.x += self.speedx

class bullet1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #定义大小
        self.image =self.image =pygame.transform.scale(zidan_pict,(20,20))
        #位置
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speedy=-6
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

class bullet2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #定义大小
        self.image = self.image =pygame.transform.scale(dazhao_pict,(50,80))
        #位置
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speedy=-4
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<-200:
            self.kill()



all_sprites=pygame.sprite.Group()
enemys=pygame.sprite.Group()
bull1=pygame.sprite.Group()
bull2=pygame.sprite.Group()
#玩家
player=player1()
all_sprites.add(player)
#敌方
for time in range(7):
    enemys1=enemy1()
    all_sprites.add(enemys1)
    enemys.add(enemys1)












