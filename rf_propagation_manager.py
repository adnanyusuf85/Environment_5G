from uuid import UUID
from custom_types import EventUUID
from event_emitter import EventEmitter

class RFPropagationManager(EventEmitter):


    # Implementation SimulatorCog
    event_list = []

    def initialize(self):
        pass

    def reset(self):
        pass

    def register_event(self, eventID:EventUUID):
        self.simulator.register_event(self, eventID)
        pass

    def action(self, eventID:EventUUID):
        self.event_list[eventID].execute()
        pass
    # ##############################