import random, threading

class Tortoise(threading.Thread):
    
    def __init__(self, total_step: int) -> None:
        super().__init__()
        self.__total_step = total_step
    
    def run(self):
        steps = 0
        while(steps < self.__total_step):
            steps += 1
            print(f"Tortoise total steps: {steps}")

class Hare(threading.Thread):

    def __init__(self, total_step: int) -> None:
        super().__init__()
        self.__total_step = total_step

    def run(self):
        steps = 0
        while(steps < self.__total_step):
            sleep = int(10 * random.random())%2 == 0
            if sleep:
                print("Hare is sleeping")
            else:
                steps += 2 
                print(f"Hare total steps: {steps}")

Tortoise(20).start()
Hare(20).start()
