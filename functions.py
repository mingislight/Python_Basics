# Functions: Mini programs, need to be defined first before called
#eg. print(), input(), int(), random.randint()
def main():
    def greeting(name):
        print('Hello', name)

    # Main Program:

    input_name = input('Enter your name:\n')

    # Calling our function
    greeting(input_name)

    ## Functions with 2 parameters

    def addition(a,b):
        return a + b

    # Main Program
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter your 2nd number:\n'))

    # Calling our function
    result = addition(num1, num2)
    print('The result is', result)

main()