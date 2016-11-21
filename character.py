#!/usr/bin/env python
from pprint import pprint
from random import randint

class Character(object):
	def __init__(self, id, character_id, character_name, stats):
		self.id = id
		self.character_id = character_id
		self.character_name = character_name
		
		self.kill_count = 0
		self.hit_count = 0
		self.miss_count = 0
		self.dodge_count = 0
		self.activate_count = 0
		
		self.health = stats["max-health"]
		self.max_health = stats["max-health"]
		self.move = stats["move"]
		self.actions = stats["actions"]
		self.attacks = stats["attacks"]
		self.abilities = stats["abilities"]
		self.type = stats["type"]
		self.faction = stats["faction"]
		self.immune = stats["immune"]
		self.dodge = stats["dodge"]
		self.armor = stats["armor"]
		
		self.new_condition = False;
		self.conditions = stats["conditions"]
		
		self.effects = []
		
		
	def find_action(self, action_string):
		for a in self.attacks:
			if action_string.find(self.attacks[a]["name"]) >= 0:
				return self.attacks[a]
		
		for a in self.abilities:
			if action_string.find(self.abilities[a]["name"]) >= 0:
				return self.abilities[a]
		return False
		
	def is_valid_action(self, action_name):
		for a in self.attacks:
			if self.attacks[a]["name"] == action_name and self.attacks[a]["status"] == "active":
				return self.attacks[a]
		
		for a in self.abilities:
			if self.abilities[a]["name"] == action_name and self.abilities[a]["status"] == "active":
				return self.abilities[a]
			
		return False
	def defend(self, attack, modifiers):
		if randint(0,100) >= (int(self.dodge) - int(modifiers["accuracy"])):
			print "Hit"
			attack = attack - int(self.armor)
			if len(modifiers["effects"]) >= 1:
				for effect in modifiers["effects"]:
					self.set_effect(effect)
			if attack >= 0:
				self.health = self.health - attack
			if self.health <= 0:
				self.die()
				result = "killed"
			else:
				if attack >= 0:
					result = "hit"
				else:
					result = "absorbed"
		else:
			self.dodge_count = self.dodge_count + 1
			result = "missed"
		print result
		self.check_conditions()
		return result
	def attack(self, attack, targets, modifiers):
		for target in targets:
			
			attack_power = 0
			for dice in attack["damage"]:
				sides = dice.split(',')
				for roll in range(0, attack["damage"][dice]):
					rand = randint(1,len(sides)) - 1
					side = int( sides[ rand ] )
					attack_power = attack_power + side
			print "Attack Power: %s" % attack_power
			extras = {
				"accuracy": attack["accuracy"],
				"effects": attack["effects"],
				"type": attack["type"],
				"range": modifiers["range"],
			}
			result = target.defend(attack_power, extras)
			print "%s's health: %s" %(target.character_name, target.health)
			if result == "killed":
				self.kill_count = self.kill_count + 1
				self.hit_count = self.hit_count + 1
			elif result == "hit" or result == "absorbed":
				self.hit_count = self.hit_count + 1
			else:
				self.miss_count = self.miss_count + 1
			self.check_conditions()
	
	def set_effect(self, effect):
		self.check_conditions()
		return True
	
			
	def die(self):
		self.check_conditions()
		print "%s has fallen" % self.character_name
		
	def check_conditions(self):
		for condition in self.conditions:
			condition_triggered = False;
			
			if condition["type"] == "health":
				if condition["compare"] == "<=":
					if self.health <= condition["value"]:
						condition_triggered = True
				elif condition["compare"] == ">=":
					if self.health >= condition["value"]:
						condition_triggered = True
				elif condition["compare"] == "!=":
					if self.health != condition["value"]:
						condition_triggered = True
				elif condition["compare"] == "==":
					if self.health == condition["value"]:
						condition_triggered = True
			
			#End condition type
			
			if condition_triggered:
				special_results = ["attacks", "abilities", "effects"]
				for r in condition["results"]:
					if r in special_results:
						if r == "attacks":
							
							# Loop through each attack
							for a in condition["results"][r]:
								
								# Loop through each property
								for attack_properties in condition["results"][r][a]:
									if attack_properties == "damage":
										
										# Loop through all damages
										for d in condition["results"][r][a][attack_properties]:
											self.attacks[a][attack_properties][d] = condition["results"][r][a][attack_properties][d]
											
									else:
										self.attacks[a][attack_properties] = condition["results"][r][a][attack_properties]
								
					else:
						setattr(self, r, condition["results"][r])


#	def get_stats():