from abc import ABC, abstractmethod
from simulator import Simulator
from event import Event
from custom_types import UUID, EventUUID
from simulation_worker import SimulationWorker


class SimulatorInterface:

    @abstractmethod
    def register_event(self, worker_uuid: UUID, event: Event):
        pass

    @abstractmethod
    def deregister_event(self, event: Event):
        pass

    @abstractmethod
    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass

    @abstractmethod
    def add_worker(self, worker: SimulationWorker):
        pass

    @abstractmethod
    def remove_worker(self, worker: SimulationWorker):
        pass