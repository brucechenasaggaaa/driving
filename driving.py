country = input('請問你是哪國人')
age = input('請輸入您的年齡')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不可考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不可考駕照')
else:
	print('您只能輸入 台灣/美國')	