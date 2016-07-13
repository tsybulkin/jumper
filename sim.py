from params import *
import numpy as np
import a_s, b_s, g_s
import x_f, y_f, a_f, b_f
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
	def __init__(self,x=0.4, y=0., a=2.4, b=1., g=1.2):
		self.q = np.array([x,y,a,b,g])
		self.q_d = np.zeros(5)
		self.psi = 0.4
		self.state_log = []

	def next_pos(self,tau):
		if self.q[1] > 0: # flies
			self.q_d = self.next_flying_pos(tau)
		else: # stands
			q_d_s = self.next_standing_pos(tau)	
			q_d_f = self.next_flying_pos(tau)
			if q_d_f[1] > q_d_s[1]: self.q_d = q_d_f
			else: self.q_d = q_d_s

		self.q += tau * self.q_d
		self.state_log.append(tuple(self.q))


	def next_standing_pos(self,tau):
		C = np.array([
			a_s.get_c1(self.q,self.q_d,self.psi),
			b_s.get_c2(self.q,self.q_d,self.psi),
			g_s.get_c3(self.q,self.q_d,self.psi)
			])
		D = - np.array([
			a_s.get_d1(self.q, self.q_d,self.psi),
			b_s.get_d2(self.q,self.q_d,self.psi),
			g_s.get_d3(self.q,self.q_d,self.psi) 
			])
		
		return self.q_d + np.hstack([np.zeros(2),tau * np.linalg.inv(C).dot(D)])
		
	

	def next_flying_pos(self,tau):
		C = np.vstack([
			x_f.get_c1(self.q,self.q_d,self.psi),
			y_f.get_c2(self.q,self.q_d,self.psi),
			a_f.get_c3(self.q,self.q_d,self.psi),
			b_f.get_c4(self.q,self.q_d,self.psi)
			])
		D = - np.array([
			x_f.get_d1(self.q, self.q_d,self.psi),
			y_f.get_d2(self.q,self.q_d,self.psi),
			a_f.get_d3(self.q,self.q_d,self.psi),
			b_f.get_d4(self.q,self.q_d,self.psi)
			])
		return self.q_d + np.hstack([tau * np.linalg.inv(C).dot(D), np.zeros(1)])
		

	def fell(self):
		_,_,_,b,g = self.q
		return b < 0 or b+g > np.pi




