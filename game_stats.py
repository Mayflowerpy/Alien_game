import json

class GameStats():
	"""Отслеживание статистики игры"""

	def __init__(self, ai_game):
		"""Инициалищирует статистику"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False

		# Рекорд не должен сбрасываться
		filename = 'record.json'
		with open(filename) as f:
			self.high_score = json.load(f)


	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры"""
		# self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		self.ships_life = self.settings.ship_limit
		self.aliens_crash = self.settings.count_aliens_crash
		self.ship_crash = self.settings.count_ship_crash