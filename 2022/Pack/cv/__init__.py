from turtle import *


class Canva(object):
	def __init__(self, start = [0,0], pendown = True):
		setup(800, 800, 0, 0)
		hideturtle()
		self.pen = Pen()
		self.dpen = self.pen
		if pendown:
			self.pen.pendown()
		print("Created canva")

	def cp(self, pen = None):
		print("Changed pen to",pen if pen else self.pen)
		self.pen = pen if pen else self.pen

	def mp(self):
		pen = Pen()
		print("Changed pen to",pen if pen else self.pen)
		self.pen = pen if pen else self.pen
		return pen

	def d(self, startx = 0, starty = 0, endx = 0, endy = 0):
		self.pen.penup()
		self.pen.goto(startx, starty)
		self.pen.pendown()
		self.pen.goto(endx, endy)

	def z(self, deg = 0):
		self.pen.right(deg)

	def clr(self, penc = None, fillc = None):
		if penc:
			color(penc)
		if fillc:
			fillcolor(fillc)

	def r(self, startx = 0, starty = 0, endx = 0, endy = 0):
		self.pen.penup()
		self.pen.goto(startx, starty)
		self.pen.pendown()
		self.d(startx, starty, endx, starty)
		self.d(endx, starty, endx, endy)
		self.d(endx, endy, startx, endy)
		self.d(startx, endy, startx, starty)

	def c(self, r = 0, posx = 0, posy = 0):
		self.pen.penup()
		self.pen.goto(posx, posy - r)
		self.pen.pendown()
		self.pen.circle(r,360)

	def g(self, posx = 0, posy = 0):
		self.pen.goto(posx, posy)

	def f(self):
		input("Press Enter to finish")
		print("Canva", self, "is closed")
		self.pen.hideturtle()
		del self

	def CLOSE(self):
		del self
		return 1

	def v(self):
		print("VIEW ONLY MODE")
		try:
			while True:
				pass
		except KeyboardInterrupt:
			self.pen.reset()
			self.pen.hideturtle()
			return 0

		

dc = Canva()