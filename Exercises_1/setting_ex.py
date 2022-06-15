
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (10, 10, 100)

        #Настройки корабля
        self.hero_speed = 1.5

        # Настройки пришельца
        self.star_speed = 1
        self.starsky_drop_speed = 0.1
        self.starsky_direction = -1

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_height = 70
        self.bullet_width = 5
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3