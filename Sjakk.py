import copy
'''
pos = [                  #opp ned
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
	['*', '♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜', '*'], 
	['*', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '*'], 
	['*', '♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖', '*'], 
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]
'''
pos = [                  #opp ned
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
	['*', '-', '♜', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '♖', '-', '*'], 
	['*', '♟', '-', '-', '-', '♖', '-', '-', '♟', '*'], 
	['*', '-', '♚', '♟', '-', '-', '♟', '-', '-', '*'], 
	['*', '♙', '-', '-', '-', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '♙', '-', '-', '-', '♙', '*'], 
	['*', '-', '-', '-', '♗', '-', '-', '-', '-', '*'], 
	['*', '-', '-', '-', '-', '-', '-', '-', '♔', '*'], 
	['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]
pos2 = []
pos3 = []
danger1 = [                  #opp ned
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[1, 1, 1, 1, 1, 1, 1, 1], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
]
danger2 = [                  #opp ned
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[1, 1, 1, 1, 1, 1, 1, 1], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
]
typ1 = [
	'♟', 
	'♜', 
	'♞',
	'♝', 
	'♛', 
	'♚'
]
typ2 = [
	'♙', 
	'♖', 
	'♘', 
	'♗', 
	'♕', 
	'♔'
]
grave1 = []
grave2 = []
kong1 = [5, 2]
kong2 = [8, 8]
kongm = False
i = 1
#a = bonde
#b = tårn
#c = hest
#d = biskop
#r = dronning
#k = konge
# stor bokstav = svart
# posisjon = bokstav, tall
# legal: n, stop: motsatt, illegal: a,b,c,d,r,k i samme
#♖, ♜, ♗, ♝, ♘, ♞, ♕, ♛, ♔, ♚, ♙, ♟

def main():
	global pos, pos3, kongm
	print('I dette sjakkspillet skriver du først bokstav, så tall.')
	play = True
	print_board()
	updateB()
	updateK()
	while play:
		t = 0
		y = 0
		turn1 = True
		while turn1:
			print("Hvilken brikke vil du flytte?", end=' ')
			fra = str(inputter())
			fra = [int(fra[1]), bokstav(fra[0])]
			if legal_move1(fra):
				turn1 = False
			possibility = test(fra)
			if len(possibility) == 0:
				turn1 = True
		printoption(possibility)
		turn = True
		while turn:
			print("Hvor vil du flytte den?", end=' ')
			til = str(inputter())                #passer på at input  (til) er gyldig
			if til in possibility:
				turn = False
		til = [int(til[1]), bokstav(til[0])]
		if pos[fra[0]][fra[1]] == typ1[5] or pos[fra[0]][fra[1]] == typ2[5]:
			kongm = True
		move(fra, til)
		updateB()
		updateK()
		printgrave(grave1)
		print_board()
		printgrave(grave2)
		play = sjekk_matt()
		pos = copy.deepcopy(pos3)


def updateB():
	global danger2, i
	danger2 = [                  #opp ned
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	]
	if i % 2 == 0:
		for g in range(1, 9):
			for h in range(1, 9):
				a = [g, h]
				if len(test2(a)) != 0:
					for l in test2(a):
						danger2[int(l[1]) - 1][int(bokstav(l[0])) - 1] += 1
	else:
		i += 1
		for g in range(1, 9):
			for h in range(1, 9):
				a = [g, h]
				if len(test2(a)) != 0:
					for l in test2(a):
						danger2[int(l[1]) - 1][int(bokstav(l[0])) - 1] += 1
		i -= 1


def updateK():
	global danger1, i
	danger1 = [                  #opp ned
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	]
	if i % 2 != 0:
		for g in range(1, 9):
			for h in range(1, 9):
				a = [g, h]
				if len(test2(a)) != 0:
					for l in test2(a):
						danger1[int(l[1]) - 1][int(bokstav(l[0])) - 1] += 1
	else:
		i += 1
		for g in range(1, 9):
			for h in range(1, 9):
				a = [g, h]
				if len(test2(a)) != 0:
					for l in test2(a):
						danger1[int(l[1]) - 1][int(bokstav(l[0])) - 1] += 1
		i -= 1


def inputter():        #funksjon som stopper programmet dersom input er i en liste (stopp, inne i funksjonen)
	stopp = ['stop', 'stopp', 'exit', 'avslutt']
	stopp1 = ['resign', 'gi opp', 'defeat']
	a = input()
	if a.lower() in stopp:
		print('Thanks for playing!')
		exit()
	elif a.lower() in stopp1:
		if i % 2 == 0:
			print("Svart gir opp; hvit vinner!")
			exit()
		else:
			print("Hvit gir opp; svart vinner!")
			exit()
	else:
		return a


def sjekk_matt():    #uferdig! Sjekker om kongen er død, eller det er sjakk matt.
	global pos, pos3
	pos3 = copy.deepcopy(pos)
	a = 0
	b = 0
	if typ1[5] in grave1:
		print('Svart vinner!')
		return False
	elif typ2[5] in grave2:
		print('Hvit vinner!')
		return False
	for tre in range(1, 9):
		for fire in range(1, 9):
			if i % 2 == 0:
				if pos[tre][fire] in typ2:
					a += len(test([tre, fire]))
			else:
				if pos[tre][fire] in typ1:
					b += len(test([tre, fire]))
	if a == 0 and i % 2 == 0:
		print('Hvit vinner!')
		return False
	elif b == 0 and i % 2 != 0:
		print('Svart vinner!')
		return False
	else:
		return True


def bokstav(bok):     #gjør bokstav om til tilsvarende tall
	if bok == 'a':
		return 1
	elif bok == 'b':
		return 2
	elif bok == 'c':
		return 3
	elif bok == 'd':
		return 4
	elif bok == 'e':
		return 5
	elif bok == 'f':
		return 6
	elif bok == 'g':
		return 7
	elif bok == 'h':
		return 8


def tall(bok):       #gjør tall om til tilsvarende bokstav
	if bok == 1:
		return 'a'
	elif bok == 2:
		return 'b'
	elif bok == 3:
		return 'c'
	elif bok == 4:
		return 'd'
	elif bok == 5:
		return 'e'
	elif bok == 6:
		return 'f'
	elif bok == 7:
		return 'g'
	elif bok == 8:
		return 'h'


def print_board():    #funksjonelt ferdig; printer brettet
	for i in range(10):
		for j in range(10):
			print(pos[9 - i][j], end='  ')
		print('\n')


# move-funksjonene med 2-tall er kun for å analysere brettet og gi farenivå


def bond_move2(fra):    #gir tilbake mulige moves for en bonde
	possible = []
	if pos[fra[0]][fra[1]] in typ2:
		if fra[0] - 1 > 0 and fra[0] - 1 < 9:
			if fra[1] + 1 > 0 and fra[1] + 1 < 9:
				possible.append(str(tall(fra[1] + 1)) + str(fra[0] - 1))
			if fra[1] - 1 > 0 and fra[1] - 1 < 9:
				possible.append(str(tall(fra[1] - 1)) + str(fra[0] - 1))
	else:
		if fra[0] + 1 > 0 and fra[0] + 1 < 9:
			if fra[1] + 1 > 0 and fra[1] + 1 < 9:
				possible.append(str(tall(fra[1] + 1)) + str(fra[0] + 1))
			if fra[1] - 1 > 0 and fra[1] - 1 < 9:
				possible.append(str(tall(fra[1] - 1)) + str(fra[0] + 1))
	return possible


def tower_move2(fra):   #gir mulige for tårn
	possibility = []
	a = True
	b = True
	c = True
	d = True
	for j in range(fra[0] + 1, 9):
		if pos[j][fra[1]] == '-' and a:
			possibility.append(tall(fra[1]) + str(j))
		elif (pos[j][fra[1]] in typ2 or typ1) and a:
			possibility.append(tall(fra[1]) + str(j))
			a = False
		else:
			a = False
	for j in range(1, fra[0]):
		if pos[fra[0] - j][fra[1]] == '-' and b:
			possibility.append(tall(fra[1]) + str(fra[0] - j))
		elif (pos[fra[0] - j][fra[1]] in typ2 or typ1) and b:
			possibility.append(tall(fra[1]) + str(fra[0] - j))
			b = False
		else:
			b = False
	for j in range(1, fra[1]):
		if pos[fra[0]][fra[1] - j] == '-' and c:
			possibility.append(tall(fra[1] - j) + str(fra[0]))
		elif (pos[fra[0]][fra[1] - j] in typ2 or typ1) and c:
			possibility.append(tall(fra[1] - j) + str(fra[0]))
			c = False
		else:
			c = False
	for j in range(fra[1] + 1, 9):
		if pos[fra[0]][j] == '-' and d:
			possibility.append(tall(j) + str(fra[0]))
		elif (pos[fra[0]][j] in typ2 or typ1) and d:
			possibility.append(tall(j) + str(fra[0]))
			d = False
		else:
			d = False
	return possibility


def horse_move2(fra):   #hest, horse, springer
	possibility = [
		[str(fra[0] + 2), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] - 1)],
		[str(fra[0] + 1), str(fra[1] + 2)],
		[str(fra[0] + 1), str(fra[1] - 2)],
		[str(fra[0] - 1), str(fra[1] + 2)],
		[str(fra[0] - 1), str(fra[1] - 2)],
	]
	b = []
	for j in range(len(possibility)):
		c = []
		for pos2 in possibility[j]:
			if int(pos2) > 0 and int(pos2) < 9:
				c.append(pos2)
			if len(c) == 2:
				b.append(possibility[j])
	e = []
	for pl in b:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	return e


