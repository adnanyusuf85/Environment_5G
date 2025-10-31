from typing import Dict
from custom_types import EventUUID
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import WorkerUUID

class SimulatorActable:

    def __init__(self, simulator:SimulatorInterface):
        self.id:WorkerUUID = None
        self.simulator_interface:SimulatorInterface = simulator
        self._events:Dict[EventUUID, Event]

    def set_simulator(self, simulator_interface:SimulatorInterface):
        self.simulator_interface = simulator_interface

    def act(self, event_uuid: EventUUID):
        self._event_list[event_uuid].execute()

    def