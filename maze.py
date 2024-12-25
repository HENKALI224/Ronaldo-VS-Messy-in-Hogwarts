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
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += 10
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += 10
        




player1 = Player('messy.png',0,100,3,80,150)
player2 = Player('ronaldo.png',620,100,3,80,150)
ball = GameSprite('nuclear-bomb-04.png',250,350,1,75,50)

font = font.SysFont('Arial',70)
winer1 = font.render('Player 1 wins',True,(255,215,0))
winer2 = font.render('Player 2 wins',True,(255,0,0))
clock = time.Clock()
finish = False
game = True
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.blit(background,(0,0))
        player1.update_left()
        player1.reset()
        player2.update_right()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.x >= 650:
            finish = True          
            mw.blit(winer1,(200,200))
        if ball.rect.x <= 0:
            finish = True
            mw.blit(winer2,(200,200))



    
    
    clock.tick(60)
    display.update()
