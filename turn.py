#!/usr/bin/env python
from pprint import pprint
import re

class Turn(object):
	def __init__(self, current_game):
		self.current_game = current_game
		self.active_character = False
		self.turn_steps = ["activate", "take_action", "finish"]
		self.step = "activate"
		self.action = False
		self.action_count = 0
		self.activate()
	
	
	def load_step(self, next_step):
		step = getattr(self, next_step)
		self.step = next_step
		step()
	
	
	def step_back(self):
		step_position = self.turn_steps.index(self.step)
		if step_position > 0:
			self.load_step(self.turn_steps[step_position - 1])
		else:
			self.step_again()
	
	
	def step_forward(self):
		step_position = self.turn_steps.index(self.step)
		if step_position < len(self.turn_steps)-1:
			self.load_step(self.turn_steps[step_position + 1])
		else:
			self.step_again()
	
	
	def step_again(self):
		self.load_step(self.step)
	
	
	def activate(self):
		character_name = self.filter_input(raw_input("Which character will activate? "))
		character = self.current_game.find_character(character_name)
		if character:
			if character.health > 0:
				for effect in character.effects:
					effect.run_activate()
				self.active_character = character
				self.action_count = character.actions
				print "Activating %s" % (character.character_name)
				character.activate_count = character.activate_count + 1
				self.step_forward()
			else:
				print "%s has been destroyed" % character.character_name
				self.step_again()
		else:
			print "%s is an invalid character" % character_name
			self.step_again()
	
	
	def take_action(self):
		print "%s's Heath: %s - %s's Actions: %s" % (self.active_character.character_name, self.active_character.health, self.active_character.character_name, self.action_count)
		action_string = self.filter_input(raw_input("What will %s do? " % self.active_character.character_name))
		if action_string == False:
			return False
		action = self.active_character.find_action(action_string)
		if action != False:
			if action["status"] == "active":
				if action["actions"] <= self.action_count:
					
					if action["range"] > 0:
						if action_string.find("range") >= 0:
							split_range = action_string.split("range")
							try:
								range_distance = int(re.findall(r'\d+', split_range[1])[0])
								range_label = " at range " + str(range_distance)
							except ValueError:
								print "%s is not valid - %s" %(range_distance, split_range[1])
								self.step_again()
								
						else:
							print "Range required for %s" % action["name"]
							self.step_again()
					else:
						range_distance = 0
						range_label = ""
					
					if range_distance > action["range"]:
						print "Target out of range"
						self.step_again()
					else:
						targets = self.current_game.find_targets(action_string)
						target_names = ""
						t_count = 0
						for t in targets:
							t_count = t_count + 1
							if len(targets) >= 3:
								if t_count == len(targets):
									target_names = target_names + "and " + t.character_name
								else:
									target_names = target_names + t.character_name + ", "
							elif len(targets) == 2:
								if t_count == len(targets):
									target_names = target_names + "and " + t.character_name
								else:
									target_names = t.character_name
							else:
								target_names = t.character_name
						
						
						
					if len(targets) >= 1:
						confirm_action = self.filter_input(raw_input("Confirm %s targeting %s with %s%s " % (self.active_character.character_name, target_names, action["name"], range_label)))
						if confirm_action == False:
							return False
						if confirm_action.find("yes") >= 0 or confirm_action.find("confirm") >= 0 or confirm_action.find("yeah") >= 0 or confirm_action.find("yup") >= 0:
							self.active_character.attack(action, targets, {"range": range_distance})
							self.action_count = self.action_count - action["actions"]
							if self.action_count > 0:
								self.step_again()
							else:
								self.step_forward()
						else:
							print "Action canceled"
							self.step_again()
					else:
						print "Target not found"
						self.step_again()
						
				else:
					print "Not enough actions left for %s" % action["name"]
					self.step_again()
			else:
				print "$s is not active" % action["name"]
				self.step_again()
			
			#action = active_character.is_valid_action(action_name)
			#if action:
			#	self.action = action
			#	self.step_forward()
			#else:
			#	self.step_again()
		else:
			print "Action not valid"
			self.step_again()
	
	
	def finish(self):
		print "Deactivating %s" %self.active_character.character_name
		self.step = "activate"
		self.action = False
		self.active_character = False
		self.action_count = 0
	
	
	def filter_input(self, input):
		if input.find("abort") >= 0 or input.find("cancel") >= 0:
			self.step_back()
		elif input.find("end turn") >= 0 or input.find("finish turn") >= 0 :
			confirm = self.filter_input(raw_input("Confirm ending %s's turn? " % self.active_character.character_name))
			if confirm.find("yes") >= 0 or confirm.find("confirm") >= 0 or confirm.find("yeah") >= 0 or confirm.find("yup") >= 0:
				return False
			else:
				self.step_again()

		elif input.find("end game") >= 0 or input.find("quit game") >= 0 :
			if self.current_game.end_game() == False:
				self.step_again()
		else:
			return input
			