import textwrap

def Customer_demo():
    from Customer import Customer
    import argparse
    
    description=textwrap.dedent('''
    This is the test of the class Customer. The Customer class is created to decide whether a customer receives a discount on the purchases. If yes it prints the amount of discount
                                                               
    Method 1 - discountReached: Based on the total value purchased prints the amount of discount for a customer
                                                               
    Method 2 - makePurchase: increases the total value purchased by the value of amount input parameter.
                                
    ''')
    
    parser=argparse.ArgumentParser(description=description)
    parser.parse_args()


    Person=Customer()

    Person.makePurchase(95)
    print('Expected: You still have to purchase more to receive discount.')
    Person.makePurchase(10)
    print("Expected: You receive 10$ discount on the next purchase.")

Customer_demo()



