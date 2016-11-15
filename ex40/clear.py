# Exercise 40:
import subprocess

def clear():
	tmp = subprocess.call('clear', shell=True)

for i in range(10):
	print str(i) * 10

print "Now press RETURN and I'll clear the screen."
raw_input("> ")
clear()

