#!/usr/bin/env python
from pprint import pprint

class Game(object):
	def __init__(self, players):
		self.players = players
		self.is_active = True;
	def end(self):
		self.is_active = False;
	def find_player(self, player_id):
		for p in self.players:
			if p.player_id == player_id:
				return p
		
