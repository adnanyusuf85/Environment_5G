from typing import Dict
from custom_types import EventUUID
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import SimulatorEntityUUID

class SimulatorEntity:

    def __init__(self):
        self.uuid:SimulatorEntityUUID = None
        self.simulator_interface:SimulatorInterface = None
        self._events:Dict[EventUUID, Event]

    def act(self, event_uuid:EventUUID):
        self._event_list[event_uuid].execute()

    def register_event(self, event_uuid:EventUUID):
        self.check_simulator_interface()
        self.simulator_interface.register_event(self.id, event_uuid)

    def deregister_event(self, event_uuid:EventUUID):
        self.check_simulator_interface()
        self.simulator_interface.deregister_event(self.id, event_uuid)

    def check_simulator_interface(self):
        if(self.simulator_interface == None):
            raise TypeError("Simulator Interface not set, cannot perform operation")