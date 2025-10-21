from typing import List
import heapq
from simulator_interface import SimulatorInterface
import custom_types

class Simulator:

    def __init__(self):
        # self.event_queue:List = heapq.heapify([])
        self._simulation_workers: List[SimulationWorker]= None
        self._event_queue: List[Event]
        self.interface: SimulatorInterface = SimulatorInterface(self)

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

    def add_event_to_queue(self, worker_uuid: WorkerUUID, event:EventUUID):
        heapq.heappush(self._event_queue)

    def remove_event_from_queue(self, event:EventUUID):
        # remove event where event.id = event.id