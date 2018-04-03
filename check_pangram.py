import string

def is_pangram(st,alphabet=string.ascii_lowercase):
	for a in alphabet:
		if a not in st:
			print 'Not a Pangram!!'
			break
	else:
		print '{} is a pangram!!'.format(st)

is_pangram('The quick brown fox jumps over the lazy dog')

is_pangram('Lazy me!!')
