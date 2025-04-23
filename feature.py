def sum(a,b):
    return a + b
    # Return sum of a and b together

def get_integer():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Oops! Not a valid number. Try again.")

x = get_integer()
y = get_integer()
print("Your value is: ",sum(x,y))
