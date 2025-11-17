from abc import ABC, abstractmethod
from event import Event
from custom_types import UUID, EventUUID, WorkerUUID, SimulatorEntityUUID
from event_status import EventStatus
from simulator_entity import SimulatorEntity

class SimulatorInterface:

    @abstractmethod
    def add_simulation_entity(self, simulator_entity: SimulatorEntity):
        pass

    @abstractmethod
    def remove_simulation_entity(self, simulator_entity_uuid: SimulatorEntityUUID):
        pass

    @abstractmethod
    def register_event(self, simulator_entity_uuid: SimulatorEntityUUID, event: Event):
        pass

    @abstractmethod
    def deregister_event(self, event: Event):
        pass

    @abstractmethod
    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass

    @abstractmethod
    def get_time(self):
        pass