def bishop_move2(fra):
	possibility1 = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] + 2)],
		[str(fra[0] + 3), str(fra[1] + 3)],
		[str(fra[0] + 4), str(fra[1] + 4)],
		[str(fra[0] + 5), str(fra[1] + 5)],
		[str(fra[0] + 6), str(fra[1] + 6)],
		[str(fra[0] + 7), str(fra[1] + 7)],
	]
	possibility2 = [
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] - 2)],
		[str(fra[0] - 3), str(fra[1] - 3)],
		[str(fra[0] - 4), str(fra[1] - 4)],
		[str(fra[0] - 5), str(fra[1] - 5)],
		[str(fra[0] - 6), str(fra[1] - 6)],
		[str(fra[0] - 7), str(fra[1] - 7)],
	]
	possibility3 = [
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 2), str(fra[1] - 2)],
		[str(fra[0] + 3), str(fra[1] - 3)],
		[str(fra[0] + 4), str(fra[1] - 4)],
		[str(fra[0] + 5), str(fra[1] - 5)],
		[str(fra[0] + 6), str(fra[1] - 6)],
		[str(fra[0] + 7), str(fra[1] - 7)],
	]
	possibility4 = [
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] + 2)],
		[str(fra[0] - 3), str(fra[1] + 3)],
		[str(fra[0] - 4), str(fra[1] + 4)],
		[str(fra[0] - 5), str(fra[1] + 5)],
		[str(fra[0] - 6), str(fra[1] + 6)],
		[str(fra[0] - 7), str(fra[1] + 7)],
	]
	possibility = []
	c = 0
	plep = True
	for k in possibility1:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif pos[int(k[0])][int(k[1])] in typ1 or typ2:
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility2:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif pos[int(k[0])][int(k[1])] in typ1 or typ2:
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility3:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif pos[int(k[0])][int(k[1])] in typ1 or typ2:
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility4:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif pos[int(k[0])][int(k[1])] in typ1 or typ2:
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	e = []
	for pl in possibility:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	return e


