from simulator import Simulator
from simulator_subscriber import SimulatorSubscriber
from event import Event
from network_user import NetworkUser
from network_user import Drive

simulator = Simulator()
network_user1 = NetworkUser()
network_user2 = NetworkUser()

network_user1.subscribe_simulator(simulator)
network_user2.subscribe_simulator(simulator)

network_user1.register_event(network_user1.drive_event)
network_user2.register_event(network_user2.drive_event)

print('Simulator time:', network_user1.get_simulator_time())
print('Simulator time:', network_user2.get_simulator_time())

simulator.step()
simulator.step()

