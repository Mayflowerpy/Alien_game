import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""Класс для одной звезды"""

	def __init__(self, ai_game):
		"""Инициализация и нач позиция"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		self.image = pygame.image.load('Images/star1.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		self.y += (self.settings.star_speed * self.settings.starsky_direction)
		self.rect.y = self.y

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.top or self.rect.bottom <= screen_rect.bottom:
			return True