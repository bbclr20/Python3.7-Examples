from threading import Thread, Lock

state = ""

def dead(lock: Lock):
    with lock:
        global state
        while True:
            state = "dead"
            if state != "dead":
                raise ValueError(f"The cat is {state} not dead")

def alive(lock: Lock):
    with lock:
        global state
        while True:
            state = "alive"
            if state != "alive":
                raise ValueError(f"The cat is {state} not alive")


# two functions acccess 
lock = Lock()
cat_is_dead = Thread(target=dead, args=(lock,))
cat_is_alive = Thread(target=alive, args=(lock,))

cat_is_dead.start()
cat_is_alive.start()
