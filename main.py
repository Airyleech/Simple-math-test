import random


def add(): #This is for addition
    #Defining the variabbles
    a = random.randint(1, 100)
    b = random.randint(1,100)
    mathFormula = a + b
    mathFormulaUser = f"{a} + {b}"
    answer(a, b, mathFormulaUser, mathFormula)

def sub(): #This is for subtraction
    #Defining the variables
    a = random.randint(1, 100)
    b = random.randint(1,100)
    mathFormula = a - b
    if mathFormula <= 0: #This does not allow the first number to be smaller than the larger number (so not negative numbers)
        sub()
    else:
        mathFormulaUser = f"{a} - {b}"
        answer(a, b, mathFormulaUser, mathFormula)

def multiply():
    #Defining the variables for multiplication
    a = random.randint(1, 11)
    b = random.randint(1, 11)
    mathFormula = a * b
    mathFormulaUser = f"{a} * {b}"
    answer(a, b, mathFormulaUser, mathFormula)

def divide():
    #Defining the variables for division
    a = random.randint(5, 10)
    b = random.randint(1, 5)
    mathFormula = a / b
    mathFormulaUser = f"{a} / {b} (Write it as a float)"
    answer(a, b, mathFormulaUser, mathFormula)

def answer(a, b, mathFormulaUser, mathFormula):
    print(f"Solve this: {mathFormulaUser}") #This prints out the question
    userInput = str(input()) #This allows user input
    if userInput == str(mathFormula): #This checks if user input is correct
        print("Correct!") #If it is correct it will print "Correct!"
    else: #Else:
        print(f"Inccorect! The correct answer was: {mathFormula}.") #If user input is incorrect it will print this and show the correct answer

def main(): #This is the main method
    #Choosing if additon and subtraction or multiplication or division
    lowOrHighLevel = random.randint(0, 3) #This chooses if it is subtraction, addition, multiplication or division randomly.
    if lowOrHighLevel == 0:
        add()
    elif lowOrHighLevel == 1:
        multiply()
    elif lowOrHighLevel == 2:
        divide()
    elif lowOrHighLevel == 3:
        sub()

while True:
    main()
