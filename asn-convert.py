#!/usr/bin/python

import sys

def asdot2plain( asdot ):
	"This returns an ASPLAIN formated ASN given an ASDOT+ format"
	left,right= asdot.split('.')
	ret = int(left) * 65536 + int(right)
	return ret

def asplain2asdot( asplain ):
	"This returns an ASDOT+ formated ASN given an ASPLAIN format"
	begin = int(asplain)
	current = begin
	new = current
	counter = 0
	while current > 65535:
		new = current - 65536;
		counter = counter + 1
		current = new
	ret = str(counter) + "." + str(new)
	return ret

def main():
	length = len(sys.argv)

	if length == 2:
		start = sys.argv[1]
		if "." not in start:
			print "Start is ASPLAIN: ", start
			print asplain2asdot( start )
		else:
			print "Start is ASDOT+: ", start
			print asdot2plain( start )
	else:
		print "Usage:"
		print sys.argv[0] + " <asn>"
		print ""
		print "    <asn> - ASN to convert in ASPLAIN or ASDOT format"
		print ""

if __name__ == "__main__":
    main()
