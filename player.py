#!/usr/bin/env python
class Player(object):
	def __init__(self, player_id, characters):
		self.player_id = player_id
		self.characters = characters
	def find_character(self, character_name):
		for c in self.characters:
			if c.character_name == character_name:
				return c
