# from game_of_greed.game_logic import ameLogic
class Banker:
    def __init__(self ):
        self.balance = 0 
        self.shelved = 0

    def shelf(self,num):
        self.shelved+=num
        return self.shelved

    def bank(self):
        self.balance+=self.shelved
        self.shelved=0
        return self.balance

    def clear_shelf(self):
        self.shelved=0