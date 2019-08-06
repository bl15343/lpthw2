tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

single_cat = '''
I'll do a list
\t\b\r* Cat food
\t\b\f* Fishies
\t\b\v* Catnip\n\t\b* Grass
\x41\x42\x43\x44
'''

print single_cat

raw_format = "%r %s" % ('I am 6\'2"', 'I am 6\'2"')

print raw_format

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
