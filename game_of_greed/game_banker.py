# from game_of_greed.game_logic import ameLogic
class Banker:
    '''

    Banker class that has 4 methods:

    __init__: which instiate when class is called which takes in 2 optional arguments balance and balance.
    shelf: which takes 1 argument an integer and calculate the total and returns an integer
    bank: which takes no arguments and stores the total balance
    clear_shelf: which takes no arguments and clears the shelf and assign it to 0


    '''

    def __init__(self , balance = 0 , shelved = 0  ):
        # give the balance and shelved a defulte value
        self.balance = balance 
        self.shelved = shelved

    def shelf(self,score):
        # shelved as a counter for the score
        self.shelved += score
        return self.shelved

    def bank(self):
        # balance in bank is commulated from shelf
        self.balance+=self.shelved
        self.shelved=0
        return self.shelved, self.balance

        # when zelsh mush be return to zero
    def clear_shelf(self):
        self.shelved=0

