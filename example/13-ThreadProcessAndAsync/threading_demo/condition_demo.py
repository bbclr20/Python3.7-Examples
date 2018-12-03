from threading import Thread, Condition
import random

class Clerk:

    def __init__(self):
        self.product = -1
        self.cond = Condition()
    
    def perchase(self, product: int):
        with self.cond:
            while self.product != -1:
                self.cond.wait()
            self.product = product
            self.cond.notify()
    
    def sellout(self) -> int:
        with self.cond:
            while self.product == -1:
                self.cond.wait()
            p = self.product

            self.product = -1
            self.cond.notify()
            return p

def producer(clerk: Clerk):
    for _ in range(10):
        product = int(10 * random.random())
        clerk.perchase(product)
        print(f"Perchase {product} products")

def consummer(clerk: Clerk):
    for _ in range(10):
        print(f"{clerk.sellout()} products is sold\n")

clerk = Clerk()
Thread(target=producer, args=(clerk, )).start()
Thread(target=consummer, args=(clerk, )).start()
