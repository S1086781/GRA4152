#The Message class has 2 class variables the number of messages and the log dictionary that contains the sender recipient and the text of the message.
#The Message class has 6 methods. 1 constructor 3 mutator and 2 accessor. See the detailed description below or in the test file of this class.

class Message:
    #Setting the number of messages to 0 and creating an empty log dictionary
    _no_messages=0
    _log={}

    #The constructor method creates 3 instance variables. The sender, recipient and the content
    #@params sender - sender of the message, recipient - recipient of the message
    def __init__(self, sender='someone', recipient='someone else'):
        self._sender=sender
        self._recipient=recipient
        self._content=str()

    #This mutator method appends a new line to the existing content instance variable. Also invokes log_message method which modifies the value of the class variables
    #@params line - the string that you want to append as new line
    def append(self, line="example"):
        self._content=self._content+'\n'+line
        self.log_messages()

    #This mutator prints 1 string - sender, recipient, content concatenated
    def toString(self):
        self._outputstring=f"From: {self._sender} \nTo: {self._recipient} \n {self._content}"
        print(self._outputstring)

    #This mutator method modifies class variables. Adds +1 to the number of messages and adds sender, recipient, content info to the log dictionary.
    def log_messages(self):
        Message._no_messages+=1
        sender=self._sender
        recipient=self._recipient
        content=self._content
        Message._log[sender] = {recipient: content}

    #This accessor method prints the number of messages
    def getNoMessages(self):
        print(Message._no_messages)

    #This accessor method prints the log dictionary
    def getLogfile(self):
        print(Message._log)
