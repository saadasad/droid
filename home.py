import Messages
import Contacts
import Phone
import Media






def menu():
	print('1. Messages        2. Contacts')
	print('3. Phone           4. Media')
	print('b. Back            0. Exit')
	choice = ''
	while(choice!=0):
		choice = input('Enter Choice : ')

		if( choice == '1' ):
			Messages.menu()
		elif( choice == '2'):
			Contacts.menu()
		elif( choice == '3'):
			Phone.menu()
		elif( choice == '4'):
			Media.menu()


menu()



