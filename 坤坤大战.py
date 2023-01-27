import pygame
import os
from  time import sleep

ti=0
score=0
panduan=True
宽=600
长=800
fps=60
dadan=10

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((宽,长))
clock=pygame.time.Clock()
pygame.display.set_caption('坤坤大战')

#图片
kunkun_pict=pygame.image.load(os.path.join('pict','kunkun.png')).convert()
gj_pict=pygame.image.load(os.path.join('pict','gj.jpg')).convert()
kaida_pict=pygame.image.load(os.path.join('pict','kaida.png')).convert()
dazhao_pict=pygame.image.load(os.path.join('pict','dazhao.png')).convert()
diren_pict=pygame.image.load(os.path.join('pict','diren.jpg')).convert()
zidan_pict=pygame.image.load(os.path.join('pict','zidan.jpg')).convert()
jieshu_pict=pygame.image.load(os.path.join('pict','jieshu.png')).convert()
#声音
shoot_sound=pygame.mixer.Sound(os.path.join('sound','ji.mp3'))
start1_sound=pygame.mixer.Sound(os.path.join('sound','heiheihei.mp3'))
start2_sound=pygame.mixer.Sound(os.path.join('sound','lailea.mp3'))
dazhao_sound=pygame.mixer.Sound(os.path.join('sound','zhendetaixunle.mp3'))
jieshu_sound=pygame.mixer.Sound(os.path.join('sound','niganmahahayou.mp3'))


from allthings import *

font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,(0,0,0))
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    surf.blit(text_surface,text_rect)

running=True
start1_sound.play()
start2_sound.play()
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot1()
            elif event.key==pygame.K_ESCAPE:
                running=False
            elif event.key==pygame.K_f:
                if dadan>0:
                    player.shoot2()
                    dadan=dadan-1
                else:
                    pass

    #移动
    all_sprites.update()
    bullet1_hit_enemys1=pygame.sprite.groupcollide(enemys,bull1,True,True)
    for hit in bullet1_hit_enemys1:
        enemys1 = enemy1()
        all_sprites.add(enemys1)
        enemys.add(enemys1)
        score=score+10
    bullet2_hit_enemys1 = pygame.sprite.groupcollide(enemys,bull2,True,False)
    for hits in bullet2_hit_enemys1:
        enemys1 = enemy1()
        all_sprites.add(enemys1)
        enemys.add(enemys1)
        score = score + 20
    player_hit_enemy=pygame.sprite.spritecollideany(player,enemys)
    if player_hit_enemy!=None:
        player_hit_enemy.kill()
        enemys1 = enemy1()
        all_sprites.add(enemys1)
        enemys.add(enemys1)
        player.health-=10
        if player.health<=0:
            running=False





    #画面显示
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    draw_text(screen,str(score),18,宽/2,18)
    pygame.display.update()
pygame.quit()









































