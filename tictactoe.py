p1key = raw_input('Player1: Do you want to play with X or O?\n')
if (p1key == 'X'):
	p2key = 'O'
elif (p1key == 'O'):
	p2key = 'X'
else:
	print 'Invalid Input! Please enter X or O, Player1!!!!!!\n'

#dic = { '1' : 'one', '2': 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine' }

dic = ['','one','two','three','four','five','six','seven','eight','nine']
#ready = raw_input('Do you want to play? Enter y or n\n')
print "Let's Start Playing Tic-Tac-Toe...\n"

def make_board(dic):
	board = {
	'row1' : "{} | {} | {} ".format(dic[7], dic[8], dic[9]),
	'row2' : "{} | {} | {} ".format(dic[4],dic[5], dic[6]),
	'row3' : "{} | {} | {} ".format(dic[1],dic[2], dic[3])
	}
	row1 = [dic[7],dic[8],dic[9]]
	row2 = [dic[4],dic[5],dic[6]]
	row3 = [dic[1],dic[2],dic[3]]
	col1 = [dic[7],dic[4],dic[1]]
	col2 = [dic[8],dic[5],dic[2]]
	col3 = [dic[9],dic[6],dic[3]]
	diag1 = [dic[7],dic[5],dic[3]]
	diag2 = [dic[9],dic[5],dic[1]]

	tictactoe = \
	"	{}  \n \
	\n\
	 {}   \n\
         \n\
	 {}   \
	         \n\
	".format(board['row1'], board['row2'], board['row3'])
	
	print tictactoe
	if ((row1 == ['X','X','X']) or 	(row2 == ['X','X','X']) or (row3 == ['X','X','X']) or (col1 == ['X','X','X']) or (col2 == ['X','X','X']) or (col3 == ['X','X','X']) or (diag1 == ['X','X','X']) or (diag2 == ['X','X','X'])):
		print 'Player1 -- Congratulations! You won the game!!'
		more = raw_input('Do you want to play once more? Say y or n\n')
		if (more == 'y'):
			return 'y'	
		else:
			return 'n'
	elif ((row1 == ['O','O','O']) or (row2 == ['O','O','O']) or (row3 == ['O','O','O']) or (col1 == ['O','O','O']) or (col2 == ['O','O','O']) or (col3 == ['O','O','O']) or (diag1 == ['O','O','O']) or (diag2 == ['O','O','O'])):
		print 'Player2 -- Congratulations! You won the game!!'
		more = raw_input('Do you want to play once more? Say y or n\n')
		if (more == 'y'):
			return 'y'
		else:
			return 'n'


times = 1
while (times <= 5):
	print 'This is time {}...'.format(times)	
	p1pos = int(raw_input('Enter your position, player 1... (1-9)\n'))
	if (dic[p1pos] != p1key):
		dic[p1pos] = p1key
	else:
		print 'This position is taken already! Enter something else!'
	b = make_board(dic)
	times = times + 1
	if (b == 'n'):
		break
	elif (b == 'y'):
		times = 1
		dic = ['','one','two','three','four','five','six','seven','eight','nine']
		continue	
	if (times <= 5):
		p2pos = int(raw_input('Enter your position, player 2... (1-9)\n'))
		if (p2pos == p1pos or dic[p2pos] == p2key):
			print 'This position is taken already! Enter something else!'
		dic[p2pos] = p2key
		b = make_board(dic)
		if (b == 'n'):
			break
		elif (b == 'y'):
			times = 1
			dic = ['','one','two','three','four','five','six','seven','eight','nine']
			continue

if (times == 6):
	print "It's a tie! Neither player won :("
	

