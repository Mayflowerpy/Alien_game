
#New project "Alien Game"

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()     #Инициализирует настройки игры
        self.settings = Settings()
        
        # Полноэкранный режим:q
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # По указанным размерам:
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # Название окна
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #Отслеживание событий клавиатуры и мыши
            self._check_events()
            self.ship.update() # Обновление позиции корабля
            self._update_bullets()
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
        if event.key == pygame.K_RIGHT:  #K_RIGHT - тут какая клавиша
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed: # Првоерка, что на экране 3 снаряда
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        # Обновление позиции снаряда
        self.bullets.update() # Обновление прорисовки пуль

        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.top <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets)) - Проверка удаления

    def _create_fleet(self):
        """Создание флота пришельцев"""
        # Создание пришельца и вычисление количства пришельцев в ряду
        # Интревал между соседними пришельцами равен ширине пришельца
        # Создание пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        available_space_x = self. settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #Корабль рисуется вызовом этой команды
        # Чтобы пули были нарисованы:
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

