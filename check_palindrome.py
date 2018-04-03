#!/usr/intel/bin/python

st = raw_input('Enter a string\n')
club_st = ''.join(st.split())
#club_st = ' '.join(st)
if (len(club_st) % 2 == 0):
	mid = len(club_st)/2
else:
	mid = (len(club_st) - 1)/2
for i in range(mid):
	if (club_st[i] != club_st[len(club_st) - 1 - i]):
		print 'Not a Palindrome!'
		break
else:
	print '{} is a palindrome!\n'.format(st)
	
