
from game_of_greed.game_banker import Banker
from game_of_greed.game_logic import GameLogic

class Game:


    def __init__(self, roller=GameLogic.roll_dice):
        self.roller = roller
        self.banker = Banker()
        self.logic = GameLogic()
        self.banker.bank
        self.cheater=self.logic.validate_input


    def play(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            banked = self.banker
            logic = self.logic
            round = 1
            result = 0
            choice = 0
            rem_dice = 6
            while round:

                if round==20 or banked.balance>=10000:
                    break
                if choice != 'r' :

                    
                    print(f"Starting round {round}")

                print(f"Rolling {rem_dice} dice...")
        
                rolled_dice = self.roller(rem_dice)
                #make test incase he inputs strings instead of numbers

                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print("*** "+",".join(nums))
        

                possible_score = logic.calculate_score(rolled_dice)# rolled_dice
                
                #Zilch
                if possible_score == 0:
                    print('Zilch!!! Round over')
                    print(f'You banked 0 points in round {round}')
                    print(f'Total score is {banked.balance} points')
                    banked.clear_shelf()
                    round += 1
                    choice=0
                    rem_dice = 6
                    continue

                print("Enter dice to keep, or (q)uit:")
                
                decision = input("Enter dice to keep, or (q)uit:")
                

                #BANK HERE -----------
                result = banked.balance
                # Thanks for playing depends on this to calculate the result 70 passes
                if banked.balance == 0 and decision == 'q' and round != 1: 
                    print(f'Total score is {result} points')
                    print(f'Thanks for playing. You earned {result} points') 
                    break 
                if banked.balance == 0 and decision == 'q':
                    print(f"Thanks for playing. You earned 0 points")
                    break    

                if banked.balance != 0 and decision == 'q':
                        print(f'Total score is {result} points')
                        print(f'Thanks for playing. You earned {result} points') 
                        break 
                  
                new_list = []
                selected_dice = tuple(decision)
                for elem in selected_dice:
                    new_list.append(int(elem))
                   

                
                    
                new_tuple = tuple(new_list)
                
                self.cheater(rolled_dice,new_tuple)
                cheater= self.cheater(rolled_dice,new_tuple)
                
                if cheater:
                    print('Cheater!!! Or possibly made a typo...')
                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))
                    print("*** "+",".join(nums))
                    banked.clear_shelf()
                    print("Enter dice to keep, or (q)uit:")
                    decision = input("Enter dice to keep, or (q)uit:")
                    new_list = []
                    selected_dice = tuple(str(decision))
                    for elem in selected_dice:

                       
                        
                        new_list.append(int(elem))
                       


                    
                        
                    
                    new_tuple = tuple(new_list)

                    
                score = GameLogic.calculate_score(new_tuple)
                shelved = banked.shelf(score)

                # remaining dice counter
                rem_dice = rem_dice - len(selected_dice)

                print(f"You have {shelved} unbanked points and {rem_dice} dice remaining")
                if rem_dice == 0:
                    rem_dice = 6
                print("(r)oll again, (b)ank your points or (q)uit:")
                choice = input("(r)oll again, (b)ank your points or (q)uit:")

                if choice == "b":    
                    print(f'Thanks for playing. You earned {shelved} points')                    
                    print(f"You banked {shelved} points in round {round}")
                    print(f"Total score is {banked.bank()[1]} points")
                    round += 1
                    rem_dice = 6

                if choice=="q":
                    print(f'Total score is {result} points')
                    print(f'Thanks for playing. You earned {result} points')                  
                    break

                if choice == 'r':
                    if rem_dice == 0:
                        rem_dice = 6
                    continue

                

                
                    

           


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
