import pygame
import random
from random import randint
pygame.init()

def game_1111():
    pygame.mixer.music.load("krushgirl.mp3")
    pygame.mixer.music.play()
    print('Управління:\nW-Вгору\nA-Вліво\nS-Вниз\nD-Праворуч\nR-Стріляти') #Підказка в управлінні
    vorog = int(input("Введи кількість ворогів,писати тільки число:"))
    back = (29,219,13)
    window = pygame.display.set_mode((600,600))


    start_x = 0
    start_y = 0
    count = 4

    class Area():
        def __init__(self, x=0, y=0, width =10, height =10, color=None):
            self.rect = pygame.Rect(x, y, width, height)
            self.fill_color = back
            if color:
                self.fill_color = color

        def color(self, new_color):
            self.fill_color = new_color

        def fill(self):
            pygame.draw.rect(window,self.fill_color,self.rect)
        def collidepoint(self, x, y):
            return self.rect.collidepoint(x, y)
        def colliderect(self, rect):
                return self.rect.colliderect(rect)

    class Picture(Area):
        def __init__(self, filename, x=0, y=0, width =10, height =10):
            Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
            self.image = pygame.image.load(filename)
    
        def draw(self):
            window.blit(self.image, (self.rect.x,self.rect.y))

    class Bullet(Area):
        def __init__(self, x, y):
            super().__init__(x, y, 5, 10, (255, 0, 30))
            self.speed = 10
        # функція, яка реалізує постійний рух пуль
        def move(self):
            self.rect.y -= self.speed

    class Bullet1(Area):
        def __init__(self, x, y):
            super().__init__(x, y, 5, 10, (205, 0, 30))
            self.speed1 = 10
        # функція, яка реалізує постійний рух пуль
        def move(self):
            self.rect.y += self.speed1

    enemy = Picture('horish.png',200,350,40,40)

    move_r = False
    move_l = False
    move_u = False
    move_d = False
    clock = pygame.time.Clock() #Потрібне для оновлення єкрану

    healths = [] #Здоров'є
    for h in range(3):
        x = 50 * h
        y = 350
        health = Picture('serdechko.png',x,y,50,50)
        healths.append(health)
        health.fill()

    plohishs = [] #Противники
    for b in range(vorog):
        x = random.randint(100,350)
        y = 20
        plohish = Picture('plohish.png',x,y,50,50)
        plohishs.append(plohish)
        plohish.speed = random.randint(1, 5) 
        plohishs.append(plohish) 
        


    bullets = []
    bullets1 = []

    game = True #Означає що гра запущена
    while game: #Цикл гри
        enemy.fill() #Заповнює форму гравця


            
        
        for bullet in bullets: 
            bullet.fill() #Малює пулю
            bullet.move() #Заставляє рухатись пулю в напрямку вистрілу
            if bullet.rect.y >= 450: #Видаляє з невидимої частини поля
                bullets.remove(bullet)
        
        for bullet1 in bullets1:
            bullet1.fill() #Малює пулю
            bullet1.move() #Заставляє рухатись пулю в напрямку вистрілу
            if bullet1.rect.y <= 0: #Видаляє з невидимої частини поля
                bullets1.remove(bullet1)
        
    
        #Як що клавіша натиснута то робить свою дію
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_d:
                    move_r = True
                if e.key == pygame.K_a:
                    move_l = True
                if e.key == pygame.K_w:
                    move_u = True
                if e.key == pygame.K_s:
                    move_d = True
                if e.key == pygame.K_r: #Відповідає за вистріли персонажа
                    sound = pygame.mixer.Sound("sss.mp3")
                    sound.play()
                    x = enemy.rect.x + enemy.rect.width // 2 - 2
                    y = enemy.rect.y
                    bullet = Bullet(x, y)
                    bullets.append(bullet)

                    #Відповідає за те що коли піднята клавіша то рух зупиняється
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_d:
                    move_r = False
                if e.key == pygame.K_a:
                    move_l = False
                if e.key == pygame.K_w:
                    move_u = False
                if e.key == pygame.K_s:
                    move_d = False

                    #Відповідає за частоту вистрілів противника 
        for b in plohishs:
            if randint(0,200) < 1:
                x = b.rect.x + b.rect.width // 2 - 2
                y = b.rect.y
                bullet1 = Bullet1(x, y)
                bullets1.append(bullet1)

        #Відповідає за рух

        if move_r:
            enemy.rect.x += 10
        if move_l:
            enemy.rect.x -= 10
        if move_u:
            enemy.rect.y -= 10
        if move_d:
            enemy.rect.y += 10


        #1,2,3,4 Перевіряють чи дійшов ворог до певних координат 
            
        if enemy.rect.x <= 0:      #1
            game = False
        if enemy.rect.x >= 450:    #2
            game = False
        if enemy.rect.y <= 250:    #3
            move_u = False
        if enemy.rect.y >= 420:    #4
            move_d = False

        

        window.fill(back)
        for i in plohishs:
            i.draw()
            if i.rect.colliderect(enemy.rect):
                plohishs.remove(i)
                i.fill()
        window.fill(back)
        enemy.draw()
        

        for plohish in plohishs:
            plohish.draw()
                
        for bullet in bullets: 
            bullet.move()
            bullet.fill()
        for bullet1 in bullets1:
            bullet1.move()
            bullet1.fill()
        
        

        for plohish in plohishs: #Цей код потрібен для перевірки того що пуля достигла цілі і пуля та ворог видаляться 
            for bullet in bullets:
                if bullet.rect.colliderect(plohish.rect):
                    bullets.remove(bullet)
                    plohishs.remove(plohish)
        


        for plohish in plohishs:
            plohish.rect.x += plohish.speed
            # Перевірка, чи ворог дійшов до кінця вікна
            if plohish.rect.x < 0:
                plohish.rect.x = 0
                plohish.speed = -plohish.speed  # Зміна напрямку руху
            if plohish.rect.x > 500 - plohish.rect.width:
                plohish.rect.x = 500 - plohish.rect.width
                plohish.speed = -plohish.speed  # Зміна напрямку руху
        
        enemy.draw()

        for bullet1 in bullets1:
            if bullet1.rect.colliderect(enemy.rect):
                bullets1.remove(bullet1)
                if len(healths) > 0:
                    healths.pop()
                    pygame.display.update()
                elif len(healths) == 0: #Як що здоров'я буде 0 то гра закінчиться
                    window.fill(back)
                    pygame.display.update()
                    pygame.time.delay(1000) #Час через який зупиниться гра 
                    game = False
        
        for h in healths:  #Малювання здоровья
                h.fill()
                h.draw()
        pygame.display.update() #Оновлення єкрану
        clock.tick(50) #Частота кадрів