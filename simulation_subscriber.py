from typing import Dict
from custom_types import EventUUID
from event import Event
from simulator_interface import SimulatorInterface
from simulator_entity import SimulatorEntity

class SimulationSubscriber(SimulatorEntity):

    def __init__(self, simulator:SimulatorInterface):
        self.simulator_interface:SimulatorInterface = simulator

    def subscribe_simulator(self, simulator_interface:SimulatorInterface):
        self.simulator_interface = simulator_interface

    def unsubscribe_simulator(self):
        self.simulator_interface = None

    def register_event(self, event:Event):
        self.add_event_to_queue(event)
        self.simulator_interface.register_event(self.uuid, event.event_id)

    def unregister_event(self, event_uuid: EventUUID):
        self.remove_event_from_queue(event_uuid)
        del self._events[event_uuid]

    def get_simulator_time(self):
        return self.simulator_interface.get_time()

    def notify_event(self, event: Event):
        pass
        # self.simulator_interface.notify_status(event.event_id:EventUUID, event.event_status:EventStatus)
        # Resume here
