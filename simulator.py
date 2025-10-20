from typing import List
import heapq

class Simulator:

    def __init__(self):
        # self.event_queue:List = heapq.heapify([])
        self._simulator_environment: SimulatorEnvironment = None

    def initialize_simulator():
        pass

    def load_environment(self, simulator_environment):
        self._simulator_environment = simulator_environment

    def start(self):
        self._simulator_environment.start()

    def stop(self):
        self._simulator_environment.stop()

    def restart(self):
        self._simulator_environment.restart()

    def step(self):
        # event = heapq.heappop(self.event_queue)
        self._simulator_environment.step()

    # def add_event(self, event:Event):
        # heapq.heappush(self.event_queue, event)