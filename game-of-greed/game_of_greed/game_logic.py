import random
from collections import Counter

class GameLogic:
    def __init__(self):
        pass

    '''
    
    doc string 

    '''
    @staticmethod
    def roll_dice(number):
        rolls = tuple([random.randint(1, 6) for _ in range(number)]) 
        # ctr = Counter(rolls)  
        return  rolls
      
    @staticmethod
    def calculate_score(rolls):
        total_score = 0
        ctr = Counter(rolls).most_common()
        print(ctr)
        common = ctr[0][1]
        if common == 1:
            total_score += 1600




        
        return common
        

            

        

        



if __name__ == '__main__':
    values = GameLogic()
    rolls = values.roll_dice(6)
    print(values.calculate_score(rolls))
    

   
