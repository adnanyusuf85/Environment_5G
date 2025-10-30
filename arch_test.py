from typing import List


class Actable:

    def __init__(self, id):
        self.id = id


class Simulator:
    def __init__(self):
        self.actables: List[Actable] = []
        print("Initializing simulator...")

    def add_actable(self, actable:Actable):
        self.actables.append(actable)
        print("Adding actable with ID: ", actable.id)

    def remove_actable(self, id):
        if (self.actable.id == id):
            pass


class Worker(Actable):

    def __init__(self, id):
        super().__init__(id)
        print("Starting worker with ID: ", self.id)

    def set_simulator(self, simulator:Simulator):
        self.simulator = simulator


if __name__ == '__main__':
    print("Starting up...\n")
    worker1 = Worker(1)
    worker2 = Worker(2)

    simulator = Simulator()
    worker1.set_simulator(simulator)

    simulator.add_actable(worker1)
    simulator.add_actable(worker2)