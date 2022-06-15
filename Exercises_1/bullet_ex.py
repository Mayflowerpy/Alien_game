import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midright = ai_game.hero.rect.midright

		self.x = float(self.rect.x)

	def update(self):
		self.x += self.settings.bullet_speed
		self.rect.x = self.x

	def draw_bullet(self):
		"""Вывод снаряда на экран"""
		pygame.draw.rect(self.screen, self.color, self. rect)