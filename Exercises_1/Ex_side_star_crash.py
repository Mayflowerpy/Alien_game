
import sys

import pygame

from setting_ex import Settings
from hero import Hero
from bullet_ex import Bullet
from star import Star
from random import randint
random_number = randint (0, 10)

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()     #Инициализирует настройки игры
        self.settings = Settings()
        
        # Полноэкранный режим:
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.screen_rect = self.screen.get_rect()

        # По указанным размерам:
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # Название окна
        
        self.hero = Hero(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_starsky()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #Отслеживание событий клавиатуры и мыши
            self._check_events()
            self.hero.update() # Обновление позиции корабля
            self._update_bullets()
            self._update_stars()
            #При каждом проходе цикла перерисовывается экран и корабль
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мышки"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  #KEYDOWN - когда клавиша нажата
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        # Клавиши движения
        if event.key == pygame.K_RIGHT:  #K_RIGHT - тут какая клавиша
                self.hero.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.hero.moving_left = True
        elif event.key == pygame.K_DOWN:
                self.hero.moving_down = True
        elif event.key == pygame.K_UP:
                self.hero.moving_up = True

        # Клавиши выстрелов
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        # Клавиша выхода
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.hero.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hero.moving_left = False
        elif event.key == pygame.K_UP:
            self.hero.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.hero.moving_down = False

    def _fire_bullet(self):
        """Создание нвого снаряда и гр"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_bullet_star_collisions()

    def _check_bullet_star_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self. stars, True, True)

        if not self.stars:
            self.bullets.empty()
            self._create_starsky() 

    def _create_starsky(self):
        """Создает сетку из звезд"""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        #Звезд в ряду
        available_space_x = self.settings.screen_width - (25 * star_width)
        number_star = (available_space_x - (5 * star_width)) // (2 * star_width)

        #Рядов
        hero_height = self.hero.rect.height
        available_space_y = (self.settings.screen_height 
        - (star_height) - hero_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_star):
                self._create_star(star_number, row_number)
    
    #def _create_one_row(self):
        """Создает сетку из звезд"""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        #Звезд в ряду
        available_space_x = self.settings.screen_width - 2 * star_width
        number_star = available_space_x // (6 * star_width)

        #Рядов
        hero_height = self.hero.rect.height
        available_space_y = self.settings.screen_height // 6 * star_height

    def _create_star(self, star_number, row_number):
        """Создание звезды и ее размещение"""
        star = Star(self)
        star_width, star_height = star.rect.size
                
        star.x = 27 * star_width + 2 * star_width * star_number 
        star.rect.x = star.x

        star.y = star.rect.height + 2 * star.rect.height * row_number
        star.rect.y = star.y

        self.stars.add(star)

    def _update_stars(self):
        self._check_starsky_edges()
        self.stars.update()

    def _check_starsky_edges(self):
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_starsky_direction()
                break

    def _change_starsky_direction(self):
        """Меняет направление и приближает флот"""
        for star in self.stars.sprites():
            star.rect.x += self.settings.starsky_drop_speed
        self.settings.starsky_direction *= -1

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.hero.blitme() #Корабль рисуется вызовом этой команды
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.stars.draw(self.screen)

        #Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()