pw = 'a123456'
input_pw = 3
while input_pw>0:
	input_pw = input_pw - 1
	user_pw = input('請輸入密碼： ')
	if user_pw == pw:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if (input_pw>0):
			print('還有', input_pw, '次機會')
		else:
			print('密碼錯誤次數過多!')
			break