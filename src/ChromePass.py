import sqlite3, win32crypt, os.path

def decrypt():
	file = raw_input('Database: ')
	if not os.path.isfile(file):
		print 'The file doesn\'t exists!'
		return
	
	connChrome = sqlite3.connect(file)
	cursor = connChrome.cursor()
	try:
		cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	except:
		print 'Impossible to read ' + file
		return

	save = raw_input('Do you wanna save the passwords in ' + file + '.txt? <S/n> ')
	print '\t\t\t*** Passwords ***'
	
	for query in cursor.fetchall():
		passwd = win32crypt.CryptUnprotectData(query[2], None, None, None, 0)[1]
		if passwd:
			print 'URL: ' + query[0]
			print 'User: ' + query[1]
			print 'Password: ' + passwd
			print '--------------------'
	
			if save.upper() == 'S':
				passwordsFile = open(file + '.txt', 'a')
				passwordsFile.writelines('URL: ' + query[0] + '\nUser: ' + query[1] + '\nPassword: ' + passwd + '\n--------------------\n')
				passwordsFile.close()

if __name__ == '__main__':
	decrypt()