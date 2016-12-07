# Exercise 44: Inheritance Versus Composition
# Composition

class Other(object):
	
	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, BEFORE OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

# I could then ask myself if I need this Other to be a class, and could I just make it into a module named other.py?

"""
# When to use Inheritance or Composition
# 1. Avoid multiple inheritance as much as possible.
# 2. Use composition to package code into modules that are used in many different unrelated places and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
"""
