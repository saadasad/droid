from time import gmtime, strftime
from ftplib import FTP
import os
import time
ftp = FTP()


class Message():
    recipient = ''
    message = ''
    state = ''
    time = ''

    def setRecipient(self, number):
        self.recipient = number

    def getRecipient():
        return recipient

    def setMessage(self, contents):
        self.message = contents

    def getMessage():
        return message

    def setState(self, status):
        self.state = status

    def getState(self):
        return self.state

    def setTime(self):
        self.time = (strftime("%a %d %b %Y %H:%M:%S ", gmtime()))

    def getTime():
        return time


class MessageObjects(Message):
    SentObjects = []
    DraftObjects = []

    def compose(self,):
        obj = Message()
        recipient = input('Enter Recipient Number: ')
        obj.setRecipient(recipient)
        message = input('Enter Message Contents: ')
        obj.setMessage(message)
        status = input('Enter "send" to send and "save" to save in drafts and "delete" to delete: ')
        obj.setState(status)
        obj.setTime()

        if(obj.getState() == 'send'):
            file = open('action.txt', 'w')
            file.writelines('smsSend' + '\n')
            file.writelines(obj.recipient + '\n')
            file.writelines(obj.message)
            file.close()
            ftp.connect('192.168.43.1', 2121)
            ftp.login(user='user', passwd='password')
            ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
            ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
            ftp.close()
            self.SentObjects.append(obj)
            print('Message Sent!')

        elif(obj.getState() == 'save'):
            self.DraftObjects.append(obj)

    def printInbox(self):
        print('1. For Read')
        #print('2. For Unread')
        choice = input('Enter Choice : ')
        if( choice == '1'):
            file = open('action.txt', 'w')
            file.writelines('getInboxRead' + '\n')
            file.close()
            ftp.connect('192.168.43.1', 2121)
            ftp.login(user='user', passwd='password')
            ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
            ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
            time.sleep(3)
            file = open('read.txt')
            ReadContent = file.readlines()
            file.close()
            #file = open('read.txt', 'w')
            #file.close()
            if(ReadContent==None):
                print('No Read Messages')
            for l in ReadContent:
                print(l,end='')
        elif( choice == '2'):
            file = open('action.txt', 'w')
            file.writelines('getInboxUnread' + '\n')
            file.close()
            ftp.connect('192.168.43.1', 2121)
            ftp.login(user='user', passwd='password')
            ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/') 
            ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
            time.sleep(2)
            file = open('unread.txt','r')
            UnreadContent = file.readlines()
            file.close()
            #file = open('unread.txt', 'w')
            #file.close()
            if(UnreadContent==None):
                print('No Unread Messages')
            for l in UnreadContent:
                print(l,end='')

        ftp.close()

    def printSentItems(self):
        if(len(self.SentObjects)==0):
            print('No Sent Messages')
        for x in self.SentObjects[::-1]:
            print('To :', x.recipient)
            print(' ', x.message)
            print(x.time)

    def printDraftItems(self):
        if(len(self.DraftObjects)==0):
            print('No Drafted Messages')
        for x in self.DraftObjects[::-1]:
            print('To :', x.recipient)
            print(' ', x.message)
            print(x.time)

obj = MessageObjects()
def menu():
    choice = ''
    while(choice != 0):
        print('1. To Compose Message.')
        print('2. Inbox.')
        print('3. Sent Messages.')
        print('4. Drafts.')
        print('b. Back')
        choice = input('Enter choice: ')
        if(choice == '1'):
            obj.compose()
        elif( choice == '2'):
            obj.printInbox()
        elif(choice == '3'):
            obj.printSentItems()
        elif(choice == '4'):
            obj.printDraftItems()
        elif(choice == '0'):
            break
    print('1. Messages        2. Contacts')
    print('3. Phone           4. Media')
    print('0. Back ')


