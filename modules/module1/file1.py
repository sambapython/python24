print "this is file1"


def fun():
	return "this is fun in file1"

def main():
	print "__name__: ",__name__
	print "this is f4"
	print "some statements to this file"
	print fun()
	print "some other statements to this file"
	print "end of f3"


if __name__ == "__main__":
	main()