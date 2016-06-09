from time import gmtime, strftime


class Messages:
    recipient = ''
    contents = ''
    state = ''
    sent = []
    drafts = []
    to = []
    time = []

    def __init__(self):
        self.recipient = ''
        self.contents = ''
        self.state = ''
        self.sent = []
        self.to = []

    def compose(self, recipient, contents, state):
        self.recipient = recipient
        self.contents = contents
        if(state == 'send'):
            self.sent.append(contents)
            self.to.append(recipient)
            self.time.append(strftime("%a %d %b %Y %H:%M:%S ", gmtime()))
            print('Message Sent!')
        elif(state == 'save'):
            self.drafts.append(contents)
            self.to.append(recipient)
            print('Message Saved In Drafts!')
        elif(state == 'delete'):
            print('Message Deleted')
        else:
            print('Choose Correct Option')

    def printSent(self):
        for x, y, z in zip(self.to[::-1], self.sent[::-1], self.time[::-1]):
            print('To:', x)
            print(y)
            print(z)

    def printDrafts(self):
        for x, y, z in zip(self.to[::-1], self.drafts[::-1], self.time[::-1]):
            print('To:', x)
            print(y)
            print(z)


test = Messages()
choice = ''
to = ''
contents = ''
while(choice != 0):
    print('1. To Compose Message.')
    print('2. Inbox.')
    print('3. Sent Messages.')
    print('4. Drafts.')
    choice = input('Enter choice: ')
    if(choice == '1'):
        to = input('Enter Recipient Name or Number: ')
        contents = input('Enter your message: ')
        choice = input(
            ' "Send" To Send, "Save" To Save in Drafts, "Delete" To Delete: ')
        test.compose(to, contents, choice)
    if(choice == '3'):
        test.printSent()
    if(choice == '4'):
        test.printDrafts()
    if(choice == '0'):
        break
