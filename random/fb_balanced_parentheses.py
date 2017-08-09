def is_balanced(s):
	stk = []
	for i in s:
		if i == '(':
			stk.append(i)
		if i == ')':
			if stk:
				stk.pop()
			else:
				return False
	return True

def solution(s):
	balanced = ''
	if is_balanced(s):
		return s
	else:
		stk = []
		lstk = []
		for i in s:
			if i != ')':
				if i == '(':
					stk.append(i)
				else:
					lstk.append(i)
			else:
				if stk:
					balanced+=stk.pop()
					if lstk:
						balanced+=lstk.pop()
					balanced+= i
	return balanced
