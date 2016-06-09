import android
import getInboxRead
import getInboxUnread
from ftplib import FTP
ftp = FTP()
droid = android.Android()




def Runner():
	file = open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'r')
	list = file.readlines()
	list = [l.replace('\n', '') for l in list]
	if(list):
		action=list[0]
		if(action == 'smsSend'):	
			recipient = list[1]
			content   = list[2]
			print(list)
			droid.smsSend(recipient, content)
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()

		elif(action == 'getInboxRead'):
			print('read')
			getInboxRead.run()
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()
		
		elif(action == 'getInboxUnread'):
			print('unread')
			getInboxUnread.run()
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()

		elif(action == 'dialNumber'):
			number = list[1]
			droid.phoneCallNumber(number)
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()
		elif(action == 'speak'):
			message = str(list[1])
			print(message)
			droid.ttsSpeak(message)
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()
		elif(action == 'getMusic'):
			musicName = str(list[1])
			print(musicName)
			ftp.connect('192.168.43.98', 21)
			ftp.login(user='user', passwd='password')
			ftp.cwd('/Mobile Simulator Project')
			path = '/storage/emulated/0/com.hipipal.qpyplus/project/Music/' + musicName
			print(path)
			ftp.storbinary('STOR '+musicName, open(path, 'rb+'))
			ftp.close()
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()

		else:
			open('/storage/emulated/0/com.hipipal.qpyplus/project/action.txt', 'w').close()




import sched, time
s = sched.scheduler(time.time, time.sleep)



def do_something(sc): 
    Runner()
    sc.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()



