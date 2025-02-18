try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1/num2
    print("Result is ", result)
    print("Result is ", result1)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a number")
except NameError as ex:
    print("The exception is ", ex)
except:
    print("Error occured")
finally:
    print("I will execute no matter what happens")