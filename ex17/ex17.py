# EXERCISE 17: MORE FILES
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" % (from_file, to_file)

# We could do there two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).read()

print "The input file is %d byttes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') # This will create the file if doesn't exists.
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
