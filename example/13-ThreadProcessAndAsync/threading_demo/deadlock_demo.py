from threading import Thread, Lock

class Resource:

    def __init__(self, name: str, resource: int) -> None:
        self.name = name
        self.resource = resource
        self.lock = Lock()

    def action(self) -> int:
        with self.lock:
            self.resource += 1
            return self.resource
    
    def cooperate(self, other_res: Resource):
        with self.lock:
            other_res.action()
            print(f"{self.name} is intergrating {other_res.name}")

def cooperate(r1:Resource, r2: Resource):
    for _ in range(10):
        r1.cooperate(r2)
    
res1 = Resource("Res 1", 10)
res2 = Resource("Res 2", 20)

th12 = Thread(target=cooperate, args=(res1, res2))
th21 = Thread(target=cooperate, args=(res2, res1))

th12.start()
th21.start()
