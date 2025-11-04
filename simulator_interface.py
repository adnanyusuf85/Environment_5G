from abc import ABC, abstractmethod
from event import Event
from custom_types import UUID, EventUUID, WorkerUUID
from event_status import EventStatus
from simulator_entity import SimulatorEntity

class SimulatorInterface:

    @abstractmethod
    def add_simulation_worker(self, worker: SimulatorEntity):
        pass

    @abstractmethod
    def remove_simulation_worker(self, worker_uuid: WorkerUUID):
        pass

    @abstractmethod
    def register_event(self, worker_uuid: WorkerUUID, event_uuid: EventUUID):
        pass

    @abstractmethod
    def deregister_event(self, event: Event):
        pass

    @abstractmethod
    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass
