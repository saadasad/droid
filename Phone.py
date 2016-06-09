


def menu():
	import Contacts
	myContacts = Contacts.ContactObjects.AllContacts
	import os
	from ftplib import FTP
	ftp = FTP()
	choice = ''
	number = ''
	name   = ''
	while(choice!='0'):
		print('1. Dial A Number')
		print('2. Dial A Contact')
		print('0. To Exit')
		choice = input('Enter Choice : ')
		if(choice == '1'):
			number = input('Enter Number : ')
			file = open('action.txt', 'w')
			file.writelines('dialNumber' + '\n')
			file.writelines(number)
			file.close()
			ftp.connect('192.168.43.1', 2121)
			ftp.login(user='saad', passwd='1234')
			ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
			ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
		elif( choice == '2'):
			name = input('Enter Contact Name : ')
			for x in myContacts:
				if name in x.Name:
					number = x.Number
			if(number == ''):
				print('Wrong Contact Name')
			file = open('action.txt', 'w')
			file.writelines('dialNumber' + '\n')
			file.writelines(number)
			file.close()
			ftp.connect('192.168.43.1', 2121)
			ftp.login(user='saad', passwd='1234')
			ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
			ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
			
	print('1. Messages        2. Contacts')
	print('3. Phone           4. Media')
	print('0. Back ')
	