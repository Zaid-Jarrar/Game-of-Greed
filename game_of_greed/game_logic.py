import random
from collections import Counter
class GameLogic:
    def __init__(self):
        pass

    '''
    
    GameLogic class that has two methods:

    roll_dice: which takes in an integer as argument and returns a tuple of random numbers from 1 to 6
    calculate_score: which takes in a tuple of integers as an argument and returns the total_score.

    '''
    @staticmethod
    def roll_dice(number):
        rolls = tuple([random.randint(1, 6) for _ in range(number)]) 
    #     print(rolls)  
        return  rolls
      
    @staticmethod
    def validate_input(rolled_dice,chosen_dice):
        ctr_rolled_dice=Counter(rolled_dice)
        ctr_chosen_dice=Counter(chosen_dice)
        
        for i in ctr_chosen_dice and ctr_rolled_dice:
            if ctr_chosen_dice[i]>ctr_rolled_dice[i]:
                return True

        for i in chosen_dice:
            for j in rolled_dice:
                if i not in rolled_dice:
                    return True

            
    @staticmethod
    def calculate_score(rolls):

        ctr = Counter(rolls)
        # print(f'occurances of Five : {ctr[5]}')
        # print(f'occurances of One : {ctr[1]}')
        # print(ctr)
        total_score = 0
        # print(ctr.keys())
        pairs=0
        for i in ctr:

            if len(ctr) == 6:
                total_score= 1500
                return total_score

            else:

                if ctr[i] == 3 and i != 1 and i != 5:
                    total_score+= i * 100
                    
                if ctr[i] > 3 and i != 1 and i != 5:
                    total_score+= (i*100) * (ctr[i] - 2)
                   
                if ctr[i] == 2:
                   pairs+=1

                if i == 5 and ctr[i] < 3:
                    total_score+= ctr[i] * 50

                if i == 5 and ctr[i] >= 3:
                    total_score+= (ctr[i]-2) * 500

                if i == 1 and ctr[i] < 3:
                    total_score+= ctr[i] * 100

                if i == 1 and ctr[i] >= 3:
                    total_score+= (ctr[i]-2) * 1000 
            if pairs==3:
                total_score=1500
        # print (f'Totalscore: {total_score}')    



        return total_score   


if __name__ == '__main__':
    values = GameLogic()
    rolls = values.roll_dice(6)
    values.calculate_score(rolls)
    

   
        




     
        # return common


                # ctr = Counter(rolls)
        # print(ctr)
        # total_score=0
        # triples=0
        # for i in ctr:
        #     if ctr[i] == 3:
        #         triples += 1
        #         total_score+=i*100

        #     elif ctr[i] < 3 and i == 5:
        #         total_score += (ctr[i] * 50)

        #     elif ctr[i] >= 3 and i == 5:
        #         total_score += 500
        #         ctr[i] -= 3
        #         for i in range(ctr[i]):
        #             total_score += 500


        #     elif ctr[i] < 3 and i == 1:
        #         total_score += (ctr[i] * 100)

        #     elif ctr[i] >= 3 and i == 1:
        #         total_score += 1000
        #         ctr[i] -= 3
        #         for i in range(ctr[i]):
        #             total_score += 1000

        # "Ones Counter"
        # while 1 in ctr.keys():
    
        #     if ctr[1]<=2:
        #         i = 1
        #         for i in range(ctr[1]):
        #             total_score+=100
        #         i +=1            
                
        #     # elif ctr[1]==3:
        #     #     total_score=1000
                
        #     elif ctr[1]>=3:
        #         i = 2
        #         for i in range(ctr[1]-i): 
                    
        #             total_score+=1000
        #             i +=1
        #     break
        # print (f'Total_score of Ones: {total_score}')
            
            
        

 
        
        # "Five Counter"
        # while 5 in ctr.keys():
        #     if ctr[5]<=2:
        #         i = 1
        #         for i in range(ctr[5]):
        #             total_score+=50
        #             i +=1
                
        #     # elif ctr[5]==3:
        #     #     total_score=500
                
        #     elif ctr[5]>=3:
        #         i = 2
        #         for i in range(ctr[1]-i):
        #             total_score+=500
        #             i +=1
        #     break

        # while 2 in ctr.keys():
         

                
        #     if ctr[2]>=3:
        #         i = 2
        #         for i in range(ctr[2]-i):
        #             total_score+=200
        #             i +=1
        #     break

        # while 3 in ctr.keys():
                
        #     if ctr[3]>=3:
        #         i = 2
        #         for i in range(ctr[3]-i):
        #             total_score+=300
        #             i +=1
        #     break