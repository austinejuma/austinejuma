class Calculator:
    count = 0  # Static attribute

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Using static method and updating count
result = Calculator.add(5, 3)
print(f"Result: {result}, Add method called: {Calculator.count} times")
