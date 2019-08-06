#%d is a decimal string formatting placeholder, we're assigning
#the number 10 within this string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#%s is the string formatting placeholder, we're assigning
#binary to the first placeholder and do_not to the second 
y = "Those who know %s andthose who %s." % (binary, do_not)

#Print those variables
print x
print y

#Print the string x using the raw output formatter
print "I said: %r." % x
#Print the string y using the string output formatter. It is surrounded
#by single quotes
print "I also said: '%s'." % y

hilarious = False

#Assgined a string with a raw placeholder
joke_evaluation = "Isn't that joke so funny?! %r"

#When printing, bind hilarious to the output formatter
#in joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#The + operator acts as a concatenator
print w + e
