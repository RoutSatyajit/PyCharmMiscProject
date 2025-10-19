number1=int(input("Enter number1\n"))
number2=int(input("Enter number2\n"))
operator=input("Enter the operator")

match operator:
    case "/":
        print(f"O/p is : {number1 / number2}")
    case "*":
        print(f"O/p is :{number1 * number2}")
    case "+":
        print(f"O/p is :{number1 + number2}")
    case "-":
        print(f"O/p is :{number1 - number2}")

