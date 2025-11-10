from uuid import UUID

class Event:
    def __init__(self, timestamp: int, event_id: str, entity_uuid: UUID):
        self.timestamp = timestamp
        self.event_id = event_id
        self.entity_uuid = entity_uuid

    def __lt__(self, other):
        return self.timestamp < other.timestamp 
    
    def execute(self):
        print(f"Executing event {self.event_id} at timestamp {self.timestamp} for worker {self.worker_uuid}")   
