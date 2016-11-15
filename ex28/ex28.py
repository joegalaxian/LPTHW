# Exercise 28: Boolean Practice

print (True and True) == True
print (False and True) == False
print (1 == 1 and 2 == 1) == False
print ("test" == "test") == True
print (1== 1 or 2 != 1) == True
print (True and 1 == 1) == True
print ("test" == "testing") == False
print (1 != 0 and 2 == 1) == False

print ("test" != "testing") == True
print ("test" == 1) == False
print (not(True and False)) == True
print (not(10 == 1 or 1000 == 1000)) == False
print (not(1 != 10 or 3 == 4)) == False
print (not("testing" == "testing" and "Zed" == "Cool Guy")) == True
print (1 == 1 and (not("testing" == 1 or 1 == 0))) == True
print ("chunky" == "bacon" and (not(3 == 4 or 3 == 3))) == False
print (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) == False

# Python and many languages liek to return one of the operands to their operands to their boolean expressions rather than just True or False.
# This means that if you did False and 1 you get the fisrt operand (False) but if you do True and 1 you get the second (1).
# Play with this a bit.
