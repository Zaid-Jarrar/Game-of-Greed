from game_of_greed.game_banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:


    def __init__(self, roller=None):
        self.roller = roller
        self.banker = Banker()
        self.logic = GameLogic()
        self.banker.bank



    def play(self):
        print("Welcome to Game of Greed")
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
                # score = 0
                # shelved = banked.shelf(score)
                # print(shelved)
                # shelf = 0

                if choice != 'r':
                    
                    print(f"Starting round {round}")

                print(f"Rolling {rem_dice} dice...")
        
                rolled_dice = self.roller(rem_dice)
#make test incase he inputs strings instead of numbers
                # if round == 1: 
                #     rolled_dice = (2,6,4,3,3,6)

                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))
               

                possible_score = logic.calculate_score(rolled_dice)# rolled_dice
                
                #Zilch
                if possible_score == 0:
                    print('Zilch!!! Round over')
                    print(f'You banked 0 points in round {round}')
                    print(f'Total score is {banked.balance} points')
                    round += 1
                    # print(nums)
                    
                    # print(f"Starting round {round}")    
                    rem_dice = 6
                    break
                # if possible_score == 0:
                #     print('Zilch!!! Round over')
                #     print(f'You banked 0 points in round {round}')
                #     print(f'Total score is {banked.balance} points')
                #     round += 1
                #     print(f"Starting round {round}")

                #     print(f"Rolling {rem_dice} dice...")# dynamic dice counter step 1
                #     rolled_dice = self.roller(rem_dice)# dynamic dice counter step 2
                #     # rolled_dice = (2,6,4,3,3,6)
                #     nums = []
                #     for i in rolled_dice:
                #         nums.append(str(i))
                #     print(",".join(nums))              
                    
                    
                #I DONT KNOW HOW IT WORKED 


               
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")


                #BANKING HERE -----------
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
                else:
                    new_list = []
                    selected_dice = tuple(decision)
                    for elem in selected_dice:
                        # if elem in rolled_dice:
                        
                        new_list.append(int(elem))
                        # else:
                        #     print('cheater')
                        #     #-------------------------------------------------------HERE
                        #     break

                    
                        
                    # print(new_list)
                    new_tuple = tuple(new_list)
                    # for single_dice in new_tuple:
                    #     if single_dice not in rolled_dice:
                    #         print('cheater')
                    #         break
                    # print(new_tuple)
                   
                    score = GameLogic.calculate_score(new_tuple)
                    shelved = banked.shelf(score)

                    # print(score)
                   
                    # remaining dice counter
                    rem_dice = rem_dice - len(selected_dice)

                        
                    print(
    
                        f"You have {shelved} unbanked points and {rem_dice} dice remaining"
                    )
                    if rem_dice == 0:
                        rem_dice = 6
                    choice = input("(r)oll again, (b)ank your points or (q)uit ")

                    # choice = input("(r)oll again, (b)ank your points or (q)uit: ")

                    if choice == "b":                        
                        print(f"You banked {shelved} points in round {round}")
                        print(f"Total score is {banked.bank()[1]} points")
                        round += 1
                        rem_dice = 6

                    elif choice == 'r':
                        if rem_dice == 0:
                            rem_dice = 6
                        continue
                

                
                    

           


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
