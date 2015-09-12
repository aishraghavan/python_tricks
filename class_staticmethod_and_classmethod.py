class Car(object):

	wheels = 4

	def __init__(self, make, model):
		self.make = make
		self.model = model

	# Note: 
	# 1. no self keyword
	# 2. can call with object or call directly with the Class name. No object required.
	# 3. It can be bound it to an object or to a class.
	@staticmethod
	def steering_and_horn():
		print "steering and horn are working fine."

	@classmethod
	def print_wheels(cls):
		print "Number of wheels: {0}".format(cls.wheels)


mustang = Car('Ford', 'Mustang')
print mustang.make
print mustang.model
print mustang.wheels
mustang.steering_and_horn()
Car.steering_and_horn()
Car.print_wheels()