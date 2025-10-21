from simulator import Simulator
from event import Event

event_a = Event(timestamp=10, event_id="event_1", worker_uuid="worker_1")
event_b = Event(timestamp=5, event_id="event_2", worker_uuid="worker_2")
event_c = Event(timestamp=20, event_id="event_3", worker_uuid="worker_3")

sim = Simulator()
sim.add_event_to_queue(event_c)
sim.add_event_to_queue(event_b)
sim.add_event_to_queue(event_a)

sim.step()
sim.step()
sim.step()