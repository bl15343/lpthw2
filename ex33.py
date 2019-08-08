
numbers = []
numbers_two = []

def funky(iterations, step):
    i = 0

    while i < iterations:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    for x in range(0,iterations,step):
        print "At the top x is %d" % x
        numbers_two.append(x)
        print "Numbers now: ", numbers_two
        print "At the bottom x is %d" % x


     
funky(7,2)
print "The numbers: "

for num in numbers:
    print num

