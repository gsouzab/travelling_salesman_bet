#!/usr/bin/python

from house import House
from player import Player
from event import Event
from mask import Mask

class Game():
	turns=10000
	event=None
	house=None
	players=[]
	solution=[]
	
	def __init__(self, size_of_player, turns=10000, players_number=20, mask_size=3):
		self.mask_size = mask_size
		self.size_of_player = size_of_player
		self.turns = turns
		self.house = House()
		self.event = Event()
		
		for index in range(players_number):
			player = Player(size_of_player)
			self.players.append(player)
	
	def generateMask(self):
		return Mask(self.mask_size, self.size_of_player)
	
	def play(self):
		self.solution = self.event.getInitialSolution()
		for turn in range(self.turns):
			mask = self.generateMask()
			
			for player in self.players:
				player.calculateWeights(mask)
			
			self.house.calculateWeights(self.players)
			
			for player in self.players:
				player.makeBets(self.house)
				print "The player "+ player.name +" makes bets."
			
			relsult = mask.calculateBestMask(self.event, self.solution)
			
			for index in range(len(self.players)):
				player = self.players[index]
				if player.isWinner(result):
					player.receiveAward(self.house, result)
					print "The player "+ player.name +" receives award."
				if player.isBroke():
					print "The player "+ player.name +" is out."
					self.players[index] = player.createNew()
					print "The new player "+ self.players[index].name +" is in."
				
			new_solution = mask.generateSolution(result, self.solution)
			
			if self.event.f(new_solution) < self.event.f(solution):
				self.solution = new_solution
			
