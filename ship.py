import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Класс для управления кораблем"""
	def __init__(self, ai_game):
		"""Инициализирует корабль и задает его начальную позицию"""
		super().__init__()
		self.screen = ai_game.screen
		# get_rect - присваивание позиции прямоугольника 
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship1.bmp')
		self.rect = self.image.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана
		# midbottom - середина нижней части (600, 800)
		self.rect.midbottom = self.screen_rect.midbottom

		# Сохранение вещественной координаты центра корабля
		self.x = float(self.rect.x)

		# Флаг перемещения
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию корабля с учетом флага"""
		# Обновляется атрибут x, не rect
		# Ограничение хода корабля рамками right and left, чтоыб не выходил за экран
		if self.moving_right and self.rect.right < self.screen_rect.right: 
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.ship_speed

		# обновление атрибута rect на основании self.x
		self.rect.x = self.x

	def blitme(self):
		""" Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect) #Выводит изображение на экран

	def center_ship(self):
		"""Размещает корабль в центре нижней стороны"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

