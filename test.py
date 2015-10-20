from traits import *

class Test(TraitsClass):
	name = String()
	age = Int()
	addr = Dict()

	def onnameChanged(self, value):
		print 'name has changed to %s' % value

	def onageChanged(self, value):
		print 'age has changed to %s' % value

	def onaddrChanged(self, value):
		print 'addr has changed to %s' % value	

if __name__ == '__main__':
	t = Test()
	t.name = 'white'
	t.age = 12
	t.name = 'rabbit'
	t.age = 18
	t.age = 'invalid age'
	t.a = 12
	t.addr = {'1': 'hangzhou', '2': 'shanghai'}
	t.addr = [1, 2]