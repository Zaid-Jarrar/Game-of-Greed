# from game_of_greed.game_logic import ameLogic
class Banker:
    def __init__(self , balance = 0 , shelved = 0  ):
        # give the balance and shelved a defulte value
        self.balance = balance 
        self.shelved = shelved

    def shelf(self,score):
        # shelved as a counter for the score
        self.shelved += score
        return 

    def bank(self):
        # balance in bank is commulated from shelf
        self.balance+=self.shelved
        self.shelved=0
        return 

        # when zelsh mush be return to zero
    def clear_shelf(self):
        self.shelved=0
