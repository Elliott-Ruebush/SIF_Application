#Author: Elliott Ruebush
def evaluateRangeForQuantsAndTeams(n: int):
    """Prints Quant Team, Quant, Team, or an integer based on evaluation of each number in the range 1 to n"""
    for i in range(1, n + 1):
        currentNumber: int = i
        if(currentNumber % 14 == 0):
            """currentNumber % 14 is equivalent to checking modulus for both 2 and 7 since 14 is the product 2 * 7 and 2 and 7 are both prime numbers"""
            print("Quant Team")
        elif(currentNumber % 2 == 0):
            print("Quant")
        elif(currentNumber % 7 == 0):
            print("Team")
        else:
            print(currentNumber)


evaluateRangeForQuantsAndTeams(14)
