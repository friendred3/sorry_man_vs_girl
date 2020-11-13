from time import sleep
import os 
import sys
while('True'):
	print('Premi Y per continuare o N per uscire.')
	r = input('==> ')

	if r == 'y' or r == 'Y':
		break
	elif r == 'n' or r == 'N':
		print('(^_^)')
		sys.exit()
	else:
		print('ERROR')
		continue


def maschio():
	m = '''
         RAGAZZO
            _
        ___(_)___
       / _    _  \  
      |_||     ||_|
         |  _  |
         | | | |
         | | | |
         |_| |_|
	'''
	M = '''
         RAGAZZO  _
            _    | |
        ___(_)__/ /
       / _    _ _/  
      |_||     |
         |  _  |
         | | | |
         | | | |
         |_| |_|
	'''
	x = 0
	while(True):
		print(m)
		sleep(0.4)
		os.system('clear')
		print(M)
		if x == 4:
			break
		sleep(0.4)
		os.system('clear')
		x += 1
	
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t  SCUSA')
	sleep(0.6)

def femmina():
	f = '''
         RAGAZZA
           ^_^
        ___(_)___
       / _    _  \  
      |_||     ||_|
         /     \ 
        /       \ 
       /_________\ 
         |_| |_|
	'''
	F = '''
         RAGAZZA  _
           ^_^   | |
        ___(_)__/ /
       / _    _ _/  
      |_||     |
         /     \ 
        /       \ 
       /_________\ 
         |_| |_|
	'''
	x = 0
	while(True):
		print(f)
		sleep(0.4)
		os.system('clear')
		print(F)
		if x == 4:
			break
		sleep(0.4)
		os.system('clear')
		x += 1
	print('\t    |')
	sleep(0.6)
	print('\t    |')
	sleep(0.6)
	print('\t    |____')
	sleep(0.6)
	print('\t         |____')
	sleep(0.6)
	print('\t              |')
	sleep(0.6)
	print('\t              |')
	sleep(0.6)
	print('\t           ___|')
	sleep(0.6)
	print('\t           |')
	sleep(0.6)
	print('\t           |____________\n\t               SCUSA    |')
	sleep(0.6)
	print('\t                        |')
	sleep(0.6)
	print('\t                        HO RAGIONE IO!')
	sleep(0.6)

maschio()
femmina()
