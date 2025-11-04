from typing import Dict
from custom_types import EventUUID
from event import Event
from simulator_interface import SimulatorInterface

class SimulationSubscriber:

    def __init__(self, simulator:SimulatorInterface):
        self.simulator_interface:SimulatorInterface = simulator

    def set_simulator(self, simulator_interface:SimulatorInterface):
        self.simulator_interface = simulator_interface

    def act(self, event_uuid: EventUUID):
        self._event_queue[event_uuid].execute()