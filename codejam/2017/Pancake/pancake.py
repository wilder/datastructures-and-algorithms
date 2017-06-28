def all_happy(s):
	return '-' not in s
	#return re.match(r'^\++$',s ) != None

def should_flip(pk):
	return '-' in pk and pk[0] != '+'

def flip(p, i, k):
	replaced = ''
	for x, s in enumerate(p):
		if x >= i and x <k+i:
			if s == '+':
				replaced+='-'
			else:
				replaced+='+'
		else:
			replaced+=s
	return replaced


def test():
	assert flip('++++---', 1, 4) == '+---+--', 'flip nao passou'
	assert flip('+++++++', 0, len('+++++++')) == '-------', 'flip2 nao passou'
	assert should_flip('-+-') == True, 'should_flip n passou'
	assert should_flip('--+') == True, 'should_flip2 n passou'
	assert should_flip('---') == True, 'should_flip3 n passou'
	assert should_flip('+++') == False, 'should_flip n passou'
	assert all_happy('++++') == True, 'not happy'
	assert all_happy('----') == False, 'not happy'
	assert all_happy('--++') == False, 'not happy'


def main():
	t = int(raw_input()) #case
	for t in range (1, t+1):
		counter = 0
		input = raw_input().split()
		pancakes = input[0]
		k = int(input[1])
		#print pancakes
		if all_happy(pancakes):
			print "Case #{}: {}".format(t, 0)
			continue

		else:
			i = 0
			while i + k < len(pancakes) +1:
				#print str(i+k) + " < " + str(len(pancakes))
				if should_flip(pancakes[i:i+k]):
					pancakes = flip(pancakes, i, k)
					#print pancakes
					counter+=1
				i+=1
				#print str(t) + " "+pancakes+"\n\n"

		print "Case #{}: {}".format(t, counter if all_happy(pancakes) else 'impossible' )
		#print '\n\n\n'

if __name__ == '__main__':
	main()
	test()