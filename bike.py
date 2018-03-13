# title of assignment and separator
print "\n----------Bike Assignment----------\n"

# Create a new class called Bike with the following properties/attributes:
class Bike(object):
	# this method to run every time a new object is instantiated
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	# defines method that displays bike's price, maximum speed, and total miles.
	def displayInfo(self):
		print "Price: ${}".format(self.price)
		print "Max speed: ", self.max_speed
		print "Miles: ", self.miles
		return self

	# defines method that displays miles ridden + 10
	def ride(self):
		self.miles += 10
		print "Riding... {} miles".format(self.miles)
		return self

	# defines method that displays miles ridden - 5
	def reverse(self):
		# doesn't allow the bike to reverse if miles reversed falls below 0
		if self.miles > 4:
			self.miles -= 5
			print "Reversing... {} miles".format(self.miles)
		else:
			print "There is not enough room to reverse. Please try riding first!"
		return self

# create 3 instances/objects of class: 'Bike'
bike1 = Bike(1, "10mph", 0)
bike2 = Bike(2, "20mph", 0)
bike3 = Bike(3, "30mph", 0)

# bike instance separator
print "\n----------Bike 1----------"
# first instance rides three times, reverses once and displayInfo()
bike1.ride().ride().ride().reverse().displayInfo()

print "\n----------Bike 2----------"
# second instance rides twice, reverses twice and displayInfo().
bike2.ride().ride().reverse().reverse().displayInfo()

print "\n----------Bike 3----------"
# third instance reverses three times and displayInfo().
bike3.reverse().reverse().reverse().displayInfo()

# separator
print ""