def king_move2(fra):    
	possibility = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 1), str(fra[1])],
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 1), str(fra[1])],
		[str(fra[0]), str(fra[1] + 1)],
		[str(fra[0]), str(fra[1] - 1)],
	]
	b = []
	for j in range(len(possibility)):
		c = []
		for pos2 in possibility[j]:
			if int(pos2) > 0 and int(pos2) < 9:
				c.append(pos2)
			if len(c) == 2:
				b.append(possibility[j])
	e = []
	for pl in b:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	if len(e) > 0:
		kongm = True
	return e


def queen_move2(fra):
	possible = []
	a = True
	b = True
	c = True
	d = True
	for j in range(fra[0] + 1, 9):
		if pos[j][fra[1]] == '-' and a:
			possible.append(tall(fra[1]) + str(j))
		elif (pos[j][fra[1]] in typ2 or typ1) and a:
			possible.append(tall(fra[1]) + str(j))
			a = False
		else:
			a = False
	for j in range(1, fra[0]):
		if pos[fra[0] - j][fra[1]] == '-' and b:
			possible.append(tall(fra[1]) + str(fra[0] - j))
		elif (pos[fra[0] - j][fra[1]] in typ2 or typ1) and b:
			possible.append(tall(fra[1]) + str(fra[0] - j))
			b = False
		else:
			b = False
	for j in range(1, fra[1]):
		if pos[fra[0]][fra[1] - j] == '-' and c:
			possible.append(tall(fra[1] - j) + str(fra[0]))
		elif (pos[fra[0]][fra[1] - j] in typ2 or typ1) and c:
			possible.append(tall(fra[1] - j) + str(fra[0]))
			c = False
		else:
			c = False
	for j in range(fra[1] + 1, 9):
		if pos[fra[0]][j] == '-' and d:
			possible.append(tall(j) + str(fra[0]))
		elif (pos[fra[0]][j] in typ2 or typ1) and d:
			possible.append(tall(j) + str(fra[0]))
			d = False
		else:
			d = False
	possibility1 = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] + 2)],
		[str(fra[0] + 3), str(fra[1] + 3)],
		[str(fra[0] + 4), str(fra[1] + 4)],
		[str(fra[0] + 5), str(fra[1] + 5)],
		[str(fra[0] + 6), str(fra[1] + 6)],
		[str(fra[0] + 7), str(fra[1] + 7)],
	]
	possibility2 = [
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] - 2)],
		[str(fra[0] - 3), str(fra[1] - 3)],
		[str(fra[0] - 4), str(fra[1] - 4)],
		[str(fra[0] - 5), str(fra[1] - 5)],
		[str(fra[0] - 6), str(fra[1] - 6)],
		[str(fra[0] - 7), str(fra[1] - 7)],
	]
	possibility3 = [
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 2), str(fra[1] - 2)],
		[str(fra[0] + 3), str(fra[1] - 3)],
		[str(fra[0] + 4), str(fra[1] - 4)],
		[str(fra[0] + 5), str(fra[1] - 5)],
		[str(fra[0] + 6), str(fra[1] - 6)],
		[str(fra[0] + 7), str(fra[1] - 7)],
	]
	possibility4 = [
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] + 2)],
		[str(fra[0] - 3), str(fra[1] + 3)],
		[str(fra[0] - 4), str(fra[1] + 4)],
		[str(fra[0] - 5), str(fra[1] + 5)],
		[str(fra[0] - 6), str(fra[1] + 6)],
		[str(fra[0] - 7), str(fra[1] + 7)],
	]
	possibility = []
	c_1 = 0
	plep = True
	for k_1 in possibility1:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif pos[int(k_1[0])][int(k_1[1])] in typ1 or typ2:
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility2:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif pos[int(k_1[0])][int(k_1[1])] in typ1 or typ2:
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility3:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif pos[int(k_1[0])][int(k_1[1])] in typ1 or typ2:
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility4:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif pos[int(k_1[0])][int(k_1[1])] in typ1 or typ2:
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	e = []
	for pl in possibility:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	for kl in possible:
		e.append(kl)
	return e


