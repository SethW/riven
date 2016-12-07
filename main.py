#!/usr/bin/env python

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

#import pyttsx
from characters import characters
from game import Game
from player import Player
from character import Character
from pprint import pprint
from turn import Turn
import sys


class RivenApp(App):
	def build(self):
		
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
			
		
		global current_game
		current_game = Game(players)
		
		while current_game.is_active:
			
			print "Ready for action"
			
			
			new_turn = Turn(current_game)
			

def searchStringForCharacters(string):
	result = []
	for c in current_game.all_characters():
		if string.find(c.character_name) >= 0:
			result.append(c)
			string.replace(c.character_name, " ")
	return result

def searchStringForAction(string, character):
	for a in character.attacks:
		if string.find(character.attacks[a]["name"]) >= 0:
			return character.attacks[a]
	for a in character.abilities:
		if string.find(character.abilities[a]["name"]) >= 0:
			return character.abilities[a]
	return False


if __name__ == '__main__':
    RivenApp().run()
	
	
	#print "%s's health is %s" %(active_character_name, active_character.health)
	#print "Attacks"
	#pprint(active_character.attacks)
	#for attack in active_character.attacks:
	#	print active_character.attacks[attack]["name"]
	#	pprint(active_character.attacks[attack])
	#print ""
	
	#print "Abilities"
	#for ability in active_character.abilities:
	#	print active_character.abilities[ability]["name"]
	#	pprint(active_character.abilities[ability])
	#print ""
	#action = raw_input ("What action should %s take? " % active_character_name)
	#valid_action = active_character.is_valid_action(action)
	#if valid_action:
		
		#target_player_id = int(raw_input("Which player is the target? "))
		#target_player = current_game.find_player(target_player_id)
	#	target_character_name = raw_input("Which character is the target of %s's %s? " % (active_character_name, action))
	#	target_character = current_game.find_character(target_character_name)
	#	target_range = raw_input("How far away is %s from %s? " % (target_character_name, active_character_name))
	#	active_character.attack(valid_action, [target_character], {"range": target_range} )
		
	#else:
	#	print "Invalid action: %s" % action
	
	


#engine = pyttsx.init()
#engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
#engine.startLoop(False)
## engine.iterate() must be called inside externalLoop()
#externalLoop()
#engine.endLoop()
