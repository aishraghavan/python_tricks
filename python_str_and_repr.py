"""
Source: http://pythoncentral.io/what-is-the-difference-between-__str__-and-__repr__-in-python/

object.__repr__(self): called by the repr() built-in function and by string conversions (reverse quotes) to compute the "official" string representation of an object.
object.__str__(self): called by the str() build-in function and by the print statement to compute the "informal" string representation of an object.
"""

x=1
print repr(x)
print str(x)

y = 'a string'
print repr(y)
print str(y)

print eval(repr(y))

# wont work :(
#print eval(str(y))

from datetime import datetime
from decimal import Decimal

print(Decimal('42'), datetime.now())
print (str(Decimal('42')), str(datetime.now()))

"""
Tips and Suggestions between __str__ and __repr__ in Python

Implement __repr__ for every class you implement. There should be no excuse.
Implement __str__ for classes which you think readability is more important of non-ambiguity.
"""

class ClassA(object):
	def __init__(self, a=None):
		self.a  = a

	def __repr__(self):
		return '%s(%r)' % (self.__class__, self.a)

a = ClassA()
print repr(a)