def bond_move(fra):    #gir tilbake mulige moves for en bonde 
	possible = []
	if pos[fra[0]][fra[1]] in typ2:
		if pos[fra[0] - 1][fra[1]] == '-':
			possible.append(str(tall(fra[1])) + str(fra[0] - 1))
		if fra[0] == 7 and pos[fra[0] - 2][fra[1]] == '-':
			possible.append(str(tall(fra[1])) + str(fra[0] - 2))
		if pos[fra[0] - 1][fra[1] + 1] in typ1:
			possible.append(str(tall(fra[1] + 1)) + str(fra[0] - 1))
		if pos[fra[0] - 1][fra[1] - 1] in typ1:
			possible.append(str(tall(fra[1] - 1)) + str(fra[0] - 1))
	else:
		if pos[fra[0] + 1][fra[1]] == '-':
			possible.append(str(tall(fra[1])) + str(fra[0] + 1))
		if fra[0] == 2 and pos[fra[0] + 2][fra[1]] == '-':
			possible.append(str(tall(fra[1])) + str(fra[0] + 2))
		if pos[fra[0] + 1][fra[1] + 1] in typ2:
			possible.append(str(tall(fra[1] + 1)) + str(fra[0] + 1))
		if pos[fra[0] + 1][fra[1] - 1] in typ2:
			possible.append(str(tall(fra[1] - 1)) + str(fra[0] + 1))
	a = []
	if i % 2 == 0:
		for kl in possible:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[kong2[0] - 1][kong2[1] - 1] == 0:
				a.append(kl)
	elif i % 2 != 0:
		for kl in possible:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger2[kong1[0] - 1][kong1[1] - 1] == 0:
				a.append(kl)
	else:
		a = possible
	return a


def test_move(fra, til):
	global pos, kongm, pos2
	pos2 = copy.deepcopy(pos)
	pos[til[0]][til[1]] = pos[fra[0]][fra[1]]
	pos[fra[0]][fra[1]] = '-'
	if kongm:
		if i % 2 == 0:
			kong2 = [til[0], til[1]]
		else:
			kong1 = [til[0], til[1]]
		kongm = False
	updateB()
	updateK()
	pos = copy.deepcopy(pos2)
	

