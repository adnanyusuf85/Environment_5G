from typing import List, Optional
from heapq import heappush, heappop
import heapq
# from simulator_interface import SimulatorInterface
from simulation_worker import SimulationWorker
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import WorkerUUID, EventUUID

class Simulator(SimulatorInterface):

    def __init__(self):
        # self.event_queue:List = heapq.heapify([])
        self._simulation_workers: List[SimulationWorker] 
        self._event_queue: List[Event] = []
        # self.interface: SimulatorInterface = SimulatorInterface(self)

    def load_simulation_parameters(self, simulation_parameters: dict):
        self._simulation_parameters = simulation_parameters

    def start_simulation(self):
        pass

    def stop_simulation(self):
        pass

    def step(self):
        heappop(self._event_queue).execute()

    # SimulatorInterface methods
    def register_event(self, worker_uuid: WorkerUUID, event_uuid: EventUUID):
        pass

    def deregister_event(self, event:Event):
        pass

    def notify_status(self, event_uuid: EventUUID, event_status: str):
        pass

    def add_worker(self, worker: SimulationWorker):
        self._simulation_workers.append(worker)

    def remove_worker(self, worker: SimulationWorker):
        self._simulation_workers.remove(worker)

    # ######################################## 