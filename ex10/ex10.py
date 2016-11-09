tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# It's the same if instead of ''' I use """.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '\\a: *BEEP* \a'
print '\\b: *BACKSPACE* \b'
print '\\f: *FORMFEED* \f'
print '\\r: *CARRIAGE_RETURN* \r'
print '\\v: *VERTICAL_TAB* \v'
print "I'm wondering where this line will be printed after the vertical tab."

print "HELLO WORLD!\r", # The '\r' will locate the cursor at the begging.
print "hello w"


# Extra: infinite loop printing a "clock"
while True:
	for i in ["/", "-", "|", "\\", "|"]:
#	for i in "0123456789": # Let's see what happens with this one.
		print "%s\r" % i, 
