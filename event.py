from uuid import UUID, uuid4
from custom_types import EventUUID
from event_status import EventStatus

class Event:
    def __init__(self, timestamp: int, entity_uuid: UUID):
        self.timestamp = timestamp
        self.event_id = uuid4()
        self.entity_uuid = entity_uuid
        self.status = EventStatus.PENDING

    def __lt__(self, other):
        return self.timestamp < other.timestamp 
    
    def execute(self):
        print(f"Executing event {self.event_id} at timestamp {self.timestamp} for worker {self.entity_uuid}")   
