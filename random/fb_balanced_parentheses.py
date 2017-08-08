def solution(s):
	balanced = ''
	stk = []
	for i in s:
		if i != ')':
			balanced += i
			if i == '(':
				stk.append(i)
		else:
			if stk:
				stk.pop()
				balanced += i
	return balanced
