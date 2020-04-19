def calc(expression):
	properArr = toProperArr(expression)
	polished = toPolish(properArr)
	return evaluate(polished)

def precedence(char):
	prec = {'^' : 2, '*' : 1, '/' : 1, '+' : 0, '-' : 0, ')' : -1}
	return prec[char]

def toProperArr(string):
	arr = []
	digits = ''
	for idx, val in enumerate(string):
		if val.isdigit() or val == '.':
			digits += val

		elif val != ' ':
			if digits != '':
				arr.append(convDigit(digits))
				digits = ''
			arr.append(val)
	if digits != '':
		arr.append(convDigit(digits))

	return arr

def convDigit(a):
	return int(a) if a.isdigit() else float(a)

def toPolish(string):
	string = string[::-1]
	opr = []
	vals = []
	for idx, val in enumerate(string):
		if isinstance(val, str):
			opr.append(val)
			if val == '(':
				isPar(opr, vals)
			else:
				if val == '-':
					if idx == len(string) - 1:
						isNegative(val, 'end', opr, vals)
					else:
						isNegative(val, string[idx+1], opr, vals)
				else:
					comparePrec(val, opr, vals)
		else:
			vals.append(val)
	
	pol = vals + opr[::-1]
	return pol

def isPar(operators, values):
	iter_opr = iter(reversed(operators))
	while next(iter_opr) != ')':
		if operators[-1] != '(':	values.append(operators[-1])
		operators.pop()
	return operators.pop()

def isNegative(cur, nxt, operators, values):
	if isinstance(nxt, str) and nxt != ')':
		values.append(0)
		values.append('-')
		operators.pop()
	else:
		comparePrec(cur, operators, values)
	return ''

def comparePrec(cur, operators, values):
	iter_opr = iter(reversed(operators))
	if cur == ')' or len(operators) <= 1:
		return ''
	# print('precedence: ' + str(operators))
	# print('current: ' + cur)
	opr1 = precedence(cur)
	opr2 = precedence(operators[-2])
	# print('op1: ' + str(opr1) + ' opr2: ' + str(opr2))
	while opr1 < opr2:
		operators.pop()
		values.append(operators[-1])
		operators.pop()
		# print('current append: ' + str(cur))
		if len(operators) == 0:
			operators.append(cur)
			return ''
		else:
			# print('current last index: ' + str(operators[-1]))
			opr2 = precedence(operators[-1])
			operators.append(cur)
			# print('latest op1: ' + str(opr1) + ' opr2: ' + str(opr2))
	return ''

def evaluate(arr):
	stack = []
	for a in arr:
		if isinstance(a, str):
			if a == '*':
				val = stack[-1] * stack[-2]
				del stack[-2:]
				stack.append(val)
			elif a == '/':
				val = stack[-1] / stack[-2]
				del stack[-2:]
				stack.append(val)
			elif a == '+':
				val = stack[-1] + stack[-2]
				del stack[-2:]
				stack.append(val)
			elif a == '-':
				val = stack[-1] - stack[-2]
				del stack[-2:]
				stack.append(val)
		else:
			stack.append(a)
	print(stack)
	return stack[0]
