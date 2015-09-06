"""
Range(5): [0, 1, 2, 3, 4] 
"""
print "Range(5): [0, 1, 2, 3, 4] "
print range(5)

"""
Xrange: Returns Xrange object.
"""
print "\nXrange: Returns Xrange object."
print xrange(5)

"""
Zipping and unzipping lists
"""
print "\nZipping and unzipping lists"
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
# zip values
zipped_values = zip(x, y, z)
print zipped_values
# unzip values
unzipped_values = zip(*zipped_values)
for list in unzipped_values:
	print list

"""
Reduce function 
"""
print "\nReduce function"
print reduce(lambda x,y: x+y, range(100))

"""
Map function
"""
print "\nMap function"
numbers = (10, 20, 30)
squared_values = map(lambda x: x**2, numbers)
print squared_values

"""
Filter values
"""
print "\nFilter values "
int_numbers = range(20)
print "Int numbers : ", int_numbers
odd_numbers = filter(lambda x: x%2, int_numbers)
print "Odd numbers: ", odd_numbers
even_numbers = filter(lambda x: x%2==0, int_numbers)
print "Even numbers: ", even_numbers