class Customer:
    #Customer class is a class that helps to decide whether a customer recieves a discount on her or his purchases.

    #construct amount_purchased and discount instance variables
    def __init__(self):
        self._amount_purchased=0
        self._discount=0

    #checks whether discount is reached after the purchase
    #if yes, prints the amount of the discount on the next purchase and resets amount_purchased to 0.
    #if no,  prints that more purchases required to receive discount

    def discountReached(self):
        if self._amount_purchased >= 100:
            self._discount=10
            print(f"You receive {self._discount}$ discount on the next purchase.")
            self._amount_purchased=0
        else:
            print("You still have to purchase more to receive discount.")

    #books the amount of purchase on the amount purchased instance variable
    #@param amount - the amount of the purchase
    def makePurchase(self, amount):
        self._amount_purchased=self._amount_purchased+amount
        self.discountReached()
    






