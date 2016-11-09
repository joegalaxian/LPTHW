# EXERCISE 13: PARAMETERS, UNPACKING, VARIABLES.

# Imports "modules" (features) to the script from the Python feature set.

from sys import argv

# Unkpacking argv ("Argument variable") into STRING variables.
script, first, second, third = argv

# The first in argv is the name of the *.py file.
print "The script is called: %r" % script
print "Your firs variable is: %r" % first
print "Your second variable is: %r" % second
print "Your third variable is: %r " % third
