def get_token_list(expr):
	l=list(expr)
	operand = str()
	token_list = []
	length = len(expr)
	#print(len(l))
	for token in l:
		#print(token, token_list,operand)
		if token in'()+-*/^':
			if len(operand) == 0:
				token_list.append(token)
			else:
				token_list.append(operand)
				token_list.append(token)
				operand = str()
		elif token == ' ':
			continue
		elif token == '.':
			operand += token
		elif token.isdecimal():
			operand += token
	if operand is not None and token.isdecimal():
		token_list.append(operand)
	return token_list

expr = input()
value = get_token_list(expr)
print(value)