from pygame import *
from random import randint

img_back = "img_back.png"
img_hero = "Player.png"
img_ball = "ball.png"
#шрифты и надписи
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
win = font1.render("YOU WIN!", True, (255, 255, 255))

lose1 = font1.render("PLAYER 1 LOSE", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE", True, (180, 0, 0))

speed_x = 3
speed_y = 3
score1 = 0
score2 = 0

class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)




       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed




       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))




#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed
#Создаём окошко
win_width = 700
win_height = 500
display.set_caption("Ping_pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("img_back.png"), (win_width, win_height))




#создаём спрайты
racket1 = Player(img_hero, 10, 250, 80, 100, 10)
racket2 = Player(img_hero, 600, 250, 80, 100, 10)
ball = GameSprite(img_ball, 350, 250, 80, 100, 10)
finish = False
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:

        window.blit(background,(0,0))

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:  
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1.001
            speed_y *= 1.001

        if ball.rect.x < 0:
            score2 = score2 + 1
            ball.rect.x = (350)
            ball.rect.y = (250)

        if ball.rect.x > 700:
            score1 = score1 + 1
            ball.rect.x = (350)
            ball.rect.y = (250)

        if score1 >= 5:
            finish = True
            window.blit(lose2, (200, 200))
        if score2 >= 5:
           finish = True
           window.blit(lose2, (200, 200))

        text1 = font2.render(str(score1), 1, (255, 255, 255))
        window.blit(text1, (330, 250 ))
        text2 = font2.render(str(score2), 1, (255, 255, 255))
        window.blit(text2, (370, 250))



        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    #цикл срабатывает каждую 0.05 секунд
    time.delay(50)