def tower_move(fra):   #gir mulige for tårn
	possibility = []
	a = True
	b = True
	c = True
	d = True
	for j in range(fra[0] + 1, 9):
		if pos[j][fra[1]] == '-' and a:
			possibility.append(tall(fra[1]) + str(j))
		elif (pos[j][fra[1]] in typ2 and i % 2 != 0 and a) or (pos[j][fra[1]] in typ1 and i % 2 == 0 and a):
			possibility.append(tall(fra[1]) + str(j))
			a = False
		else:
			a = False
	for j in range(1, fra[0]):
		if pos[fra[0] - j][fra[1]] == '-' and b:
			possibility.append(tall(fra[1]) + str(fra[0] - j))
		elif (pos[fra[0] - j][fra[1]] in typ2 and i % 2 != 0 and b) or (pos[fra[0] - j][fra[1]] in typ1 and i % 2 == 0 and b):
			possibility.append(tall(fra[1]) + str(fra[0] - j))
			b = False
		else:
			b = False
	for j in range(1, fra[1]):
		if pos[fra[0]][fra[1] - j] == '-' and c:
			possibility.append(tall(fra[1] - j) + str(fra[0]))
		elif (pos[fra[0]][fra[1] - j] in typ2 and i % 2 != 0 and c) or (pos[fra[0]][fra[1] - j] in typ1 and i % 2 == 0 and c):
			possibility.append(tall(fra[1] - j) + str(fra[0]))
			c = False
		else:
			c = False
	for j in range(fra[1] + 1, 9):
		if pos[fra[0]][j] == '-' and d:
			possibility.append(tall(j) + str(fra[0]))
		elif ((pos[fra[0]][j] in typ2) and i % 2 != 0 and d) or ((pos[fra[0]][j] in typ1) and i % 2 == 0 and d):
			possibility.append(tall(j) + str(fra[0]))
			d = False
		else:
			d = False
	ter = []
	if i % 2 == 0:
		for kl in possibility:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[kong2[0] - 1][kong2[1] - 1] == 0:
				ter.append(kl)
	elif i % 2 != 0:
		for kl in possibility:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger2[kong1[0] - 1][kong1[1] - 1] == 0:
				ter.append(kl)
	else:
		ter = possibility
	return ter


def horse_move(fra):   #hest, horse, springer
	possibility = [
		[str(fra[0] + 2), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] - 1)],
		[str(fra[0] + 1), str(fra[1] + 2)],
		[str(fra[0] + 1), str(fra[1] - 2)],
		[str(fra[0] - 1), str(fra[1] + 2)],
		[str(fra[0] - 1), str(fra[1] - 2)],
	]
	b = []
	for j in range(len(possibility)):
		c = []
		for pos2 in possibility[j]:
			if int(pos2) > 0 and int(pos2) < 9:
				c.append(pos2)
			if len(c) == 2:
				b.append(possibility[j])
	d = []
	for y in b:
		if pos[int(y[0])][int(y[1])] == '-':
			d.append(y)
		elif pos[int(y[0])][int(y[1])] in typ2 and i % 2 != 0:
			d.append(y) 
		elif pos[int(y[0])][int(y[1])] in typ1 and i % 2 == 0:
			d.append(y)
	e = []
	for pl in d:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	ter = []
	if i % 2 == 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[kong2[0] - 1][kong2[1] - 1] == 0:
				ter.append(kl)
	elif i % 2 != 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger2[kong1[0] - 1][kong1[1] - 1] == 0:
				ter.append(kl)
	else:
		ter = e
	return ter


