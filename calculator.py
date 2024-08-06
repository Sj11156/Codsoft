class Calculator:
    
    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2

def main():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    calc = Calculator()

    while True:
        operation = int(input("Choose an Operation: (1) Addition (2) Subtraction (3) Multiplication (4) Division :- "))
        if operation == 1:
            print(calc.add(num1, num2))
            break
        elif operation == 2:
            print(calc.sub(num1, num2))
            break
        elif operation == 3:
            print(calc.mul(num1, num2))
            break
        elif operation == 4:
            print(calc.div(num1, num2))
            break
        else:
            print("invalid option")

if __name__ == "__main__":
    main()