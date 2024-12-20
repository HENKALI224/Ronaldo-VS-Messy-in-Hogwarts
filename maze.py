#создай игру "Лабиринт"!
from pygame import *
mixer.init()
font.init()
#создай окно игры
mw = display.set_mode((700,500))
display.set_caption('Ping Pong')
#задай фон сцены
background = transform.scale(image.load('fightPlace.jpg'),(700, 500))
mw.blit(background,(0,0))
mixer.music.load('Music.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
kick = mixer.Sound('udar.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += 10
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += 10
        




player1 = Player('messy.png',50,100,3,80,150)
player2 = Player('ronaldo.png',100,100,3,80,150)

font = font.SysFont('Arial',70)
winer = font.render('TO BE CONTINUED',True,(255,215,0))
lose = font.render('TO BE CONTINUED',True,(255,0,0))
clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.blit(background,(0,0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        
        

    
    
    clock.tick(60)
    display.update()