def bishop_move(fra):
	possibility1 = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] + 2)],
		[str(fra[0] + 3), str(fra[1] + 3)],
		[str(fra[0] + 4), str(fra[1] + 4)],
		[str(fra[0] + 5), str(fra[1] + 5)],
		[str(fra[0] + 6), str(fra[1] + 6)],
		[str(fra[0] + 7), str(fra[1] + 7)],
	]
	possibility2 = [
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] - 2)],
		[str(fra[0] - 3), str(fra[1] - 3)],
		[str(fra[0] - 4), str(fra[1] - 4)],
		[str(fra[0] - 5), str(fra[1] - 5)],
		[str(fra[0] - 6), str(fra[1] - 6)],
		[str(fra[0] - 7), str(fra[1] - 7)],
	]
	possibility3 = [
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 2), str(fra[1] - 2)],
		[str(fra[0] + 3), str(fra[1] - 3)],
		[str(fra[0] + 4), str(fra[1] - 4)],
		[str(fra[0] + 5), str(fra[1] - 5)],
		[str(fra[0] + 6), str(fra[1] - 6)],
		[str(fra[0] + 7), str(fra[1] - 7)],
	]
	possibility4 = [
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] + 2)],
		[str(fra[0] - 3), str(fra[1] + 3)],
		[str(fra[0] - 4), str(fra[1] + 4)],
		[str(fra[0] - 5), str(fra[1] + 5)],
		[str(fra[0] - 6), str(fra[1] + 6)],
		[str(fra[0] - 7), str(fra[1] + 7)],
	]
	possibility = []
	c = 0
	plep = True
	for k in possibility1:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif (pos[int(k[0])][int(k[1])] in typ1 and i % 2 == 0) or (pos[int(k[0])][int(k[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility2:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif (pos[int(k[0])][int(k[1])] in typ1 and i % 2 == 0) or (pos[int(k[0])][int(k[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility3:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif (pos[int(k[0])][int(k[1])] in typ1 and i % 2 == 0) or (pos[int(k[0])][int(k[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	c = 0
	plep = True
	for k in possibility4:
		c = 0
		if int(k[0]) > 0 and int(k[0]) < 9:
			c += 1
		if int(k[1]) > 0 and int(k[1]) < 9:
			c += 1
		if c == 2:	
			if plep and pos[int(k[0])][int(k[1])] == '-':
				possibility.append(k)
			elif (pos[int(k[0])][int(k[1])] in typ1 and i % 2 == 0) or (pos[int(k[0])][int(k[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k)
					plep = False
			else:
				plep = False
		if c != 2:
			plep = False
	e = []
	for pl in possibility:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	ter = []
	if i % 2 == 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[kong2[0] - 1][kong2[1] - 1] == 0:
				ter.append(kl)
	elif i % 2 != 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger2[kong1[0] - 1][kong1[1] - 1] == 0:
				ter.append(kl)
	else:
		ter = e
	return ter


def king_move(fra):    #HUSK: dersom du lar folk gå tilbake når de har valgt en bevegbar brikke, må du endre koden som sier når kongen beveger seg!
	global kongm
	possibility = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 1), str(fra[1])],
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 1), str(fra[1])],
		[str(fra[0]), str(fra[1] + 1)],
		[str(fra[0]), str(fra[1] - 1)],
	]
	b = []
	for j in range(len(possibility)):
		c = []
		for pos2 in possibility[j]:
			if int(pos2) > 0 and int(pos2) < 9:
				c.append(pos2)
			if len(c) == 2:
				b.append(possibility[j])
	d = []
	for y in b:
		if pos[int(y[0])][int(y[1])] == '-':
			d.append(y)
		elif pos[int(y[0])][int(y[1])] in typ2 and i % 2 != 0:
			d.append(y) 
		elif pos[int(y[0])][int(y[1])] in typ1 and i % 2 == 0:
			d.append(y)
	a = []
	for u in d:
		if danger2[int(u[0]) - 1][int(u[1]) - 1] == 0 and i % 2 != 0:
			a.append(u)
		elif danger1[int(u[0]) - 1][int(u[1]) - 1] == 0 and i % 2 == 0:
			a.append(u)
	e = []
	for pl in a:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	ter = []
	if i % 2 == 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[til[0] - 1][til[1] - 1] == 0:
				ter.append(kl)
	elif i % 2 != 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			if danger2[til[0] - 1][til[1] - 1] == 0:
				ter.append(kl)
	return ter


def queen_move(fra):
	possible = []
	a = True
	b = True
	c = True
	d = True
	for j in range(fra[0] + 1, 9):
		if pos[j][fra[1]] == '-' and a:
			possible.append(tall(fra[1]) + str(j))
		elif (pos[j][fra[1]] in typ2 and i % 2 != 0 and a) or (pos[j][fra[1]] in typ1 and i % 2 == 0 and a):
			possible.append(tall(fra[1]) + str(j))
			a = False
		else:
			a = False
	for j in range(1, fra[0]):
		if pos[fra[0] - j][fra[1]] == '-' and b:
			possible.append(tall(fra[1]) + str(fra[0] - j))
		elif (pos[fra[0] - j][fra[1]] in typ2 and i % 2 != 0 and b) or (pos[fra[0] - j][fra[1]] in typ1 and i % 2 == 0 and b):
			possible.append(tall(fra[1]) + str(fra[0] - j))
			b = False
		else:
			b = False
	for j in range(1, fra[1]):
		if pos[fra[0]][fra[1] - j] == '-' and c:
			possible.append(tall(fra[1] - j) + str(fra[0]))
		elif (pos[fra[0]][fra[1] - j] in typ2 and i % 2 != 0 and c) or (pos[0][fra[1] - j] in typ1 and i % 2 == 0 and c):
			possible.append(tall(fra[1] - j) + str(fra[0]))
			c = False
		else:
			c = False
	for j in range(fra[1] + 1, 9):
		if pos[fra[0]][j] == '-' and d:
			possible.append(tall(j) + str(fra[0]))
		elif ((pos[fra[0]][j] in typ2) and i % 2 != 0 and d) or ((pos[fra[0]][j] in typ1) and i % 2 == 0 and d):
			possible.append(tall(j) + str(fra[0]))
			d = False
		else:
			d = False
	possibility1 = [
		[str(fra[0] + 1), str(fra[1] + 1)],
		[str(fra[0] + 2), str(fra[1] + 2)],
		[str(fra[0] + 3), str(fra[1] + 3)],
		[str(fra[0] + 4), str(fra[1] + 4)],
		[str(fra[0] + 5), str(fra[1] + 5)],
		[str(fra[0] + 6), str(fra[1] + 6)],
		[str(fra[0] + 7), str(fra[1] + 7)],
	]
	possibility2 = [
		[str(fra[0] - 1), str(fra[1] - 1)],
		[str(fra[0] - 2), str(fra[1] - 2)],
		[str(fra[0] - 3), str(fra[1] - 3)],
		[str(fra[0] - 4), str(fra[1] - 4)],
		[str(fra[0] - 5), str(fra[1] - 5)],
		[str(fra[0] - 6), str(fra[1] - 6)],
		[str(fra[0] - 7), str(fra[1] - 7)],
	]
	possibility3 = [
		[str(fra[0] + 1), str(fra[1] - 1)],
		[str(fra[0] + 2), str(fra[1] - 2)],
		[str(fra[0] + 3), str(fra[1] - 3)],
		[str(fra[0] + 4), str(fra[1] - 4)],
		[str(fra[0] + 5), str(fra[1] - 5)],
		[str(fra[0] + 6), str(fra[1] - 6)],
		[str(fra[0] + 7), str(fra[1] - 7)],
	]
	possibility4 = [
		[str(fra[0] - 1), str(fra[1] + 1)],
		[str(fra[0] - 2), str(fra[1] + 2)],
		[str(fra[0] - 3), str(fra[1] + 3)],
		[str(fra[0] - 4), str(fra[1] + 4)],
		[str(fra[0] - 5), str(fra[1] + 5)],
		[str(fra[0] - 6), str(fra[1] + 6)],
		[str(fra[0] - 7), str(fra[1] + 7)],
	]
	possibility = []
	c_1 = 0
	plep = True
	for k_1 in possibility1:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif (pos[int(k_1[0])][int(k_1[1])] in typ1 and i % 2 == 0) or (pos[int(k_1[0])][int(k_1[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility2:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif (pos[int(k_1[0])][int(k_1[1])] in typ1 and i % 2 == 0) or (pos[int(k_1[0])][int(k_1[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility3:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif (pos[int(k_1[0])][int(k_1[1])] in typ1 and i % 2 == 0) or (pos[int(k_1[0])][int(k_1[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	c_1 = 0
	plep = True
	for k_1 in possibility4:
		c_1 = 0
		if int(k_1[0]) > 0 and int(k_1[0]) < 9:
			c_1 += 1
		if int(k_1[1]) > 0 and int(k_1[1]) < 9:
			c_1 += 1
		if c_1 == 2:	
			if plep and pos[int(k_1[0])][int(k_1[1])] == '-':
				possibility.append(k_1)
			elif (pos[int(k_1[0])][int(k_1[1])] in typ1 and i % 2 == 0) or (pos[int(k_1[0])][int(k_1[1])] in typ2 and i % 2 != 0):
				if plep:
					possibility.append(k_1)
					plep = False
			else:
				plep = False
		if c_1 != 2:
			plep = False
	e = []
	for pl in possibility:
		t = tall(int(pl[1]))
		e.append(str(t) + str(pl[0]))
	for klo in possible:
		e.append(klo)
	ter = []
	if i % 2 == 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger1[kong2[0] - 1][kong2[1] - 1] == 0:
				ter.append(kl)
	elif i % 2 != 0:
		for kl in e:
			til = [int(kl[1]), bokstav(kl[0])]
			test_move(fra, til)
			if danger2[kong1[0] - 1][kong1[1] - 1] == 0:
				ter.append(kl)
	else:
		ter = e
	return ter


def test(fra):
	if not legal_move1(fra):
		return []
	else:
		if pos[fra[0]][fra[1]] in typ1 and i % 2 != 0:
			if pos[fra[0]][fra[1]] == typ1[0]:
				return bond_move(fra)
			elif pos[fra[0]][fra[1]] == typ1[1]:
				return tower_move(fra)
			elif pos[fra[0]][fra[1]] == typ1[2]:
				return horse_move(fra)
			elif pos[fra[0]][fra[1]] == typ1[3]:
				return bishop_move(fra)
			elif pos[fra[0]][fra[1]] == typ1[4]:
				return queen_move(fra)
			elif pos[fra[0]][fra[1]] == typ1[5]:
				return king_move(fra)
			else:
				print("Feil i test-funksjonen, 1")
		elif pos[fra[0]][fra[1]] in typ2 and i % 2 == 0:
			if pos[fra[0]][fra[1]] == typ2[0]:
				return bond_move(fra)
			elif pos[fra[0]][fra[1]] == typ2[1]:
				return tower_move(fra)
			elif pos[fra[0]][fra[1]] == typ2[2]:
				return horse_move(fra)
			elif pos[fra[0]][fra[1]] == typ2[3]:
				return bishop_move(fra)
			elif pos[fra[0]][fra[1]] == typ2[4]:
				return queen_move(fra)
			elif pos[fra[0]][fra[1]] == typ2[5]:
				return king_move(fra)
			else:
				print("Feil i test-funksjonen, 2")


def test2(fra):
	if not legal_move1(fra):
		return []
	else:
		if pos[fra[0]][fra[1]] in typ1 and i % 2 != 0:
			if pos[fra[0]][fra[1]] == typ1[0]:
				return bond_move2(fra)
			elif pos[fra[0]][fra[1]] == typ1[1]:
				return tower_move2(fra)
			elif pos[fra[0]][fra[1]] == typ1[2]:
				return horse_move2(fra)
			elif pos[fra[0]][fra[1]] == typ1[3]:
				return bishop_move2(fra)
			elif pos[fra[0]][fra[1]] == typ1[4]:
				return queen_move2(fra)
			elif pos[fra[0]][fra[1]] == typ1[5]:
				return king_move2(fra)
			else:
				print("Feil i test-funksjonen, 1")
		elif pos[fra[0]][fra[1]] in typ2 and i % 2 == 0:
			if pos[fra[0]][fra[1]] == typ2[0]:
				return bond_move2(fra)
			elif pos[fra[0]][fra[1]] == typ2[1]:
				return tower_move2(fra)
			elif pos[fra[0]][fra[1]] == typ2[2]:
				return horse_move2(fra)
			elif pos[fra[0]][fra[1]] == typ2[3]:
				return bishop_move2(fra)
			elif pos[fra[0]][fra[1]] == typ2[4]:
				return queen_move2(fra)
			elif pos[fra[0]][fra[1]] == typ2[5]:
				return king_move2(fra)
			else:
				print("Feil i test-funksjonen, 2")


def legal_move1(fra):           #sjekker om brikken kan brukes
	if pos[fra[0]][fra[1]] == '-' or pos[fra[0]][fra[1]] == '*':
		return False
	elif pos[fra[0]][fra[1]] in typ1 and i % 2 == 0:
		return False
	elif pos[fra[0]][fra[1]] in typ2 and i % 2 != 0:
		return False
	else:
		return True


def move(fra, til):
	global pos, i, grave1, grave2, kongm, kong1, kong2
	print(kongm)
	dead = pos[til[0]][til[1]]
	pos[til[0]][til[1]] = pos[fra[0]][fra[1]]
	pos[fra[0]][fra[1]] = '-'
	if kongm:
		if i % 2 == 0:
			kong2 = [til[0], til[1]]
		else:
			kong1 = [til[0], til[1]]
		kongm = False
	i += 1
	if i % 2 == 0:
		if dead != '-':
			grave2.append(dead)
		print("Svart sin tur.")
	else:
		if dead != '-':
			grave1.append(dead)
		print("Hvit sin tur.")


def printoption(poss):
	print('Mulige ruter du kan flytte til: ', end='')
	a = len(poss)
	if a == 1:
		print(poss[0] + '.')
	else:
		for tre in poss:
			if a == 2:
				print(tre + ' og ', end='')
				a -= 1
			elif a == 1:
				print(tre + '.')
			else:
				print(tre + ', ', end='')
				a -= 1
 

def printgrave(grave):
	tro = 0
	for klep in grave:
		if tro == len(grave) - 1:
			print(klep)
		elif tro < 7:
			print(klep, end='  ')
			tro += 1
		elif tro == 7:
			print(klep, '\n')
			tro += 1
		else:
			print(klep, end='  ')
			tro += 1


main()