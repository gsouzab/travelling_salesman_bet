#!/usr/bin/python

from random import random
from names import randomName

class Player():
	name="Default"
	probabilities=[]
	bets=[]
	bankroll=1000.0
	weights=[]
	
	def __init__(self, size, bankroll=100.0):
		if size<1:
			print "Erro to instatiate Player"
			return
	  
		self.bankroll = bankroll
		self.name=randomName()
		self.probabilities = [0] * size
		for i in range(size):
			self.probabilities[i] = random()


	def calculateWeights(self, mask):
		number_of_weights = pow(2,mask.size)
		self.weights = [ 0 for x in range(number_of_weights) ]
		
		for i in range(number_of_weights):
			w = mask.calculateWeight(i, self.probabilities)
			self.weights[i] = w
	
	def makeBets(self, house):
		number_of_bets = len(self.weights)
		self.bets = [ 0 for x in range(number_of_bets) ]
		for i in range(number_of_bets):
			bet=0
			if house.weights[i] > self.weights[i]:
				p = 1.0/self.weights[i]
				bet = ((p*house.weights[i] - 1)/(house.weights[i] - 1))*self.bankroll
				bet = min(self.bankroll, max(bet, house.bet_min))
			
			self.bankroll -= bet
			self.bets[i] = bet
			house.receiveBet(bet)
	
	def isWinner(self, result):
		return self.bets[result] > 0
	
	def isBroken(self):
		return self.bankroll == 0
	
	def receiveAward(self, house, result):
		self.bankroll += house.payAward(result, self)
	
	def createNew(self):
		return Player(len(self.probabilities))

