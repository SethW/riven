#!/usr/bin/env python

import pyttsx
from characters import characters
from game import Game
from player import Player
from character import Character
from pprint import pprint


if False:
	players_count = int(raw_input("How many players are there? "))
	players = []
	for p in range(1, players_count+1):
		
		#player_characters_count = int(raw_input("How many characters does player %r have? " % p))
		player_characters = []
		#for c in range(1, player_characters_count+1):
		c = 1
		character_name = ""
		
		while character_name != "done":
			character_name = raw_input("Enter name for Player %s's character #%s (or type 'done' if you are finished adding characters): " % (p, c))
			
			if character_name != "done":
				character_id = raw_input("Enter character id for %s: " % character_name)
				if character_id in characters:
					new_character = Character(c, character_id, character_name, characters[character_id])
					player_characters.append(new_character)
					c = c + 1
			
		players.append(Player(p, player_characters))


players = [
	Player(1, [
		Character(1, 1, "Phara", characters[1]),
	]),
	Player(2, [
		Character(1, 2, "Op", characters[2]),
	]),
]
	
current_game = Game(players)

while current_game.is_active:
	
	print "Ready for action"
	active_player = current_game.find_player(int(raw_input("Which player will activate? ")))
	active_character_name = raw_input("Which character will activate? ")
	
	active_character = active_player.find_character(active_character_name)
	
	
	print "%s's health is %s" %(active_character_name, active_character.health)
	print "Attacks"
	pprint(active_character.attacks)
	for attack in active_character.attacks:
		print active_character.attacks[attack]["name"]
		pprint(active_character.attacks[attack])
	print ""
	
	print "Abilities"
	for ability in active_character.abilities:
		print active_character.abilities[ability]["name"]
		pprint(active_character.abilities[ability])
	print ""
	action = raw_input ("What action should %s take? " % active_character_name)
	valid_action = active_character.is_valid_action(action)
	if valid_action:
		target_player_id = int(raw_input("Which player is the target? "))
		target_player = current_game.find_player(target_player_id)
		target_character_name = raw_input("Which character of Player %s is the target of %s's %s? " % (target_player_id, active_character_name, action))
		target_character = target_player.find_character(target_character_name)
		target_range = raw_input("How far away is %s from %s? " % (target_character_name, active_character_name))
		active_character.attack(valid_action, [target_character], {"range": target_range} )
		
	else:
		print "Invalid action: %s" % action
	
	

#thing = Character()
#print thing.health

#engine = pyttsx.init()
#engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
#engine.startLoop(False)
## engine.iterate() must be called inside externalLoop()
#externalLoop()
#engine.endLoop()



#class character(object):
#	def __init__(self):
#		self.health = 100
#	def defend(self, attack, modifiers):
#		
#	def attack(self, attack_type, targets, modifiers):
#		
#	def change_health(self, source):
#		
#	def die(attack):
#		
#	def conditions(event, modifiers):
#		
#	def get_stats():
#		
#


