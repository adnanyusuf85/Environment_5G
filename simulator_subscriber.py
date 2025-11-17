from typing import Dict, Optional
from custom_types import EventUUID
from event import Event
from event_status import EventStatus
from simulator_interface import SimulatorInterface
from simulator_entity import SimulatorEntity
from typing import cast

class SimulatorSubscriber(SimulatorEntity):

    def subscribe_simulator(self, simulator_interface:SimulatorInterface):
        self.simulator_interface = simulator_interface
        self.simulator_interface.add_simulation_entity(self)

    def unsubscribe_simulator(self):
        self.simulator_interface = None

    def register_event(self, event:Event):
        self.add_event_to_queue(event)
        if (self.simulator_interface is not None and self.uuid is not None):
            self.simulator_interface.register_event(self.uuid, event)

    def unregister_event(self, event_uuid: EventUUID):
        self.remove_event_from_queue(event_uuid)
        del self._events[event_uuid]

    def notify_event(self, event: Event):
        if (self.simulator_interface is not None):
            self.simulator_interface.notify_status(event.event_id, event.status)
        # Resume here
    def get_simulator_time(self):
        return self.simulator_interface.get_time()