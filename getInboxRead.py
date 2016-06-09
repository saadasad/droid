def run():
	import android
	from ftplib import FTP
	import os


	droid = android.Android()

	SMSmsgs = droid.smsGetMessages(False, 'inbox').result 

	recipient = []

	content = []

	date = []

	for message in SMSmsgs:

	    recipient.append(message['address'])

	    content.append(message['body'])

	    date.append(message['date'])

	    #print('From: '+message['address']+' > '+message['body']+'\n')


	#[z for (y,x,z) in sorted(zip(recipient,content,date), key=lambda pair: pair[0])]
	read = {}

	index = -1
	for x in recipient:
		index = index + 1
		if(len(x)==11):
			orignal = x
			edited = orignal[1::]
			number = '+92' + edited
			recipient[index] = number



	for x,y in zip(recipient,content):
		
		if(x in read.keys()):

			read[x].append(

				y

				)
		
		else:
			
			read[x] = [
				
				y
			
			]



	for k,v in read.items():
		#print(k,':-')
		mylen=len(read[k])
		counter = 1
		for d in read[k]:
			#print(counter,':')
			#print(d)
			#print('')
			counter = counter + 1
				

	file = open('/storage/emulated/0/com.hipipal.qpyplus/project/read.txt', 'w')
	file.close()
	

	for k,v in read.items():
		file = open('/storage/emulated/0/com.hipipal.qpyplus/project/read.txt', 'a')
		temp = k + ':-' + '\r\n'
		file.write(temp)
		counter = 1
		for d in read[k]:
			d.replace('\n','\r\n')
			temp =str(counter) + ': ' + d +'\r\n' + '\r\n'
			file.write(temp)
			counter = counter + 1







	ftp = FTP()

	ftp.connect('192.168.43.98', 21)

	ftp.login(user='user', passwd='password')

	ftp.cwd('/Mobile Simulator Project')

	#file = open('read.txt', 'rb')

	#ftp.storlines('STOR' + 'read.txt', file)


	ftp.storbinary('STOR read.txt', open('/storage/emulated/0/com.hipipal.qpyplus/project/read.txt', 'rb'))

	ftp.close()


	