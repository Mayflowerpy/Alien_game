import pygame

class Ship():
	"""Класс для управления кораблем"""
	def __init__(self, ai_game):
		"""Инициализирует корабль и задает его начальную позицию"""
		self.screen = ai_game.screen
		# get_rect - присваивание позиции прямоугольника 
		self.screen_rect = ai_game.screen.get_rect()

		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship1.bmp')
		self.rect = self.image.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана
		# midbottom - середина нижней части (600, 800)
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		""" Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect) #Выводит изображение на экран

