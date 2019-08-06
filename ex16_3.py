from sys import argv

#Unpack filename from command line args
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Prompt user to quit or continue
raw_input("?")

#Open the filename provided on command line
print "Opening the file..."
target = open(filename, 'w')

#Erasing the contents of the file
print "Truncating the file. Goodbye!"
target.truncate()

#Get new content for file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#Write content to file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write( "%s\n%s\n%s\n"  % (line1, line2, line3) )

#Close file object
print "And finally, we close it."
target.close()
