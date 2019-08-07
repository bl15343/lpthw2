from sys import argv

script, input_file = argv

#Read the contents of the file and print them to stdout
def print_all(f):
    print f.read()

#Reposition the read head on the file object to the 
#beginning of the file
def rewind(f):
    f.seek(0)

#Print the current line count and the next line of the file
def print_a_line(line_count, f):
    print line_count, f.readline()

#Open the file defined on the command line
current_file = open(input_file)

print "First let's print the whole file:\n"

#Print the contents of current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Reposition the read head to the beginning
rewind(current_file)

print "Let's print three lines:"

#Set the current line to 1
current_line = 1
#Print 1 <First line of file>
print_a_line(current_line, current_file)

#Increment current line
current_line += 1
#Print 2 <Second line of file>
print_a_line(current_line,current_file)

#Increment current line
current_line += 1
#Print 3 <Third line of file>
print_a_line(current_line, current_file)

