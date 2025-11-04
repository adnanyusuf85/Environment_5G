from typing import List, Optional
from heapq import heappush, heappop
import heapq
# from simulator_interface import SimulatorInterface
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import WorkerUUID, EventUUID
from event_status import EventStatus
from simulation_subscriber import SimulationWorker

class Simulator(SimulatorInterface):

    def __init__(self):
        # self._simulation_workers: List[SimulationWorker]
        self._event_queue: List[Event] = []
        self._simulation_workers: dict[WorkerUUID, SimulationWorker] = {}
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
    def add_simulation_worker(self, worker: SimulationWorker):
        self._simulation_workers[worker.id] = worker

    def remove_simulation_worker(self, worker_uuid: WorkerUUID):
        self._simulation_workers(worker_uuid).pop()

    def register_event(self, worker_uuid: WorkerUUID, event_uuid: EventUUID):
        pass

    def deregister_event(self, event:Event):
        pass

    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass


    # ########################################