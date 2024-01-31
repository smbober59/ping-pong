from pygame import *

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <  win_height-155:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <  win_height-155:
            self.rect.y += self.speed

bek = (154,20,212)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(bek)

raket1 = Player('Frame 2.png', 30,200,4,50,150)
raket2 = Player('Frame 2.png', 520,200,4,50,150)
boll = GameSprite('Frame 1.png', 200,200,4,50,50)

font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!',True, (205,58,58))
lose2 = font.render('PLAYER 2 LOSE!', True, (205,58,58))

speedx = 3
speedy  =3

finish = False
game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    if finish != True:
        window.fill(bek)
        raket1.update_l()
        raket2.update_r()
        
        boll.rect.x += speedx
        boll.rect.y += speedy

        if sprite.collide_rect(raket1,boll) or sprite.collide_rect(raket2,boll):
            speedx *= -1

        if boll.rect.y <0 or boll.rect.y > win_height-50:
            speedy *= -1 

        if boll.rect.x < 0:
            finish = True 
            window.blit(lose1,(200,200)) 

        if boll.rect.x > win_width-50:
            finish = True
            window.blit(lose2,(200,200))
        
        raket1.reset()
        raket2.reset()
        boll.reset()
    display.update()
    clock.tick(FPS)
