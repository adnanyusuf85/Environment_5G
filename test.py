from simulator import Simulator
from simulator_subscriber import SimulatorSubscriber  
from event import Event

simulator = Simulator()
simsub1 = SimulatorSubscriber()
simsub1.subscribe_simulator(simulator)
simsub2 = SimulatorSubscriber()
simsub2.subscribe_simulator(simulator)


event = Event(1, simsub1.uuid)
event2 = Event(3, simsub2.uuid)
simulator.register_event(simsub1.uuid, event)
simulator.register_event(simsub2.uuid, event2)
simulator.step()
simulator.step()