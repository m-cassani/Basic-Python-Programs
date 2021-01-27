######################################################################################################
# This program receives a positve integer number as input and returns if it`s a prime number or not. #
# Examples: 151 -> It`s a prime number! or 6513332 -> Not a prime number.                            #
######################################################################################################

i = 2
prime = True
close = False

while (close == False):

    num = int(input("Type an integer positive number: "))

    if (num < 2):
        print ("Not a prime number.\n")

    else:

        while ((i < num) and prime):

            if ((num % i) == 0):
                prime = False
            
            else:
                i = i + 1

        if (prime):
            print ("It's a prime number!\n")

        else:
            print ("Not a prime number.\n")
    
        i = 2
        prime = True