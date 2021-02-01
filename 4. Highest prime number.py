#############################################################################################################################
# This program receives an integer number higher than 1 as input and returns the highest prime number below or equal to it. #
# Examples: 100 -> 97  or 5000 -> 4999 or 6235 -> 6229. Obs: It may run slow for numbers higher than 100k.                  #
#############################################################################################################################

close = False

def highest_prime(num):
    highest_prime = 2
    aux = 2
    i = 2
    prime = True

    while (aux <= num):

        while ((i < aux) and prime):
            
            if ((aux % i) == 0):
                prime = False
            
            else:
                i = i + 1

        if (prime == True):
            highest_prime = aux
        
        prime = True
        aux = aux + 1
        i = 2

    return (highest_prime)

while (close == False):

    number = int(input("Input an integer number higher than 1: "))

    if(number <= 1):
        print("Invalid input.\n")

    else:
        print("The highest prime number below or equal to", number, "is", highest_prime(number), "\n")