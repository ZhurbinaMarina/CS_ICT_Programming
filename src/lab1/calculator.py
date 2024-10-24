class Calculator:
    # Method for adding two numbers
    def add(self, x, y):
        return x + y

    # The method of subtracting one number from another
    def subtract(self, x, y):
        return x - y

    # Method of performing the product of two numbers
    def multiply(self, x, y):
        return x * y

    # Method that calculates the division of one number by another
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")

    # Method of calculating one number to the power of another
    def involution(self, x, y):
        return x ** y
