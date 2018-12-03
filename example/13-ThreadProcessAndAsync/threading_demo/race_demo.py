import threading

state = ""

def dead():
    global state
    while True:
        state = "dead"
        if state != "dead":
            raise ValueError(f"The cat is {state} not dead")

def alive():
    global state
    while True:
        state = "alive"
        if state != "alive":
            raise ValueError(f"The cat is {state} not alive")


# two functions acccess 
cat_is_dead = threading.Thread(target=dead)
cat_is_alive = threading.Thread(target=alive)

cat_is_dead.start()
cat_is_alive.start()
