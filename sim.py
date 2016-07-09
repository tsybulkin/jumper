from params import *
import numpy as np
from a import get_c1, get_d1
from b import get_c2, get_d2
from gama import get_c3, get_d3



class Robot():
	def __init__(self,a=1.8,b=1.2,gama=np.pi/2):
		self.q = np.array([a,b,gama])
		self.q_d = np.zeros(3)
		self.psi = 0

	def next_pos(self,tau):
		C = np.array([get_c1(self.q,self.q_d,self.psi),
					get_c2(self.q,self.q_d,self.psi),
					get_c3(self.q,self.q_d,self.psi)])
		D = - np.array([get_d1(self.q, self.q_d,self.psi),
						get_d2(self.q,self.q_d,self.psi),
						get_d3(self.q,self.q_d,self.psi) ])
		#print 'C:',C
		#print 'D:',D

		self.q_d += tau * np.linalg.inv(C).dot(D)
		self.q +=  tau * self.q_d
		if self.q[2] > 3: 
			self.q[2] = 3
			self.q_d[2] = 0


	def fell(self):
		_,b,_ = self.q
		return b<0 or b>np.pi/2
		

def run(tau,T):
	assert tau < 0.1
	assert tau > 0
	assert T > 0

	bot = Robot()
	t = 0
	while t < T:
		bot.next_pos(tau)
		t += tau
		print '\nt =', t, 'pos:\n', bot.q, bot.q_d
		if bot.fell(): break



