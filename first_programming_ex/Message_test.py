def Message_demo():
    from Message import Message
    import argparse
    import textwrap
    description="""
    The Message class is created to write messages including the name of the sender, recipient. You can append lines to the existing content and convert the whole message to 1 string. The user can access the class variables: the number of messages and the log dictionary.

    Method1 - append: appends a new line to the existing content instance variable. Also invokes log_message method which modifies the value of class variables.

    Method2 - toString: prints 1 string - sender, recipient, content concatenated

    Method3 - log_messages: modifies class variables. Adds +1 to the number of messages and adds values to the log dictionary.

    Method4 - getNoMessages: prints the number of messages

    Method5 - getLogfile: prints the log dictionary

    """
    parser=argparse.ArgumentParser(description=textwrap.dedent(description))

    parser.parse_args()

    email1=Message('me', 'you')
    email1.append()
    email1.append()
    email1.toString()
    print("Expected:\n From: me \n To: you\n\nexample\nexample")
    email1.getNoMessages()
    print("Expected: 2")
    email1.getLogfile()
    print("Expected: {'me': {'you': '\nexampleexample'}}\n\n\n")

    email2=Message()
    email2.append("new line")
    email2.append("new line")
    email2.toString()
    print("Expected:\nFrom: someone\nTo: someone else\n\nnew line\nnew line ")
    email2.getNoMessages()
    print("Expected: 4")
    email2.getLogfile()
    print("Expected: {'me': {'you': '\nexample\nexample'}, 'someone': {'someone else': '\nnew line\nnew line'}}")

Message_demo()