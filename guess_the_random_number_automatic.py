import random
import matplotlib.pyplot as plt
class Random():
    def __init__(self,starting_number,numbers_guessed):
        self.rand_num1=random.randrange(1,starting_number+1)
        self.rand_num2=[]
        if numbers_guessed<=starting_number:
            for i in range(numbers_guessed):
                self.check=random.randrange(1,starting_number+1)
                while self.check in self.rand_num2:
                    self.check=random.randrange(1,starting_number+1)
                self.rand_num2.append(self.check)
    def compare_numbers(self):
        for i in self.rand_num2:
            if self.rand_num1==i:
                return True
        return False            
def lottery(x,numbers_guessed):
    for i in range(x):
        r=Random(x-i,numbers_guessed)
        if r.rand_num2==[]:
            print('invalid input')
            break
        if r.compare_numbers():
            return x-i
            break
def repeat_lottery(starting_num,numbers_guessed,repeat):
    results=[]
    for i in range(repeat):
        results.append(lottery(starting_num,numbers_guessed))
    print(results)
    print(sum(results)/len(results))
