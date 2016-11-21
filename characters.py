#!/usr/bin/env python

characters = {
	1: {
		"name": "Saint Pyros",
		"max-health": 100,
		"type": ["ground", "holy"],
		"faction": ["fire"],
		"immune": [],
		"move": 6,
		"actions": 3,
		"attacks": {
			"fire-sword": {
				"name": "Fire Sword",
				"range": 0,
				"status": "active",
				"actions": 1,
				"damage": {
					"1,2,3,4,5,6": 2,
					"1": 1
				},
				"area": 0,
				"accuracy": 10,
				"effects": ["fire"],
				"type": ["fire", "physical"]
				
			}
		},
		"abilities":{
			"healing-warmth": {
				"name": "Healing Warmth",
				"range": 0,
				"status": "active",
				"actions": 2,
				"damage": {
					"1,2,3": -3
				},
				"area": 0,
				"effects": [],
				"type": ["friendly", "heal"]
			}
		},
		"dodge": 20,
		"armor": 2,
		"conditions": [
			{
				"type": "health",
				"compare": "<=",
				"value": 80,
				"results": {
					"move": 5,
					"attacks": {
						"fire-sword": {
							"damage": {
								"1,2,3,4,5,6": 1
							}
						}
					}
				}
			}
		]
	},
	
	
	2: {
		"name": "Fire Bird",
		"max-health": 20,
		"type": ["air", "creature"],
		"faction": ["fire"],
		"immune": ["fire"],
		"move": 10,
		"actions": 5,
		"attacks": {
			"dive-bomb": {
				"name": "Dive Bomb",
				"range": 3,
				"actions": 2,
				"status": "active",
				"damage": {
					"0,0,0,1,2,3": 2,
				},
				"area": 1,
				"accuracy": 0,
				"effects": ["fire"],
				"type": ["fire", "physical"]
				
			}
		},
		"dodge": 30,
		"armor": 1,
		"abilities": {},
		"conditions": [
			{
				"type": "health",
				"compare": "<=",
				"value": 15,
				"results": {
					"move": 5,
					"attacks": {
						"dive-bomb": {
							"damage": {
								"0,0,0,1,2,3": 2
							},
							"accuracy": -10,
						}
					}
				}
			}
		]
	},
	
	
}
