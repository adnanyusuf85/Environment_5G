from typing import Dict, Optional, cast
from custom_types import EventUUID
from event import Event
from custom_types import SimulatorEntityUUID
from uuid import UUID, uuid4

class SimulatorEntity:

    def __init__(self):
        self.uuid:SimulatorEntityUUID = uuid4()
        self._events:Dict[UUID, Event] = dict()

    def act(self, event_uuid:EventUUID):
        self._events[event_uuid].execute()

    # def register_event(self, event_uuid:EventUUID):
        # self.check_simulator_interface()
        # self.simulator_interface.register_event(self.id, event_uuid)

    # def deregister_event(self, event_uuid:EventUUID):
        # self.check_simulator_interface()
        # self.simulator_interface.deregister_event(self.id, event_uuid)

    def add_event_to_queue(self, event:Event):
        self._events[event.entity_uuid] = event

    def remove_event_from_queue(self, event_uuid: EventUUID):
        del self._events[event_uuid]
