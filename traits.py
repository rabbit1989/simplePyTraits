class String(object):
	@staticmethod
	def isValid(value):
		return isinstance(value, str)
	
class Int(object):
	@staticmethod
	def isValid(value):
		return isinstance(value, int)
	
class Dict(object):
	@staticmethod
	def isValid(value):
		return isinstance(value, dict)

class MetaTraitsClass(type):
	def __new__(meta, name, bases, dic):
		cls = super(MetaTraitsClass, meta).__new__(meta, name, bases, dic)	

		cls._traitsChangeHandlers = {}
		cls._traitsFields = {}
		for key, value in dic.iteritems():
			if value.__class__ in (String, Int, Dict): 
				cls._traitsFields[key] = value.__class__
				changeHandlerName = 'on' + key + 'Changed'
				if changeHandlerName in dic:
					cls._traitsChangeHandlers[key] = dic[changeHandlerName]

		return cls			
					
class TraitsClass(object):
	__metaclass__ = MetaTraitsClass

	def __setattr__(self, key, value):
		if key in self._traitsFields:
			if self._traitsFields[key].isValid(value):
				self.__dict__[key] = value
				if key in self._traitsChangeHandlers:
					self._traitsChangeHandlers[key](self, value)
			else:
				print 'invalid value %s: ' % str(value)

