from sys import argv

#Unpack the command line arguments
script, filename = argv

#Open a file stored at the path filename
#Return a file object/reference
txt = open(filename)

#Print out the filename from the command line
print "Here's your file %r:" %filename
#Print the contents of the file object
print txt.read()

txt.close()

print "Type the filename again:"
#Get the filename from the user's input
file_again = raw_input("> ")

#Open the file
txt_again = open(file_again)

#Print out the contents
print txt_again.read()

txt_again.close()
