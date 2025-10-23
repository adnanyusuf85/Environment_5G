from typing import List, Optional
from heapq import heappush, heappop
import heapq
# from simulator_interface import SimulatorInterface
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import WorkerUUID, EventUUID
from event_status import EventStatus

class Simulator(SimulatorInterface):

    def __init__(self):
        # self.event_queue:List = heapq.heapify([])
        # self._simulation_workers: List[SimulationWorker]
        self._event_queue: List[Event] = []
        # self.interface: SimulatorInterface = SimulatorInterface(self)

    def load_simulation_parameters(self, simulation_parameters: dict):
        self._simulation_parameters = simulation_parameters

    def start_simulation(self):
        print("Starting simulation...\n")

    def stop_simulation(self):
        print("Stopping simulation...\n")

    def step(self):
        heappop(self._event_queue).execute()
        print("Simulation step...\n")

    # SimulatorInterface methods
    def register_event(self, worker_uuid: WorkerUUID, event_uuid: EventUUID):
        pass

    def deregister_event(self, event:Event):
        pass

    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass


    # ########################################