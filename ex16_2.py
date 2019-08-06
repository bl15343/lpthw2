from sys import argv

script, filename = argv

print "Reading your file: %s" % filename

file_to_read = open(filename)
print file_to_read.read()

print "Closing file"
file_to_read.close() 
