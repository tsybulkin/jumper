from params import *
import numpy as np
import a_s, b_s, g_s
from show import show


def eq_zero(x): 
	TRESHOLD = 0.0001
	return abs(x) < TRESHOLD
	

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


class Robot():
	def __init__(self,x=0.4, y=0., a=2.4, b=1.08, g=1.2):
		self.q = np.array([x,y,a,b,g])
		self.q_d = np.zeros(5)
		self.psi = 0.5
		self.state_log = []

	def next_pos(self,tau):
		if self.q[4] == g0: # flies
			self.next_flying_pos(tau)
		else: # stands
			self.next_standing_pos(tau)	
		self.state_log.append(tuple(self.q))


	def next_standing_pos(self,tau):
		C = np.array([a_s.get_c1(self.q,self.q_d,self.psi),
					b_s.get_c2(self.q,self.q_d,self.psi),
					g_s.get_c3(self.q,self.q_d,self.psi)])
		D = - np.array([a_s.get_d1(self.q, self.q_d,self.psi),
						b_s.get_d2(self.q,self.q_d,self.psi),
						g_s.get_d3(self.q,self.q_d,self.psi) ])
		
		self.q_d += np.hstack([np.zeros(2),tau * np.linalg.inv(C).dot(D)])
		self.q += tau * self.q_d

		if self.q[4] < g0:
			bn = self.q[4]
			xa = self.q[0] + L3*np.cos(bn)
			ya = self.q[1] + L3*np.sin(bn)
			delta = g0 - self.q[4]
			self.q_d[4] = 0
			self.q[0] = xa - L3*np.cos(bn-delta)
			self.q[1] = ya - L3*np.sin(bn-delta)  

			if self.q[3] > np.pi/2:
				self.q[1] = 0

			self.q[3] += -delta 
			self.q[4] = g0
			

	def next_flying_pos(self,tau):
		self.q_d = np.array([0, 10*(0.1-self.q[1]), 0, 0, 0])
		self.q += tau* self.q_d
		
		

	def fell(self):
		_,_,_,b,g = self.q
		return b < 0 or b+g > np.pi




