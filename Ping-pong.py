from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

window = display.set_mode((600, 500))
window.fill((255, 255, 255))
clock = time.Clock()
game = True
finish = False
ball = GameSprite('tenis_ball.png', 250, 250, 5, (50,50))
Player1 = Player('racket.png', 5, 150, 5, (50,150))
Player2 = Player('racket.png', 550, 150, 5, (50,150))

speed_x = 7
speed_y = 7
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((255, 255, 255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        Player1.reset()
        Player1.update_l()
        Player2.reset()
        Player2.update_r()
        ball.reset()
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(Player1, ball) or sprite.collide_rect(Player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > 550:
        finish = True
        window.blit(lose2, (200,200))

    display.update()
    clock.tick(60) 
    


