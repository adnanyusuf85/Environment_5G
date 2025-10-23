from abc import ABC, abstractmethod
from event import Event
from custom_types import UUID, EventUUID, WorkerUUID
from event_status import EventStatus

class SimulatorInterface:

    @abstractmethod
    def register_event(self, worker_uuid: WorkerUUID, event_uuid: EventUUID):
        pass

    @abstractmethod
    def deregister_event(self, event: Event):
        pass

    @abstractmethod
    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass
