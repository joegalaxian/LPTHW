# Exercise 37: Symbol Review

# Keywords
# ========

True and False == False

with X as Y:
	pass

assert False, "Error!"

while True:
	break

class Person(object)

while True:
	continue

def X():
	pass

del X[Y]

if: X; elif: Y; else: J

except ValueError, e: print e

exec 'print "hello"'

finally:
	pass

for X in Y:
	pass

from x import Y

global X

import os

for X in Y: pass
1 in [1] == True

1 is 1 == True

s = lambda y: y ** y; s(3)

True of False == True

def empty():
	pass

print 'this string'

raise ValueError("No")

def X():
	return Y

try:
	pass

while X:
	pass

with X as Y:
	pass

def X(): yield Y; X().next()

# Data Types
# ==========

# True
True or False == True

# False boolean value.
False and True == False

# None: Represent "nothing" or "no value".
x = None

# strings: Stores textual information.
x = "hello"

# numbers: Stores integers.
i = 100

# floats: Stores decimals.
i = 10.389

# lists: Stores a list of things.
j = [1, 2, 3, 4]

# dicts: Stores a key=value mapping of things.
e = {'x': 1, 'y': 2}

# String Escape Sequences
# =======================

print '\\' # Backslash
print '\'' # Single-quote
print '\"' # Double-quote
print '\a' # Bell
print '\b' # Backspace
print '\f' # Form feed
print '\n' # New line
print '\r' # Carriage
print '\t' # Tab
print '\v' # Vertical tab

# String formats
# ==============

# %d Decimal integers (not floating point).
"%d" % 5 == '45'

# %i Same as %d.
"%i" % 45 == '45'

# %o Octal number.
"%o%" % 1000 == '1750'

# %u Unsigned decimal.
"%u" % -1000 = '-1000'

# %x Hexadecimal lowercase.
"%x" % 1000 = '3e8'

# %X Hexadecimal uppercase.
"%X" % 1000 = '3E8'

# %e Exponential notation, lowercase 'e'.
"%e" % 1000 == '1.000000e+03'

# %E Exponential notation, upper case 'E'.
"%E" % 1000 == '1.000000E+03'

# %f Floating point real number.
"%f" % 10.34 == '10.340000'

# %F Same as %f.
"%F" % 10.34 == '10.340000'

# %g Either %f or %e, whichever is shorter.
"%g" % 10.34 == '10.34'

# %G Same as %g but uppercase.
"%G" % 10.34 == '10.34'

# %c Character format.
"%c" % 34 == '"'

# %r Repr format (debugging format).
"%r" % int == "<type 'int'>"

# %s String format.
"%s there" % 'hi' == 'hi there'

# %% A percent sign.
"%g%%" % 10.34 == '10.34%'

# Operators
# =========

# + Addition
print 2 + 4

# - Substraction
print 2 - 4

# * Multiplication
print 2 * 4

# ** Power of
print 2 ** 4

# / Division
print 2 / 4.0

# // Floor division
print 2 // 4.0

# % String interpolate or modulus
print 2 % 4

# < Less than
print 4 < 4

# > Greater than
print 4 > 4 

# <= Less than equal
print 4 <= 4

# >= Greater than equal
print 4 >= 4

# == Equal
print 4 == 5

# != Not equal
print 4 != 5

# <> Not equal
print 4 <> 4

# () Parenthesis
print len('hi')

# [] List brackets
print [1, 3, 4]

# {} Dict curly braces
print {'x': 5, 'y': 10}

# @ At (Decorators)
print @classmethod

# , Comma
print range(0,10)

# : Colon
print "def X():"

# . Dot
print "self.x = 10"

# = Assign equal
print x = 10

# ; semi-colon
print "hi"; print "there"

# += Add and assign
x = 1; x +=2; print x

# -= Substract and assign
x = 1; x -= 2; print x

# *= Multiply and assign
x = 1; x *=2; print x

# /= Divide and assign
x = 1; x /= 2; print x

# //= Floor divide and assign
x = 1; x //= 2; print x

# %= Modulus assign
x = 1; print x %= 2

# **= Power assign
x = 1; x **= 2; print x

