#!/usr/bin/env python
from pprint import pprint
import sys
from player import Player
from characters import characters
from character import Character

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty, BooleanProperty, DictProperty

class Game(Widget):
	def __init__(self):
		players = ListProperty([
			Player(1, [
				Character(1, 1, "Phara", characters[1]),
			]),
			Player(2, [
				Character(1, 2, "Op", characters[2]),
			]),
		])
		StringProperty("Setting up game...")
		#self.add_widget(Label(text="Setting up Game.."))
		#self.players = players
		self.is_active = BooleanProperty(True)
		self.turn_count = NumericProperty(0)
	def end(self):
		self.is_active = False
		print "Thanks for playing"
		sys.exit()
	def end_game(self):
		input = raw_input("Are you sure you want to end the game? ")
		if input.find("yes") >= 0 or input.find("confirm") >= 0 or input.find("yeah") >= 0 or input.find("yup") >= 0:
			self.end()
		else:
			return False
	def find_player(self, player_id):
		for p in self.players:
			if p.player_id == player_id:
				return p
	
	def find_targets(self, string):
		result = []
		for p in self.players:
			for c in p.characters:
				if string.find(c.character_name) >= 0:
					result.append(c)
		return result
	
	def find_character(self, character_name):
		for p in self.players:
			character = p.find_character(character_name)
			if character:
				return character
		return False
	def all_characters(self):
		result = []
		for p in self.players:
			for c in p.characters:
				result.append(c)
		return result
		
