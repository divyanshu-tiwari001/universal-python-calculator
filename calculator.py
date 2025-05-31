from fractions import Fraction

def parse_number(value):
    try:
        return Fraction(value)  # handles fractions like "3/4"
    except ValueError:
        try:
            return float(value)  # handles decimals like "3.14"
        except ValueError:
            raise ValueError(f"Invalid number format: {value}")

def calculator():
    print("Welcome to the Python Calculator (supports decimals, fractions, and whole numbers)")
    
    while True:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        try:
            n1 = parse_number(num1)
            n2 = parse_number(num2)
        except ValueError as e:
            print(e)
            continue

        print("Choose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = n1 + n2
        elif choice == '2':
            result = n1 - n2
        elif choice == '3':
            result = n1 * n2
        elif choice == '4':
            if n2 == 0:
                print("Cannot divide by zero.")
                continue
            result = n1 / n2
        else:
            print("Invalid choice.")
            continue

        print(f"Result: {float(result)} (Exact: {result})")

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
