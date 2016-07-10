from params import *
import numpy as np
from a import get_c1, get_d1
from b import get_c2, get_d2
from gama import get_c3, get_d3
from show import show



class Robot():
	def __init__(self,a=1.9,b=1.0,gama=1.1):
		self.q = np.array([a,b,gama])
		self.q_d = np.zeros(3)
		self.psi = 0
		self.state_log = []

	def next_pos(self,tau):
		C = np.array([get_c1(self.q,self.q_d,self.psi),
					get_c2(self.q,self.q_d,self.psi),
					get_c3(self.q,self.q_d,self.psi)])
		D = - np.array([get_d1(self.q, self.q_d,self.psi),
						get_d2(self.q,self.q_d,self.psi),
						get_d3(self.q,self.q_d,self.psi) ])
		
		self.q_d += tau * np.linalg.inv(C).dot(D)
		self.q +=  tau * self.q_d
		if self.q[2] > 2.5: 
			self.q = (self.q[0], self.q[1], 2.5)
			self.q_d = (self.q_d[0],self.q_d[1],0)
		elif self.q[2] < gama0:
			self.q = (self.q[0], self.q[1], gama0)
			self.q_d = (self.q_d[0], self.q_d[1], 0)
		self.state_log.append(tuple(self.q))


	def fell(self):
		_,b,gama = self.q
		return b < 0 or b+gama > np.pi
		

def run(tau,T,playback_speedup=1):
	assert tau < 0.1
	assert tau > 0
	assert T > 0

	bot = Robot()
	t = 0
	while t < T:
		bot.next_pos(tau)
		t += tau
		#print '\nt =', t, 'pos:\n', bot.q, bot.q_d
		if bot.fell(): break

	show('no_control.html',bot.state_log,tau/playback_speedup)



