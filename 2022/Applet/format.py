MODULE = "format"
class Template(object):
	def __init__(self,temp):
		self.__spec = temp
	def format(self,*te):
	    self.__spec.format(*te)
