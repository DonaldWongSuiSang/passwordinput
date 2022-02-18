pw = 'a123456'
input_pw = 2
while True:
	user_pw = input('請輸入密碼： ')
	if input_pw > 0:
		if user_pw == pw:
			print('登入成功!')
			break
		else:
			print('密碼錯誤! 還有', input_pw, '次機會')
			input_pw = input_pw - 1			
	elif input_pw == 0:
		if user_pw == pw:
			print('登入成功!')
			break
		else:
			print('密碼錯誤次數過多!')
			break