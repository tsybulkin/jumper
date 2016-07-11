from params import *
from numpy import sin, cos

x,y = 0.3, 0 # coords of the toe tip


def show(anim_file, state_log,tau):
	f = open(anim_file,'w')
	f.write("<html>\n<body>\n<svg width='1000' height='650'>\n")

	draw_line(f,[((x,y),(x+L3*cos(b),y+L3*sin(b))) for (x,y,_,b,_) in state_log ],5,'blue',tau)
	draw_line(f,[((x+L3*cos(b),y+L3*sin(b)),(x+L3*cos(b)+L2*cos(b+g),y+L3*sin(b)+L2*sin(b+g))) 
		for (x,y,_,b,g) in state_log ],7,'rgb(50,50,200)',tau)
	draw_line(f,[((x+L3*cos(b)+L2*cos(b+g),y+L3*sin(b)+L2*sin(b+g)),
			(x+L3*cos(b)+L2*cos(b+g)+2*L1*cos(a+b+g),y+L3*sin(b)+L2*sin(b+g)+2*L1*sin(a+b+g))) 
		for (x,y,a,b,g) in state_log ],9,'rgb(70,70,150)',tau)

	f.write("</svg>\n</body>\n</html>")
	f.close()


def draw_line(f, points_list, width, color, tau):
	f.write("\t<line x1='%i' y1='%i' x2='%i' y2='%i' \
		style='stroke:%s;stroke-width:%i' >\n" % (0,0,0,0,color,width))
	T = 0
	for xy1,xy2 in points_list:
		x1,y1 = px(xy1)
		x2,y2 = px(xy2)
		f.write("\t\t<set attributeName='x1' attributeType='XML'\n \
         to='%i' begin='%.2fs'  />\n" %(x1,T) ),
		f.write("\t\t<set attributeName='y1' attributeType='XML'\n \
         to='%i' begin='%.2fs'  />\n" %(y1,T) ),
		f.write("\t\t<set attributeName='x2' attributeType='XML'\n \
         to='%i' begin='%.2fs'  />\n" %(x2,T) ),
		f.write("\t\t<set attributeName='y2' attributeType='XML'\n \
         to='%i' begin='%.2fs'  />\n" %(y2,T) ),
		T += tau
	f.write("\t</line>\n")	


def px(xy):
	return ( 100+round(xy[0]*1500), 600-round(xy[1]*1500) )



