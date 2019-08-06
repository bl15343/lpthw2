#Defining the cheese_and_crackers function with two 
#arguments. One for the count of cheese, the other
#for the number of boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #Print out the number of cheeses
    print "You have %d cheeses!" % cheese_count
    #Print out the number of boxes of crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
#Call the function with 20 cheese and 30 boxes of crackers
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#Call the function with variables, instead of integer literals
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#Call the function with other functions as arguments!
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
#Call the function with variables and functions as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def baguettes_and_jam(baguette_count, jam_count):
    print "You need %d baguettes!" % baguette_count
    print "Because you have %d jams!" % jam_count
    print "Nice hiss!"


party_baguettes = 200
party_jam = 100

baguettes_and_jam(1,2)
baguettes_and_jam(100 % 4, 300 % 20)
baguettes_and_jam(party_baguettes, party_jam)
baguettes_and_jam(party_baguettes + party_jam, party_jam)

