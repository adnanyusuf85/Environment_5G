from typing import List


class Actable:

    def __init__(self, id):
        self.id = id
        print("Starting Actable with ID", self.id)

    def act(self):
        print("Actable with ID", self.id, "doing something...")

class Simulator:
    def __init__(self):
        self.actables: List[Actable] = []
        print("Initializing simulator...")

    def add_actable(self, actable:Actable):
        self.actables.append(actable)
        print("Adding actable with ID", actable.id)

    def remove_actable(self, id):
        for actable in self.actables:
            if (actable.id == id):
                self.actables.remove(actable)

    def step(self):
        for actable in self.actables:
            actable.act()

class Worker(Actable):

    def set_simulator(self, simulator:Simulator):
        self.simulator = simulator

    def act(self):
        print("Worker with ID", self.id, "working")


if __name__ == '__main__':
    print("Starting up...\n")
    worker1 = Worker(1)
    worker2 = Worker(2)

    simulator = Simulator()
    worker1.set_simulator(simulator)

    simulator.add_actable(worker1)
    simulator.add_actable(worker2)

    simulator.step()

    simulator.remove_actable(worker1.id)

    print("Removed one actable")

    simulator.step()
