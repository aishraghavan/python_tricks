def pythagorean_triples():
	for x in range(1, 30):
		for y in range(x, 30):
			for z in range(y, 30):
				if x**2 + y**2 == z**2:
					print(x, y, z)

if __name__ == "__main__":
	pythagorean_triples()

	print "list_comprehension:"
	print [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
