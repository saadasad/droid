def run():
	import android
	from ftplib import FTP
	import os


	droid = android.Android()

	SMSmsgs = droid.smsGetMessages(True, 'inbox').result 

	recipient = []

	content = []

	for message in SMSmsgs:

	    recipient.append(message['address'])

	    content.append(message['body'])

	    #print('From: '+message['address']+' > '+message['body']+'\n')



	unread = {}

	index = -1
	for x in recipient:
		index = index + 1
		if(len(x)==11):
			orignal = x
			edited = orignal[1::]
			number = '+92' + edited
			recipient[index] = number



	for x,y in zip(recipient,content):
		
		if(x in unread.keys()):

			unread[x].append(

				y

				)
		
		else:
			
			unread[x] = [
				
				y
			
			]



	for k,v in unread.items():
		#print(k,':-')
		mylen=len(unread[k])
		counter = 1
		for d in unread[k]:
			#print(counter,':')
			#print(d)
			#print('')
			counter = counter + 1
				

	file = open('/storage/emulated/0/com.hipipal.qpyplus/project/unread.txt', 'w')
	file.close()
	

	for k,v in unread.items():
		file = open('/storage/emulated/0/com.hipipal.qpyplus/project/unread.txt', 'a')
		temp = k + ':-' + '\r\n'
		file.write(temp)
		counter = 1
		for d in unread[k]:
			d.replace('\n','\r\n')
			temp =str(counter) + ': ' + d +'\r\n' + '\r\n'
			file.write(temp)
			counter = counter + 1







	ftp = FTP()

	ftp.connect('192.168.43.98', 21)

	ftp.login(user='user', passwd='password')

	ftp.cwd('/Mobile Simulator Project')

	#file = open('/storage/emulated/0/com.hipipal.qpyplus/project/unread.txt', 'rb')

	#ftp.storlines('STOR' + 'unread.txt', file)


	ftp.storbinary('STOR unread.txt', open('/storage/emulated/0/com.hipipal.qpyplus/project/unread.txt', 'rb'))



