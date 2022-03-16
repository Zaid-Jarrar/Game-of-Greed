from game_of_greed.game_banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            bank = Banker()
            result = 0
            while round:
                score = 0
                shelved = bank.shelf(score)
                # print(shelved)
                # shelf = 0
                print(f"Starting round {round}")
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))
                # print(*rolled_dice, sep=',')
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision == "q":
                    print('this is decision')
                    result= balanced[1]
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
                    shelved = bank.shelf(score)
                    balanced = bank.bank()

                    # print(score)
                   
                    
                    rem_dice = 6 - len(selected_dice)
                    print(
                        f"You have {shelved} unbanked points and {rem_dice} dice remaining "
                    )
                    choice = input("(r)oll again, (b)ank your points or (q)uit: ")
                    
                    if choice == "b":
                        print(f"You banked {shelved} points in round {round}")
                        round += 1
                        print('this is balanced[1] ',balanced[1])

                    
                    # print('roll again, (b)ank your points or (q)uit b')
                    # print(f"You banked {shelved} points in round {(round -1)}")
                    
                    # if choice == "q":
                    #     result= balanced[1]
                    #     print('this is result',result)
                    #     break
            print(f"Total score is {result} points")
            print(f"Thanks for playing. You earned {result} points")
                
                # print(f"Thanks for playing. You earned {result} points")
                
                    

           


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
