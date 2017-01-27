print "this is file2"


def fun():
	return "this is fun in file2"

def main():
	print "__name__: ",__name__
	print "this is f4"
	print "some statements to this file"
	print fun()
	print "some other statements to this file"
	print "end of f3"


if __name__ == "__main__":
	main()