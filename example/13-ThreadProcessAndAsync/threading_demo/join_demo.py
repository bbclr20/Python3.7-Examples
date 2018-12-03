import threading

def demo(num, name:str):
    print(f"Start a new thread {name}")
    for _ in range(num):
        print(f"Executing thread {name}")
    print(f"Thread {name} is waiting to be terminated")


print("Main thread is running")

th_A = threading.Thread(target=demo, args=(10, "A",))
th_A.start()
th_A.join()

th_B = threading.Thread(target=demo, args=(10, "B",))
th_B.start()
th_B.join()

print("Main thread is waiting to be terminated")
