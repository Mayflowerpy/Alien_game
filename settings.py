
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)

        # Настройки корабля
        self.ship_speed = 2.0
        self.ship_limit = 3

        # Настройки пришельца
        self.alien_speed = 0.6
        self.fleet_drop_speed = 30
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = -1

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3  #было 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255) # Цвет
        self.bullets_allowed = 3 # Максимальное кол-ва пуль на экране

        # Счетчик попаданий
        self.count_aliens_crash = 0
        self.count_ship_crash = 0

        # Темп ускорения игры
        self.speedup_scale = 10
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализируют настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # Подсчет очков
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо, -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)