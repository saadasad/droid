
def menu():
	from ftplib import FTP
	import os
	import time
	from pygame import mixer
	import sched


	ftp = FTP()
	choice = ''
	while(choice!='0'):
		print('1. Music')
		print('2. Take a Picture')
		print('3. Text To Speech')
		print('0. To Exit')
		choice = input('Enter Choice : ')
		if(choice == '1'):
			print('All Music Files')
			ftp.connect('192.168.43.1', 2121)

			ftp.login(user='user', passwd='password')

			ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/Music/')

			data= []

			files = ftp.nlst()
			counter=1
			
			for f in files:
				print(counter,':',end='')
				print(f)
				counter = counter + 1
			ftp.close()
			choice = input('Enter Music File Number :')
			index = int(choice)-1
			print(index)
			file = open('action.txt', 'w')
			file.writelines('getMusic' + '\n')
			musicNumber = files[index]
			path = 'D:\Computer Science\Semester 4\Data Structures & Algorithms\Mobile Simulator Project\\' + musicNumber
			print(path)
			file.writelines(musicNumber + '\n') 
			file.close()
			ftp.connect('192.168.43.1', 2121)
			ftp.login(user='user', passwd='password')
			ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
			ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
			path = musicNumber
			print(path)			
			time.sleep(15)
			mixer.init()
			choice = ''
			while(choice!=0):
				choice = input('1. To Play and 2. To Pause and 0. To Exit: ')
				if(choice=='1'):
					mixer.music.load(musicNumber)
					mixer.music.play()
				elif(choice=='2'):
					mixer.music.pause()
					
				elif(choice == '0'):
					break
			ftp.close()

			


		elif( choice == '2'):
			print('Picture Taken!')
		elif( choice == '3'):
			speak=input('Enter Your Message : ')
			file = open('action.txt', 'w')
			file.writelines('speak' + '\n')
			file.writelines(speak + '\n') 
			file.close()
			ftp.connect('192.168.43.1', 2121)
			ftp.login(user='user', passwd='password')
			ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
			ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
			ftp.close()
			break
	print('1. Messages        2. Contacts')
	print('3. Phone           4. Media')
	print('0. Back ')