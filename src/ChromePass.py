import sqlite3, win32crypt, os, sys

def decrypt(path, save_path):
	if not os.path.isfile(path):
		print 'The file doesn\'t exist!'
		return
	
	connChrome = sqlite3.connect(path)
	cursor = connChrome.cursor()
	try:
		cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	except:
		print 'Impossible to read ' + path
		return

	print '\t\t\t*** Passwords ***'
	
	for query in cursor.fetchall():
		passwd = win32crypt.CryptUnprotectData(query[2], None, None, None, 0)[1]
		if passwd:
			print 'URL: ' + query[0]
			print 'User: ' + query[1]
			print 'Password: ' + passwd
			print '--------------------'
	
			if save_path != '':
				passwordsFile = open(save_path, 'a')
				passwordsFile.writelines('URL: ' + query[0] + '\nUser: ' + query[1] + '\nPassword: ' + passwd + '\n--------------------\n')
				passwordsFile.close()

def show_help():
    print '''  Usage:
    python ChromePass.py                                   # Run with the default location of the Login Data file.
    python ChromePass.py "path_to_file"                    # Run with a path to the Login Data file.
    python ChromePass.py "path_to_file" -S "path_to_save"  # Run with a path to the Login Data file and save.
    python ChromePass.py -S "path_to_save"                 # Save the content of the default Login Data file.

  >> Developed by Cristian Henrique (cristianmsbr@gmail.com)
  >> github.com/cristian-henrique'''

if __name__ == '__main__':
    arg = sys.argv
    args = len(arg)
    login_data = os.getenv('LOCALAPPDATA') + '\Google\Chrome\User Data\Default\Login Data'

    if args == 1:
        decrypt(login_data, '')
    elif args == 2:
        decrypt(arg[1], '')
    elif args == 3:
        if arg[1].upper() == '-S':
            decrypt(login_data, arg[2])
        else:
            show_help()
    elif args == 4:
        if arg[2].upper() == '-S':
            decrypt(arg[1], arg[3])
        else:
            show_help()
    else:
        show_help()
