##### This ia python script
import sys
def multiply_two_numbers(x, y):
        return x * y
##

if __name__ == "__main__":
        x_str = sys.argv[1]
        y_str = sys.argv[2]

        x = int(x_str)
        y = int(y_str)

        print("Hello world")
        print("your numbers are", x, y)
        
        z = multiply_two_numbers(x,y)

        print(f"{x} + {y} = {z}")
