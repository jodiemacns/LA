# Classes

class Car():
	def __init__(self):
		self.color = ''
		print "car started"
	def accel(self, speed):
		print "Speeding up to %s mph" % speed
	def turn(self, direction):
		print "turning " + direction
	def stop(self):
		print "stop"

class RaceCar(Car):
	def __init__(self, color):
		self.color = color
		self.top_speed = 200
		print "%s race car started with a top speed of %s" %(self.color, self.top_speed)
	def accel(self, speed):
		print "speeding up to %s mph very very fast" % speed

car1 = Car()
car1.color='red'
car1.accel(10)
car1.turn('right')

print "....... Starting the Race car section ........"

car2 = RaceCar('blue')
car2.color = 'red'
car2.accel(10)
car2.turn('left')
car2.stop()

print vars(car2)

