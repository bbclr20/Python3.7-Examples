import random, threading

def tortoise(total_step: int):
    steps = 0
    while steps < total_step:
        steps += 1
        print(f"Tortoise total steps: {steps}")

def hare(total_step: int):
    steps = 0

    while steps < total_step:
        sleep = int(10*random.random()) % 2 == 0
        if sleep:
            print("Hare is sleeping")
        else:
            steps += 2
            print(f"Hare total steps: {steps}")


t = threading.Thread(target=tortoise, args=(10,))
h = threading.Thread(target=hare, args=(10,))

t.start()
h.start()
