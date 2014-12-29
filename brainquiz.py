from random import randint
from ctypes import windll

firstNumber = randint(10,99)
secondNumber = randint(10,99)

problem = str(firstNumber) + "  x  " + str(secondNumber)
answer = str(firstNumber*secondNumber)

windll.user32.MessageBoxA(0, problem, "Can you multiply these in your head?", 0)
windll.user32.MessageBoxA(0, "The answer is: " + answer, "How did you do?", 0)
