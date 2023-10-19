import textwrap

def Customer_demo():
    from Customer import Customer
    import argparse
    
    description=textwrap.dedent('''
    This is the test of the class Customer. The Customer class is created to decide whether a customer receives a discount on the purchases. If yes it prints the amount of discount.
                                                               
    Method 1 - discountReached: Based on the total value purchased prints the amount of discount for a customer
                                                               
    Method 2 - makePurchase: increases the total value purchased by the value of amount input parameter.
                                
    ''')
    
    parser=argparse.ArgumentParser(description=description)
    parser.parse_args()


    Person=Customer()

    Person.makePurchase(105)
    print("Expected: You receive 10$ discount on the next purchase.\n\n")
    Person.makePurchase(90)
    print('Expected: You still have to purchase more to receive discount.\n\n')
    Person.makePurchase(30)
    print("Expected: You receive 10$ discount on the next purchase.\n\n")


Customer_demo()



