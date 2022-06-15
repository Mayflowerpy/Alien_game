import pygame

class Hero():
	"""Класс для управления кораблем"""
	def __init__(self, ai_game):
		"""Инициализирует корабль и задает его начальную позицию"""
		self.screen = ai_game.screen
		# get_rect - присваивание позиции прямоугольника 
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('Images/rocket.png')
		self.rect = self.image.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана
		# midbottom - середина нижней части (600, 800)
		self.rect.center = self.screen_rect.center

		# Сохранение вещественной координаты центра корабля
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Флаг перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_down = False
		self.moving_up = False

	def update(self):
		"""Обновляет позицию корабля с учетом флага"""
		# Обновляется атрибут x, не rect
		# Ограничение хода корабля рамками right and left, чтоыб не выходил за экран
		# Добавленны up and down (Ограничения по top and bottom)
		if self.moving_right and self.rect.right < self.screen_rect.right: 
			self.x += self.settings.hero_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.hero_speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.hero_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.hero_speed


		# обновление атрибута rect на основании self.x
		self.rect.x = self.x 
		self.rect.y = self.y

	def blitme(self):
		""" Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect) #Выводит изображение на экран