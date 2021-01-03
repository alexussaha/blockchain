import random

class Game:
    def __init__(self, number):
        self.gamers_account = [10] * number
    
    def start_game(self, rounds=1):
        active = len(self.gamers_account)
        zeros = 0
        while rounds!=0:
            winner = random.randint(0, active-1)
            print(winner)
            for i in range(len(self.gamers_account)):
                if self.gamers_account[winner] == 0:
                    rounds = rounds + 1
                    break
                if self.gamers_account[i] != 0:
                    if i == winner:
                        self.gamers_account[winner] = self.gamers_account[winner] +  active - 1
                    else:
                        self.gamers_account[i] = self.gamers_account[i] - 1
            rounds = rounds - 1
            print(self.gamers_account)
            
            count = 0
            for i in self.gamers_account:
                if i == 0:
                    count = count + 1
            
            if count > zeros:
                active = active - 1
                zeros = count