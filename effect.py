#!/usr/bin/env python

effects = [
	{
		"id": "fire",
		"name": "Fire",
		"cost": 2,
		"set": {
			
		},
		"activate": {
			"health": {
				"direction": "-",
				"value": 1
			},
		},
		"action": {
			
		},
		"finish": {
			
		},
		"unset": {
			
		},
	}
]

class Effect(object):
	def __init__(self, effect, character):
		self.data = effect
		self.id = effect["id"]
		self.name = effect["name"]
		self.set = effect["set"]
		self.activate = effect["activate"]
		self.action = effect["action"]
		self.finish = effect["finish"]
		self.unset = effect["unset"]
		self.character = character
		
		self.run_set()
	
	def run_set(self):
		for stat in self.set:
			if self.set[stat]["direction"] == "-":
				character_stat = getattr(self.character, stat) - self.set[stat]["value"]
			elif self.activate[stat]["direction"] == "+":
				character_stat = getattr(self.character, stat) + self.set[stat]["value"]
			setattr(self.character, stat, character_stat)
			
		self.character.check_conditions()
	
	def run_activate(self):
		for stat in self.activate:
			if self.activate[stat]["direction"] == "-":
				character_stat = getattr(self.character, stat) - self.activate[stat]["value"]
			elif self.activate[stat]["direction"] == "+":
				character_stat = getattr(self.character, stat) + self.activate[stat]["value"]
			setattr(self.character, stat, character_stat)
			
		self.character.check_conditions()
	
	def run_finish(self):
		for stat in self.finish:
			if self.finish[stat]["direction"] == "-":
				character_stat = getattr(self.character, stat) - self.finish[stat]["value"]
			elif self.activate[stat]["direction"] == "+":
				character_stat = getattr(self.character, stat) + self.finish[stat]["value"]
			setattr(self.character, stat, character_stat)
			
		self.character.check_conditions()
	
	def run_unset(self):
		for stat in self.unset:
			if self.unset[stat]["direction"] == "-":
				character_stat = getattr(self.character, stat) - self.unset[stat]["value"]
			elif self.activate[stat]["direction"] == "+":
				character_stat = getattr(self.character, stat) + self.unset[stat]["value"]
			setattr(self.character, stat, character_stat)
			
		self.character.check_conditions()
	
	
	