from time import gmtime, strftime
from ftplib import FTP
import os
import Messages
ftp = FTP()




class Contact():
    Name = ''
    Number = ''

    
    
    def setName(self, name):
        self.Name = name
    def getName():
        return Name
    def setNumber(self, number):
        self.Number = number
    def getNumber():
        return Number
    

class ContactObjects(Contact):
    AllContacts = []
    total = 0
    
    def add(self,):
        obj = Contact()
        name=input('Enter Contact Name: ')
        obj.setName(name)
        number=input('Enter Contact Number: ')
        obj.setNumber(number)
        self.total= self.total + 1
        self.AllContacts.append(obj)
        print('Contact Added!')
        
    def search(self,):
        flag = 0
        counter = 1
        name = input('Enter The Contact Name :')
        for x in self.AllContacts:
            flag = x.Name.find(name) 
            if (flag)>-1:
                print(counter,':')
                print('Name   :', x.Name)
                print('Number :', x.Number)
                print()
                break
            counter = counter + 1
        selection = input('Enter Contact Selection Number : ')
        selection = int(selection)
        selection = selection - 1
        print('1. To Call Contact')
        print('2. To Message Contact')
        print('3. To Edit Contact')
        print('4. To Delete Contact')
        choice = input('Enter Choice : ')
        if( choice == '1'):
            number = self.AllContacts[int(selection)].Number
            file = open('action.txt', 'w')
            file.writelines('dialNumber' + '\n')
            file.writelines(number)
            file.close()
            ftp.connect('192.168.43.1', 2121)
            ftp.login(user='user', passwd='password')
            ftp.cwd('/storage/emulated/0/com.hipipal.qpyplus/project/')
            ftp.storbinary('STOR action.txt', open('action.txt', 'rb'))
        elif( choice == '2'):
            number = self.AllContacts[int(selection)].Number
            obj = Messages.Message()
            container = Messages.MessageObjects()
            obj.setRecipient(number)
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
            
                container.SentObjects.append(obj)
                print('Message Sent!')

            elif(obj.getState() == 'save'):
                self.DraftObjects.append(obj)
        elif( choice == '3'):
            pass
        elif( choice == '4'):
            pass
        else:
            print('Wrong Choice')
        if(flag=='0'):
            print('No Contact Found')
        '''
            if (i.find('za'))>-1:
        print('Found It : ',i)
        '''
        
    def printContacts(self):
        for x in self.AllContacts:
            print('Name   :', x.Name)
            print('Number :',x.Number)


def menu():
    obj = ContactObjects()
    choice = ''
    while(choice != 0):
        print('1. Add Contact')
        print('2. Show Contacts.')
        print('3. Search Contacts.')
        print('b. Back')
        choice = input('Enter choice: ')
        if(choice == '1'):
            obj.add()
        elif(choice == '2'):
            obj.printContacts()
        elif(choice == '3'):
            obj.search()
        elif(choice == '0'):
            break
    print('1. Messages        2. Contacts')
    print('3. Phone           4. Media')
    print('0. Back ')


