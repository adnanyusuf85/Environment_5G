from abc import ABC, abstractmethod
from simulator import Simulator

class SimulatorInterface:

    def __init__(self, simulator: Simulator):
        self._simulator = simulator

    def register_event(self, worker_uuid: UUID, event_uuid: EventUUID):
        self._simulator.add_event_to_queue(worker_uuid, event_uuid)

    def deregister_event(self, event_uuid: EventUUID):
        pass

    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass

    def add_worker(self, worker: SimulatonWorker):
        pass

    def remove_worker(self, worker: SimulationWorker):
        pass