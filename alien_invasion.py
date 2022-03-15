
#New project "Alien Game"

import sys

import pygame

from settings import Settings
from ship import Ship

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

        # По указанным размерам:
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # Название окна
        
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #Отслеживание событий клавиатуры и мыши
            self._check_events()
            self.ship.update() # Обновление позиции корабля
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
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            
            self.ship.moving_left = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #Корабль рисуется вызовом этой команды

        #Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

