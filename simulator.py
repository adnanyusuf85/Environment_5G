from typing import List, Optional, Tuple
from heapq import heappush, heappop
import heapq
# from simulator_interface import SimulatorInterface
from event import Event
from simulator_interface import SimulatorInterface
from custom_types import WorkerUUID, EventUUID, SimulatorEntityUUID
from event_status import EventStatus
from simulator_entity import SimulatorEntity

class Simulator(SimulatorInterface):

    def __init__(self):
        # self._simulation_workers: List[SimulationWorker]
        self._event_queue: List[Tuple[int,Event]] = []
        self._simulation_entities: dict[SimulatorEntityUUID, SimulatorEntity] = {}
        self._current_time: int = 0
        # self.interface: SimulatorInterface = SimulatorInterface(self)

    def load_simulation_parameters(self, simulation_parameters: dict):
        self._simulation_parameters = simulation_parameters

    def start_simulation(self):
        print("Starting simulation...\n")

    def stop_simulation(self):
        print("Stopping simulation...\n")

    def step(self):
        while (len(self._event_queue) != 0):

            if (self._current_time <= self._event_queue[0][0]):
                timestamp, next_event = heappop(self._event_queue)
                next_event.execute()
                self._current_time = next_event.timestamp


    # SimulatorInterface methods
    def add_simulation_entity(self, simulator_entity: SimulatorEntity):
        if simulator_entity.uuid is None:
            raise ValueError("Simulator entity must have a UUID before being added to the simulator.")
        self._simulation_entities[simulator_entity.uuid] = simulator_entity

    def remove_simulation_entity(self, simulator_entity_uuid: SimulatorEntityUUID):
        self._simulation_entities.pop(simulator_entity_uuid)

    def register_event(self, simulator_entity_uuid: SimulatorEntityUUID, event: Event):
        if simulator_entity_uuid not in self._simulation_entities:
            raise ValueError("Simulator entity not found in simulator.")
        heapq.heappush(self._event_queue, (event.timestamp, event))

    def deregister_event(self, event:Event):
        pass

    def notify_status(self, event_uuid: EventUUID, event_status: EventStatus):
        pass

    def get_time(self):
        return self._current_time


    # ########################################