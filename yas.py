import os
import sys

ring = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20"

ring_split = ring.split(",")

for x in ring_split:
	print "ints to conver to hex: " + x

hex_ord_values = []
hex_string_values = []

for x in ring_split:
	x = int(x)
	x = hex(x)

	hex_ord_values.append(x)

	x = str(x)
	hex_string_values.append(x)

print "-----"

for xx in hex_ord_values:
	print "Hex ordinal Values: " + str(xx)

print "------"

for xxx in hex_string_values:
	print "Hex String Values: " + xxx
