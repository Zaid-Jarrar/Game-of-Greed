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
            round = 1
            result = 0
            while round:
                score = 0
                shelved = banked.shelf(score)
                # print(shelved)
                # shelf = 0

                print(f"Starting round {round}")
                print("Rolling 6 dice...")

                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))

               
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")

                result = banked.balance
                # Thanks for playing depends on this to calculate the result 70 passes

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
                        new_list.append(int(elem))
                    # print(new_list)
                    new_tuple = tuple(new_list)
                    # print(new_tuple)

                    score = GameLogic.calculate_score(new_tuple)
                    shelved = banked.shelf(score)

                    # print(score)
                   
                    
                    rem_dice = 6 - len(selected_dice)
                    print(
                       
                        f"You have {shelved} unbanked points and {rem_dice} dice remaining"
                    )
                    
                    choice = input("(r)oll again, (b)ank your points or (q)uit ")

                    # choice = input("(r)oll again, (b)ank your points or (q)uit: ")

                    if choice == "b":
                        if round == 1:
                            print(f"You banked {shelved} points in round {round}")
                            print(f"Total score is {banked.bank()[1]} points")
                            round += 1
                        else:
                            print(f"You banked {shelved} points in round {round}")
                            print(f"Total score is {banked.bank()[1]} points")
                            # banked calculate the total score 
                            
                            round += 1
                
            # print(f"Total score is {result} points")

            # print(f"Thanks for playing. You earned {result} points")
                
                # print(f"Thanks for playing. You earned {result} points")
                
                    

           


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
