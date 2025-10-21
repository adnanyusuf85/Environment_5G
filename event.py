class Event:
    def __init__(self, timestamp: int, event_id: str, worker_uuid: str):
        self.timestamp = timestamp
        self.event_id = event_id
        self.worker_uuid = worker_uuid

    def __lt__(self, other):
        return self.timestamp < other.timestamp 
    
    def execute(self):
        print(f"Executing event {self.event_id} at timestamp {self.timestamp} for worker {self.worker_uuid}")   
