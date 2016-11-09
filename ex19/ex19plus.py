def test_modify_variable(var):
	print "\tEntering the function:"
	print "\tThe input variable =", var
	var += 10
	print "\tAfter modifying the variable =", var
	print "\tLeaving the function."

v = 1
print "Starting with the variable=", v
test_modify_variable(v)
print "After calling the funciton, the variable remains the same =", v
