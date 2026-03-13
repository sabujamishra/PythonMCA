# Global variable
x = 10

def outer_function():
    # Enclosing variable
    y = 20

    def inner_function():
        nonlocal y   # refers to variable in outer_function
        global x     # refers to global variable

        # Local variable
        z = 30

        # Modify variables
        y += 5
        x += 2
        z += 1

        print("Inside inner_function:")
        print("Local z =", z)
        print("Nonlocal y =", y)
        print("Global x =", x)

    inner_function()
    print("Inside outer_function after inner_function call:")
    print("Nonlocal y =", y)

# Main program
print("Global x before:", x)
outer_function()
print("Global x after:", x)
