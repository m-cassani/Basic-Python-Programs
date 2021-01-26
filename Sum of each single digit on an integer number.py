#############################################################################################
# This program receives an integer number as input and returns the sum of each digit of it. #
# Examples: 135 -> 1 + 3 + 5 = 9  ou 123456789 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45     #
#############################################################################################

sum = 0
var = 0
i = 10

num = int(input("Type an integer number: "))

if ((num // i) == 0):

    sum = num

else:

    while ((num // i) > 0):

        var = (num % i)

        if ((var) < 10):

            sum = sum + var

        else:
            var = ((num % i) - (num % (i/10)))/(i/10)
            sum = sum + var
        
        i = i * 10

sum = sum + (num // (i/10))

print(int(sum))
