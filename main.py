##### This ia python script
import sys


def multiply_two_numbers(x, y):
	return x * y


if __name__ == "__main__":

	x = sys.argv[1]
	y = sys.argv[2]
	print("Hello world")
	print("your numbers are", x, y)

	z = mulitply_two_numbers(x,y)

    #print(f"{x} + {y} = {z}")
    print(x, "+", y, "=", z)
