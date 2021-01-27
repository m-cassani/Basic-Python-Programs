################################################################################################################
# This program receives a positve integer number as input and returns if it has equal adjacent digits in it.   #
# Examples: 123456789 -> It doesn`t have equal adjacent digits. or 1324556931 -> It has equal adjacent digits! #
################################################################################################################

i = 10
adj = False
close = False

while (close == False):

    num = int(input("Type a positive integer number: "))


    if ((num // i) == 0):

            adj = False

    else:

        while ((num // i) > 0 and not adj):

            before = int((num % i) // (i/10))

            after = int(((num % (i * 10))) // i)

            if (before == after):
                    
                adj = True

            else:

                i = i * 10

    if (adj):

        print ("It has equal adjacent digits!\n")

    else:

        print ("It doesn`t have equal adjacent digits.\n")

    i = 10
    adj = False